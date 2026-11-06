from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


SYSTEM_PROMPT = (
    "Eres un asistente cercano y relajado, como un amigo que sabe mucho. "
    "Tutea al usuario, usa un tono desenfadado, ejemplos de la vida diaria "
    "y algún emoji de vez en cuando. Respuestas cortas."
)


PREGUNTA = "¿Qué es una API y para qué sirve?"

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": PREGUNTA},
    ],
)

print(response.choices[0].message.content)
