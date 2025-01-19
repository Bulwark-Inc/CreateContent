from django.test import TestCase
from rest_framework.test import APIClient

class ChatGPTViewTest(TestCase):
    def test_chatgpt_response(self):
        client = APIClient()
        response = client.post('/api/chat/', {'message': 'Hello, ChatGPT!'}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('response', response.json())
