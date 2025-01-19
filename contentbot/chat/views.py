import asyncio
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .utils import chatbot_response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.throttling import UserRateThrottle
from .models import ChatLog

class ChatbotAPIView(APIView):
    """
    A view to handle requests to ChatGPT and respond with its output.
    """
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    
    def post(self, request):
        user_input = request.data.get("message", "")
        if not user_input:
            return Response({"error": "Message is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            response = asyncio.run(chatbot_response(user_input))

            # Save to database
            ChatLog.objects.create(user_message=user_input, bot_response=response)

            return Response({"response": response}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"An error occurred while processing your request: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
