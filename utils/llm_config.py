from mistralai import Mistral
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm():
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("MISTRAL_API_KEY not found in environment variables")
    
    return Mistral(api_key=api_key)

def generate_response(client, prompt):
    response = client.chat.complete(
        model="mistral-large-latest",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )
    return response.choices[0].message.content