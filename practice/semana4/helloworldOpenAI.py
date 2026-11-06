from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # lee GOOGLE_API_KEY del archivo .env

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {"role":"user","content":"Say hi"}
    ]
)

print(response.choices[0].message.content)