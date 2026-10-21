import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={API_KEY}"

data = {
    "contents": [{
        "parts": [{"text": "¿Qué es async en Python? (respuesta corta)"}]
    }]
}

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    text = result['candidates'][0]['content']['parts'][0]['text']
    print(f"✅ Gemini 3.8 Flash working!\n\n{text}")
else:
    print(f"❌ Error {response.status_code}: {response.text}")