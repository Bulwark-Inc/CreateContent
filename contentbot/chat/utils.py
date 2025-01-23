from openai import AsyncOpenAI
from django.conf import settings

# Initialize the OpenAI client with your API key
client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

async def chatbot_response(user_input):
    try:
        # Determine language style dynamically (if provided, or default to both)
        language_style = "You always use good simple plain English Language except when prompted in pidgin, and take not of simple typographical error not to confuse such for pidgin" 

        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": (
                    "You are a content creation assistant. Your job includes:\n"
                    "1. Ideating content creation scripts.\n"
                    "2. Generating content scripts.\n"
                    "3. Pivoting towards discussing execution of the scripts when prompted, "
                    "even though you can't execute them directly.\n\n"
                    f"{language_style}\n"
                    "Ensure your tone is natural and friendly. Provide varied responses to similar prompts to avoid repetition."
                )},
                {"role": "user", "content": user_input}
            ],
            max_tokens=200,
            temperature=0.9,
            top_p=1.0,
        )
        # Return the generated response
        return response.choices[0].message.content.strip()
    except Exception as e:
        # Handle errors gracefully
        return f"Sorry, I couldn't process that request right now: {e}"
    
