from openai import OpenAI, InternalServerError, RateLimitError, APITimeoutError
from dotenv import load_dotenv
import os
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()  # lee GOOGLE_API_KEY del archivo .env

# Modelo principal primero; los demás son de respaldo si está saturado
MODELOS = ["gemini-3.8-flash", "gemini-flash-lite-latest", "gemini-3-flash-preview"]

console = Console()
client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",  # Gemini con el SDK de OpenAI
    max_retries=1,  # 1 reintento por modelo, para no esperar demasiado
    timeout=30,  # si en 30 s no responde, pasamos al siguiente modelo
)

def chat(user_message: str, history: list) -> str:
    """Envía mensaje y devuelve respuesta"""
    history.append({"role": "user", "content": user_message})

    # Si un modelo está saturado (503), sin cuota (429) o no responde, probamos con el siguiente
    for model in MODELOS:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=history,
                temperature=0.7
            )
            break
        except (InternalServerError, RateLimitError, APITimeoutError) as e:
            console.print(f"[dim]{model} no disponible ({type(e).__name__}), probando otro modelo...[/dim]")
    else:
        history.pop()  # quitamos la pregunta sin respuesta del historial
        return "⚠️ Ningún modelo está disponible ahora mismo. Espera un minuto y vuelve a intentarlo."

    assistant_message = response.choices[0].message.content
    history.append({"role": "assistant", "content": assistant_message})
    
    return assistant_message

def main():
    console.print("[bold green]Chatbot CLI[/bold green]")
    console.print("Escribe 'exit' para salir\n")
    
    history = [
        {"role": "system", "content": "Eres un asistente útil y conciso."}
    ]
    
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "exit":
            break
        
        response = chat(user_input, history)
        console.print("\n[bold blue]Bot:[/bold blue]")
        console.print(Markdown(response))
        console.print()

if __name__ == "__main__":
    main()