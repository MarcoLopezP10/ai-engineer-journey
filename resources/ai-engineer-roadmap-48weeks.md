# 🚀 Plan Completo: De Data Science a AI Engineer
## 48 Semanas | 6h/semana | Octubre 2026 - Septiembre 2027

**Marco Lopez Prieto** | Madrid, España | Inicio: 14 Octubre 2026

---

## 📋 Índice

- [Contexto y Objetivos](#contexto-y-objetivos)
- [Setup Inicial](#setup-inicial)
- [Fase 1: Fundamentos (Oct-Dic)](#fase-1-fundamentos-oct-dic)
- [Fase 2: Backend + RAG (Ene-Mar)](#fase-2-backend-rag-ene-mar)
- [Fase 3: Producción + Agents (Abr-Jun)](#fase-3-producción-agents-abr-jun)
- [Fase 4: Deploy + Empleo (Jul-Sep)](#fase-4-deploy-empleo-jul-sep)
- [Recursos Generales](#recursos-generales)
- [Networking Madrid](#networking-madrid)
- [Preparación Entrevistas](#preparación-entrevistas)

---

## Contexto y Objetivos

### Tu situación actual (según CV):
✅ **Ya dominas:**
- Python (full-stack app, 1200+ líneas, modular)
- Git/GitHub (version control, collaborative workflows)
- SQL y REST APIs (Supabase)
- Testing y debugging
- Parallel computing (threading, multiprocessing)
- Software engineering (abstracciones, interfaces)

⚠️ **Necesitas desarrollar:**
- LLMs y AI (prompting, embeddings, RAG)
- Backend moderno (FastAPI, async, APIs production-ready)
- Docker y cloud (AWS)
- AI tooling (LangChain, vector DBs)
- Deployment real (CI/CD, monitoring)
- Portfolio público con proyectos AI

### Objetivo final: Septiembre 2027
**Perfil:** AI Engineer Junior en Madrid
- 4 proyectos desplegados y públicos
- Stack: Python, FastAPI, LLMs, RAG, Docker, AWS
- Portfolio en GitHub
- CV actualizado + LinkedIn optimizado
- Preparado para entrevistas técnicas

### Filosofía del plan
**70% HACER | 20% ESTUDIAR | 10% NETWORKING**

No vas a ser experto en todo. Vas a ser **competente construyendo productos AI end-to-end**.

---

## Setup Inicial

### Semana 0 (7-13 Octubre 2026)
**Objetivo:** Entorno listo para empezar el lunes 14.

#### ⚙️ Software a instalar

```bash
# 1. Python 3.11+ (si no lo tienes actualizado)
# Descarga: https://www.python.org/downloads/
python --version  # debe ser 3.11 o superior

# 2. VS Code (si no lo usas ya)
# Descarga: https://code.visualstudio.com/

# Extensiones recomendadas para VS Code:
# - Python (Microsoft)
# - Pylance
# - Python Debugger
# - GitLens
# - Docker
# - Thunder Client (para probar APIs)
# - Markdown All in One

# 3. Git (ya lo tienes)
git --version

# 4. Docker Desktop
# Descarga: https://www.docker.com/products/docker-desktop/
# IMPORTANTE: Tras instalar, reinicia y verifica
docker --version
docker compose version

# 5. PostgreSQL (local)
# Descarga: https://www.postgresql.org/download/
# O usa Docker (más fácil):
docker run --name postgres-local -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres

# 6. Postman o Thunder Client
# Para probar APIs: https://www.postman.com/downloads/

# 7. UV (gestor de paquetes Python moderno, opcional pero recomendado)
pip install uv
```

#### 📁 Estructura de carpetas

```bash
mkdir -p ~/ai-engineer-journey
cd ~/ai-engineer-journey

# Estructura:
# ai-engineer-journey/
# ├── learning/          # notas, tutoriales, ejercicios
# ├── projects/          # tus 4 proyectos principales
# ├── practice/          # código de práctica
# └── resources/         # PDFs, cheat sheets, etc.
```

#### 🔑 Cuentas necesarias

1. **Gemini** (necesitas API key)
   - cuenta con IE
   - https://aistudio.google.com/api-keys?original_referer=https:%2F%2Fnebulaone.ie.edu
   

2. **Anthropic** (opcional, alternativa)
   - https://www.anthropic.com/
   - API de Claude

3. **GitHub** (ya tienes)
   - Verifica que tu perfil esté actualizado
   - Foto profesional
   - Bio clara

4. **Docker Hub**
   - https://hub.docker.com/
   - Para subir imágenes 
   - (con IE) marcolopez232 // ***REMOVED***

5. **AWS** (crearás cuenta en Fase 4)
   - https://aws.amazon.com/
   - Free tier (12 meses gratis)

#### 📚 Bookmark estas páginas

- [OpenAI API Docs](https://platform.openai.com/docs)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [LangChain Docs](https://python.langchain.com/)
- [Docker Docs](https://docs.docker.com/)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)
- [Real Python](https://realpython.com/)
- [AWS Docs](https://docs.aws.amazon.com/)

#### ✅ Checklist pre-inicio
- [✅ ] Python 3.11+ instalado
- [ ✅] VS Code configurado con extensiones
- [ ✅] Docker funcionando (prueba: `docker run hello-world`)
- [✅ ] PostgreSQL accesible
- [✅ ] Cuenta Google con crédito
- [ ✅] GitHub profile actualizado
- [✅ ] Estructura de carpetas creada
- [✅ ] Este documento guardado y accesible

---

# FASE 1: FUNDAMENTOS
## Octubre - Diciembre 2026 (12 semanas)

### Objetivo de la fase
Dominar las herramientas core de AI Engineer: Python moderno, LLMs, APIs, y construir tu primer proyecto AI end-to-end.

**Proyecto final:** CLI AI Assistant con OpenAI API

---

## Semana 1: Python Moderno + Async Basics
**14-20 Octubre 2026**

### 🎯 Objetivo
Refrescar Python moderno (ya lo sabes, pero vamos a nivelar hacia backend async) y entender type hints, pydantic, y async/await.

### 📖 Conceptos clave

**Type hints:** Anotaciones que mejoran IDE autocomplete y previenen bugs.
```python
def greet(name: str) -> str:
    return f"Hello {name}"
```

**Pydantic:** Validación de datos con clases Python.
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

user = User(name="Marco", age=25, email="marco@example.com")
# Si pasas age="twenty" → ValidationError
```

**Async/await:** Permite que tu programa "espere" operaciones I/O (APIs, DB) sin bloquear.
```python
import asyncio

async def fetch_data():
    await asyncio.sleep(1)  # simula llamada API
    return "data"

# Útil cuando haces muchas llamadas a APIs externas
```

### 📚 Recursos

**Videos:**
- [Async Python en 20min - ArjanCodes](https://www.youtube.com/watch?v=2IW-ZEui4h4) (20min)
- [Pydantic en 10min](https://www.youtube.com/watch?v=502XOB0u8OY) (10min)
- [Type Hints - Real Python](https://realpython.com/lessons/type-hinting/) (15min)

**Artículos:**
- [Async Python oficial](https://docs.python.org/3/library/asyncio.html)
- [Pydantic docs - intro](https://docs.pydantic.dev/latest/)

**Repos de referencia:**
- https://github.com/tiangolo/fastapi (mira cómo usan Pydantic)

### 🗓️ Plan día a día (6h total)

**Lunes (1h):**
- Ver video Async Python (20min)
- Leer docs asyncio básico (20min)
- Ejercicio: Escribir 3 funciones async que simulen llamadas API con `asyncio.sleep()` y ejecutarlas concurrentemente

**Martes (1h):**
- Ver video Pydantic (10min)
- Leer Pydantic quickstart (20min)
- Ejercicio: Crear 3 modelos Pydantic (User, Product, Order) con validaciones

**Miércoles (1.5h):**
- Leer sobre Type Hints en Real Python (30min)
- Ejercicio: Tomar tu proyecto PSO antiguo y añadir type hints a todas las funciones (1h)

**Jueves (1h):**
- Combinar async + Pydantic
- Ejercicio: Función async que "fetch" datos de 3 URLs simuladas y devuelva una lista de modelos Pydantic validados

**Viernes (1.5h):**
- Code review de tu código de la semana
- Refactorizar y documentar
- Subir a GitHub en carpeta `practice/week01-async-pydantic/`

### 💻 Ejercicio principal de la semana

Crea `async_data_fetcher.py`:

```python
import asyncio
from pydantic import BaseModel, HttpUrl
from typing import List
import random

class APIResponse(BaseModel):
    url: HttpUrl
    status: int
    data: str

async def fetch_url(url: str, delay: float) -> APIResponse:
    """Simula llamada API async"""
    await asyncio.sleep(delay)
    return APIResponse(
        url=url,
        status=200,
        data=f"Data from {url}"
    )

async def fetch_all(urls: List[str]) -> List[APIResponse]:
    """Fetch múltiples URLs concurrentemente"""
    tasks = [fetch_url(url, random.uniform(0.5, 2.0)) for url in urls]
    return await asyncio.gather(*tasks)

async def main():
    urls = [
        "https://api.example.com/users",
        "https://api.example.com/products",
        "https://api.example.com/orders"
    ]
    
    print("Fetching data...")
    responses = await fetch_all(urls)
    
    for resp in responses:
        print(f"{resp.url} → {resp.status}: {resp.data}")

if __name__ == "__main__":
    asyncio.run(main())
```

Ejecútalo y observa que las 3 "llamadas" ocurren concurrentemente.

### ✅ Checklist
- [✅ ] Entiendo qué es async/await y cuándo usarlo
- [ ✅] Sé crear modelos Pydantic con validaciones
- [✅ ] He añadido type hints a código antiguo
- [✅ ] Ejercicio principal completado y funciona
- [✅ ] Código en GitHub

---

## Semana 2: APIs REST + FastAPI Intro
**21-27 Octubre 2026**

### 🎯 Objetivo
Dominar FastAPI para construir APIs modernas (vas a usarlo TODO el año).

### 📖 Conceptos clave

**REST API:** Arquitectura para comunicar sistemas via HTTP.
- GET: obtener datos
- POST: crear datos
- PUT: actualizar
- DELETE: eliminar

**FastAPI:** Framework Python async para APIs. Ventajas:
- Muy rápido
- Validación automática (usa Pydantic)
- Documentación automática (Swagger UI)
- Type hints nativos

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Auto-genera docs en /docs
```

**Path params vs Query params:**
```python
# Path param: /users/123
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# Query param: /search?q=marco
@app.get("/search")
def search(q: str):
    return {"query": q}
```

### 📚 Recursos

**Videos:**
- [FastAPI en 1 hora - freeCodeCamp](https://www.youtube.com/watch?v=0sOvCWFmrtA) (1h)
- [REST API explicado en 10min](https://www.youtube.com/watch?v=SLwpqD8n3d0) (10min)

**Docs:**
- [FastAPI Tutorial oficial](https://fastapi.tiangolo.com/tutorial/) (lee hasta "Request Body")

**Repos:**
- https://github.com/tiangolo/fastapi (el oficial)
- https://github.com/zhanymkanov/fastapi-best-practices

### 🗓️ Plan día a día (6h total)

**Lunes (1.5h):**
- Ver video REST API explicado (10min) OK
- Ver FastAPI tutorial hasta min 30 (30min) OK
- Instalar FastAPI: `pip install "fastapi[all]" uvicorn` OK
- Ejercicio: Crear tu primer "Hello World" API y abrirla en http://localhost:8000/docs OK

**Martes (1.5h):**
- Continuar video FastAPI hasta min 60 (30min) OK 
- Ejercicio: Crear API con 3 endpoints:
  - GET /items → devuelve lista de items
  - GET /items/{id} → devuelve item específico
  - POST /items → crea nuevo item

**Miércoles (1.5h):**
- Leer FastAPI docs: Request Body y Response Model
- Ejercicio: Añadir modelos Pydantic a tu API de items
  - `class Item(BaseModel): name: str, price: float`
  - Validar input del POST

**Jueves (1h):**
- Leer sobre error handling en FastAPI
- Ejercicio: Añadir manejo de errores (404 si item no existe, 422 si validación falla)

**Viernes (1.5h):**
- Construir una "Mini CRUD API" completa:
  - GET, POST, PUT, DELETE
  - Con Pydantic models
  - Con manejo de errores
  - Documentado en /docs
- Subir a GitHub: `projects/week02-fastapi-crud/`

### 💻 Ejercicio principal: CRUD API de Tareas

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI(title="Tasks API")

class Task(BaseModel):
    id: Optional[str] = None
    title: str
    description: Optional[str] = None
    completed: bool = False

# "Database" en memoria
tasks_db = {}

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: Task):
    task_id = str(uuid.uuid4())
    task.id = task_id
    tasks_db[task_id] = task
    return task

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return list(tasks_db.values())

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, task: Task):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    task.id = task_id
    tasks_db[task_id] = task
    return task

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks_db[task_id]
    return None

# Para ejecutar: uvicorn main:app --reload
# Docs en: http://localhost:8000/docs
```

**Prueba:**
1. Abre http://localhost:8000/docs
2. Crea varias tareas con POST
3. Lístala con GET
4. Actualiza una con PUT
5. Bórrala con DELETE

### ✅ Checklist
- [ ] Entiendo REST y los métodos HTTP
- [ ] Sé crear APIs con FastAPI
- [ ] Uso Pydantic para validación
- [ ] He probado mi API en /docs (Swagger UI)
- [ ] CRUD API funciona completamente
- [ ] Código en GitHub con README

---

## Semana 3: Git Avanzado + Testing
**28 Octubre - 3 Noviembre 2026**

### 🎯 Objetivo
Git profesional (branches, PRs, workflows) y testing automático (pytest).

### 📖 Conceptos clave

**Git branches:** Trabajar en features sin romper main.
```bash
git checkout -b feature/new-endpoint
# haces cambios
git add .
git commit -m "Add new endpoint"
git checkout main
git merge feature/new-endpoint
```

**Pull Requests (PRs):** Forma profesional de integrar código. Permiten code review.

**Testing con pytest:** Tests automáticos para verificar que tu código funciona.
```python
def add(a, b):
    return a + b

# test_math.py
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

**Test coverage:** % de código cubierto por tests. Objetivo: >80%.

### 📚 Recursos

**Videos:**
- [Git branches en 10min](https://www.youtube.com/watch?v=e2IbNHi4uCI) (10min)
- [Pytest en 20min - ArjanCodes](https://www.youtube.com/watch?v=cHYq1MRoyI0) (20min)

**Docs:**
- [Pytest docs](https://docs.pytest.org/en/stable/getting-started.html)
- [Git branching tutorial](https://learngitbranching.js.org/)

**Repos:**
- https://github.com/pytest-dev/pytest (ver estructura de tests)

### 🗓️ Plan día a día (6h total)

**Lunes (1h):**
- Jugar con [learngitbranching.js.org](https://learngitbranching.js.org/) (30min)
- Practicar en un repo: crear branch, hacer commit, merge (30min)

**Martes (1.5h):**
- Ver video pytest (20min)
- Instalar pytest: `pip install pytest pytest-cov`
- Ejercicio: Escribir 5 tests simples para funciones matemáticas

**Miércoles (1.5h):**
- Leer pytest docs: fixtures, parametrize
- Ejercicio: Escribir tests para tu CRUD API de la semana pasada
  - Test POST crea tarea
  - Test GET devuelve tareas
  - Test 404 cuando no existe

**Jueves (1h):**
- Configurar GitHub Actions (CI) básico
- Archivo `.github/workflows/tests.yml`:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest
```

**Viernes (1h):**
- Integrar todo: tu API + tests + CI
- Hacer un PR desde una branch a main con tests pasando
- Subir proyecto completo a GitHub

### 💻 Ejercicio principal: Tests para CRUD API

```python
# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks", json={
        "title": "Test task",
        "description": "Testing",
        "completed": False
    })
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test task"
    assert "id" in data

def test_get_tasks():
    # Crear una tarea primero
    client.post("/tasks", json={"title": "Task 1"})
    
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_task_not_found():
    response = client.get("/tasks/nonexistent")
    assert response.status_code == 404

def test_update_task():
    # Crear tarea
    create_response = client.post("/tasks", json={"title": "Original"})
    task_id = create_response.json()["id"]
    
    # Actualizar
    update_response = client.put(f"/tasks/{task_id}", json={
        "title": "Updated",
        "completed": True
    })
    assert update_response.status_code == 200
    assert update_response.json()["title"] == "Updated"

def test_delete_task():
    # Crear tarea
    create_response = client.post("/tasks", json={"title": "To delete"})
    task_id = create_response.json()["id"]
    
    # Borrar
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 204
    
    # Verificar que ya no existe
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404
```

**Ejecutar:**
```bash
pytest test_main.py -v
pytest --cov=main --cov-report=term-missing
```

### ✅ Checklist
- [ ] Sé trabajar con branches y merges
- [ ] He practicado en learngitbranching.js.org
- [ ] Domino pytest básico
- [ ] Mi API tiene tests con >80% coverage
- [ ] GitHub Actions ejecuta tests automáticamente
- [ ] He hecho un PR completo

---

## Semana 4: Fundamentos de LLMs
**4-10 Noviembre 2026**

### 🎯 Objetivo
Entender cómo funcionan los LLMs y cómo usarlos via API (OpenAI).

### 📖 Conceptos clave

**LLM (Large Language Model):** Modelo entrenado con billones de palabras. Ejemplos: GPT-4, Claude, Llama.

**Tokens:** Unidad de procesamiento. ~4 caracteres = 1 token. "Hola mundo" = ~3 tokens.
- Importante porque las APIs cobran por token.
- Context window: máximo de tokens (input + output). GPT-4: 128K tokens.

**Temperature:** Controla "creatividad" del modelo.
- 0.0 = determinista, respuestas consistentes
- 1.0 = creativo, respuestas variadas
- 2.0 = muy aleatorio (raramente útil)

**System prompt vs User prompt:**
```python
messages = [
    {"role": "system", "content": "Eres un asistente experto en Python."},
    {"role": "user", "content": "Explícame qué son las decoradores."}
]
```
- System: instrucciones generales, tono, personalidad
- User: la pregunta específica

**Streaming:** Recibir respuesta token por token (como ChatGPT).

### 📚 Recursos

**Videos:**
- [¿Cómo funcionan los LLMs? - 3Blue1Brown](https://www.youtube.com/watch?v=wjZofJX0v4M) (30min) ⭐
- [OpenAI API en 15min](https://www.youtube.com/watch?v=c-g6epk3fFE) (15min)

**Artículos:**
- [OpenAI API Quickstart](https://platform.openai.com/docs/quickstart)
- [Prompt Engineering Guide](https://www.promptingguide.ai/introduction/basics)

**Docs:**
- [OpenAI Python SDK](https://github.com/openai/openai-python)

### 🗓️ Plan día a día (6h total)

**Lunes (1h):**
- Ver video 3Blue1Brown sobre LLMs (30min) - FUNDAMENTAL
- Leer OpenAI Quickstart (30min)

**Martes (1.5h):**
- Crear cuenta OpenAI, añadir crédito, generar API key
- Instalar SDK: `pip install openai`
- Primer script: "Hello world" con OpenAI

```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Di hola"}
    ]
)

print(response.choices[0].message.content)
```

**Miércoles (1.5h):**
- Experimentar con temperature y system prompts
- Ejercicio: Crear 3 scripts con diferentes system prompts:
  1. Asistente formal
  2. Asistente casual
  3. Asistente técnico experto
- Comparar respuestas

**Jueves (1.5h):**
- Leer sobre structured outputs (JSON mode)
- Ejercicio: Hacer que el LLM devuelva JSON estructurado

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Dame info de 3 lenguajes de programación"}
    ],
    response_format={"type": "json_object"}
)
```

- Combinar con Pydantic para validar

**Viernes (1.5h):**
- Construir CLI interactivo básico:
  - Usuario escribe pregunta
  - Script llama OpenAI
  - Muestra respuesta
  - Loop hasta que usuario escribe "exit"

### 💻 Ejercicio principal: CLI Chatbot

```python
# chatbot.py
from openai import OpenAI
import os
from rich.console import Console
from rich.markdown import Markdown

console = Console()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat(user_message: str, history: list) -> str:
    """Envía mensaje y devuelve respuesta"""
    history.append({"role": "user", "content": user_message})
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=history,
        temperature=0.7
    )
    
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
```

**Instalar dependencias:**
```bash
pip install openai rich
export OPENAI_API_KEY="tu-api-key"
python chatbot.py
```

### ✅ Checklist
- [ ] Entiendo qué son tokens y context window
- [ ] Sé qué hace temperature
- [ ] He usado OpenAI API exitosamente
- [ ] Experimento con system prompts
- [ ] Chatbot CLI funciona
- [ ] Código en GitHub

---

## Semana 5: Prompt Engineering
**11-17 Noviembre 2026**

### 🎯 Objetivo
Aprender a escribir prompts efectivos. Esta es una habilidad CORE de AI Engineer.

### 📖 Conceptos clave

**Prompt Engineering:** Arte de instruir al LLM para obtener mejores resultados.

**Técnicas principales:**

1. **Few-shot prompting:** Dar ejemplos
```
Clasifica el sentimiento:

Texto: "Me encanta este producto!"
Sentimiento: positivo

Texto: "No funciona bien"
Sentimiento: negativo

Texto: "El servicio es terrible"
Sentimiento: ?
```

2. **Chain of Thought (CoT):** Pedir que "piense paso a paso"
```
Resuelve: 15 * 24

Piensa paso a paso:
```

3. **Role prompting:** Asignar un rol
```
Eres un ingeniero senior con 10 años de experiencia en Python...
```

4. **Structured output:** Forzar formato
```
Responde en JSON con formato:
{
  "summary": "...",
  "key_points": [...]
}
```

### 📚 Recursos

**Guías:**
- [Prompt Engineering Guide](https://www.promptingguide.ai/) (lee todo "Techniques")
- [OpenAI Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)

**Videos:**
- [Prompt Engineering en 17min](https://www.youtube.com/watch?v=dOxUroR57xs) (17min)

**Papers:**
- [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903) (opcional, solo abstract)

### 🗓️ Plan día a día (6h total)

**Lunes (1.5h):**
- Leer Prompt Engineering Guide - sections: Introduction, Few-shot, Chain-of-Thought
- Ver video 17min

**Martes (1.5h):**
- Ejercicio: Implementar 5 técnicas de prompting
  1. Zero-shot
  2. Few-shot (3 ejemplos)
  3. Chain of Thought
  4. Role-based
  5. Structured output (JSON)

**Miércoles (1.5h):**
- Proyecto: "Analizador de Código"
  - Input: código Python
  - Output: análisis estructurado (complejidad, mejoras, bugs potenciales)
  - Usa CoT y structured output

**Jueves (1h):**
- Experimentar con diferentes temperaturas y prompts
- Documentar qué funciona mejor para cada caso de uso

**Viernes (1.5h):**
- Crear "Prompt Library": colección de tus mejores prompts con ejemplos
- Formato: Markdown con categorías
- Subir a GitHub

### 💻 Ejercicio principal: Code Analyzer

```python
# code_analyzer.py
from openai import OpenAI
import os
import json
from pydantic import BaseModel
from typing import List

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class CodeAnalysis(BaseModel):
    complexity: str  # "low", "medium", "high"
    summary: str
    improvements: List[str]
    potential_bugs: List[str]

def analyze_code(code: str) -> CodeAnalysis:
    """Analiza código Python y devuelve análisis estructurado"""
    
    system_prompt = """Eres un ingeniero senior experto en Python.
Analiza código y proporciona feedback constructivo.
Responde SOLO con JSON válido."""

    user_prompt = f"""Analiza este código Python:

```python
{code}
```

Piensa paso a paso:
1. ¿Cuál es la complejidad (low/medium/high)?
2. ¿Qué hace el código?
3. ¿Qué mejoras sugerirías?
4. ¿Hay bugs potenciales?

Responde en formato JSON:
{{
  "complexity": "low|medium|high",
  "summary": "descripción breve",
  "improvements": ["mejora 1", "mejora 2"],
  "potential_bugs": ["bug 1", "bug 2"]
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3,
        response_format={"type": "json_object"}
    )
    
    analysis_json = json.loads(response.choices[0].message.content)
    return CodeAnalysis(**analysis_json)

# Ejemplo de uso
if __name__ == "__main__":
    code_to_analyze = """
def calculate(a, b):
    return a / b

result = calculate(10, 0)
print(result)
"""
    
    analysis = analyze_code(code_to_analyze)
    
    print(f"Complejidad: {analysis.complexity}")
    print(f"\nResumen: {analysis.summary}")
    print(f"\nMejoras:")
    for imp in analysis.improvements:
        print(f"  - {imp}")
    print(f"\nPotenciales bugs:")
    for bug in analysis.potential_bugs:
        print(f"  - {bug}")
```

**Prueba con diferentes códigos** y observa la calidad del análisis.

### ✅ Checklist
- [ ] Domino few-shot prompting
- [ ] Sé usar Chain of Thought
- [ ] Obtengo structured outputs consistentemente
- [ ] Code Analyzer funciona bien
- [ ] Tengo mi Prompt Library documentada
- [ ] Entiendo cuándo usar cada técnica

---

## Semana 6: Docker Basics
**18-24 Noviembre 2026**

### 🎯 Objetivo
Dominar Docker para empaquetar aplicaciones (necesario para deploy).

### 📖 Conceptos clave

**Docker:** Empaqueta tu app + dependencias en un "contenedor" que funciona igual en cualquier lugar.

**Imagen vs Contenedor:**
- Imagen: plantilla (como una clase)
- Contenedor: instancia corriendo (como un objeto)

**Dockerfile:** Receta para construir una imagen
```dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
```

**Docker Compose:** Define múltiples servicios (app + database)
```yaml
services:
  app:
    build: .
    ports:
      - "8000:8000"
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: secret
```

### 📚 Recursos

**Videos:**
- [Docker en 100 segundos](https://www.youtube.com/watch?v=Gjnup-PuquQ) (2min)
- [Docker tutorial completo - 1h](https://www.youtube.com/watch?v=3c-iBn73dDE) (1h)

**Docs:**
- [Docker Get Started](https://docs.docker.com/get-started/)
- [Docker Compose tutorial](https://docs.docker.com/compose/gettingstarted/)

**Cheatsheet:**
- [Docker Commands Cheatsheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf)

### 🗓️ Plan día a día (6h total)

**Lunes (1.5h):**
- Ver Docker 100 segundos
- Ver primera media hora del tutorial de 1h
- Instalar Docker Desktop (si no lo hiciste en setup)
- Verificar: `docker run hello-world`

**Martes (1.5h):**
- Continuar tutorial hasta min 60
- Ejercicio: Crear Dockerfile para una app Python simple
- Construir imagen y correr contenedor

**Miércoles (1.5h):**
- Leer Docker Compose docs
- Ejercicio: Dockerizar tu CRUD API de la semana 2
  - Dockerfile para la API
  - docker-compose.yml con app + postgres

**Jueves (1h):**
- Aprender Docker networking y volumes
- Ejercicio: Hacer que tu API se conecte a PostgreSQL en otro contenedor

**Viernes (1.5h):**
- Proyecto: FastAPI + PostgreSQL completamente dockerizado
- README con instrucciones para levantar todo con `docker-compose up`
- Subir a GitHub

### 💻 Ejercicio principal: Dockerizar API + PostgreSQL

**Estructura del proyecto:**
```
fastapi-docker/
├── app/
│   ├── __init__.py
│   └── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY ./app ./app

# Exponer puerto
EXPOSE 8000

# Comando de inicio
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: tasks_db
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user"]
      interval: 5s
      timeout: 5s
      retries: 5

  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://user:password@db:5432/tasks_db
    depends_on:
      db:
        condition: service_healthy
    volumes:
      - ./app:/app/app

volumes:
  postgres_data:
```

**requirements.txt:**
```
fastapi
uvicorn[standard]
psycopg2-binary
sqlalchemy
```

**app/main.py** (conexión a PostgreSQL):
```python
from fastapi import FastAPI
from sqlalchemy import create_engine
import os

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

@app.get("/")
def read_root():
    return {"status": "connected to database"}

@app.get("/health")
def health_check():
    try:
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        return {"status": "healthy"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}
```

**Ejecutar:**
```bash
docker-compose up --build
# Abre http://localhost:8000/health
```

**Comandos útiles:**
```bash
docker-compose up -d          # Levantar en background
docker-compose logs -f api    # Ver logs de la API
docker-compose down           # Parar y eliminar contenedores
docker-compose exec api bash  # Entrar al contenedor
```

### ✅ Checklist
- [ ] Entiendo qué es Docker y por qué se usa
- [ ] Sé escribir un Dockerfile
- [ ] Sé usar Docker Compose
- [ ] Mi API + PostgreSQL corren en Docker
- [ ] README con instrucciones claras
- [ ] Proyecto en GitHub

---

## Semana 7-8: Proyecto 1 - CLI AI Assistant
**25 Noviembre - 8 Diciembre 2026**

### 🎯 Objetivo
Construir tu primer proyecto AI end-to-end: un CLI que interactúa con OpenAI, con arquitectura limpia, tests, logging, y configuración profesional.

### 📋 Especificaciones del proyecto

**Nombre:** AI Assistant CLI

**Funcionalidad:**
- Usuario hace preguntas via línea de comandos
- El CLI llama a OpenAI API
- Devuelve respuesta estructurada (summary, key points, follow-up questions)
- Guarda historial de conversaciones
- Logging de todas las llamadas
- Configuración via .env
- Tests completos

**Stack:**
- Python 3.11+
- OpenAI SDK
- Pydantic (validación)
- Rich (CLI bonito)
- Pytest (tests)
- python-dotenv (config)

### 📚 Recursos adicionales

**Arquitectura de CLI:**
- [Building CLI apps with Python](https://www.youtube.com/watch?v=jfqGKbBWFwk) (20min)
- [Typer tutorial](https://typer.tiangolo.com/) (alternativa a argparse)

**Logging:**
- [Python Logging Tutorial](https://www.youtube.com/watch?v=jxmzY9soFXg) (15min)
- [Logging best practices](https://realpython.com/python-logging/)

### 🗓️ Plan por día (12h total en 2 semanas)

#### Semana 7

**Lunes (1.5h):**
- Diseñar arquitectura del proyecto
- Crear estructura de carpetas
- Setup inicial (poetry o pip, .env, .gitignore)

```
ai-assistant-cli/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── assistant.py
│   ├── config.py
│   └── models.py
├── tests/
│   ├── __init__.py
│   ├── test_assistant.py
│   └── test_models.py
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── pyproject.toml
```

**Martes (1.5h):**
- Implementar modelos Pydantic para request/response
- Implementar config.py (lectura de .env)

**Miércoles (1.5h):**
- Implementar assistant.py (lógica de llamada a OpenAI)
- Implementar structured output (summary + key points)

**Jueves (1.5h):**
- Implementar CLI con Rich
- Comandos: ask, chat (interactivo), history

**Viernes (1.5h):**
- Añadir logging (todas las llamadas, errores, costos)
- Implementar retry logic para llamadas fallidas

#### Semana 8

**Lunes (1.5h):**
- Implementar historial de conversaciones (guardar en JSON)
- Comando para ver historial: `python -m src.main history --last 5`

**Martes (1.5h):**
- Escribir tests para assistant.py (mock OpenAI API)
- Tests para modelos Pydantic

**Miércoles (1.5h):**
- Escribir tests de integración
- Configurar pytest con coverage

**Jueves (1h):**
- Escribir README completo con:
  - Descripción
  - Instalación
  - Uso
  - Ejemplos
  - Screenshots/GIFs

**Viernes (1.5h):**
- Refactoring y limpieza
- CI con GitHub Actions
- Subir a GitHub
- Crear release v1.0.0

### 💻 Código base

**src/models.py:**
```python
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class AssistantRequest(BaseModel):
    question: str
    context: Optional[str] = None

class AssistantResponse(BaseModel):
    summary: str
    key_points: List[str]
    follow_up_questions: List[str]
    tokens_used: int
    cost_usd: float

class ConversationEntry(BaseModel):
    timestamp: datetime
    question: str
    response: AssistantResponse
```

**src/config.py:**
```python
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    openai_api_key: str
    model: str = "gpt-4o-mini"
    temperature: float = 0.7
    max_tokens: int = 1000
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    return Settings()
```

**src/assistant.py:**
```python
from openai import OpenAI
import json
import logging
from .config import get_settings
from .models import AssistantRequest, AssistantResponse

logger = logging.getLogger(__name__)
settings = get_settings()
client = OpenAI(api_key=settings.openai_api_key)

def ask_assistant(request: AssistantRequest) -> AssistantResponse:
    """Procesa pregunta y devuelve respuesta estructurada"""
    
    system_prompt = """Eres un asistente AI útil y conciso.
Para cada pregunta, proporciona:
1. Un summary (2-3 frases)
2. Key points (3-5 bullets)
3. Follow-up questions (2-3 preguntas relacionadas)

Responde en formato JSON."""

    user_prompt = f"""Pregunta: {request.question}

Responde en JSON:
{{
  "summary": "...",
  "key_points": ["...", "..."],
  "follow_up_questions": ["...", "..."]
}}"""

    try:
        logger.info(f"Enviando pregunta: {request.question}")
        
        response = client.chat.completions.create(
            model=settings.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=settings.temperature,
            max_tokens=settings.max_tokens,
            response_format={"type": "json_object"}
        )
        
        # Parsear respuesta
        content = json.loads(response.choices[0].message.content)
        
        # Calcular costo (aproximado)
        tokens_used = response.usage.total_tokens
        cost_usd = tokens_used * 0.00002  # precio aproximado
        
        logger.info(f"Respuesta recibida. Tokens: {tokens_used}, Costo: ${cost_usd:.4f}")
        
        return AssistantResponse(
            summary=content["summary"],
            key_points=content["key_points"],
            follow_up_questions=content["follow_up_questions"],
            tokens_used=tokens_used,
            cost_usd=cost_usd
        )
        
    except Exception as e:
        logger.error(f"Error al procesar pregunta: {e}")
        raise
```

**src/main.py:**
```python
import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from .assistant import ask_assistant
from .models import AssistantRequest
import logging

app = typer.Typer()
console = Console()

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('assistant.log'),
        logging.StreamHandler()
    ]
)

@app.command()
def ask(question: str):
    """Hacer una pregunta al asistente"""
    try:
        request = AssistantRequest(question=question)
        response = ask_assistant(request)
        
        # Mostrar respuesta bonita
        console.print(Panel(response.summary, title="Summary", border_style="green"))
        
        console.print("\n[bold]Key Points:[/bold]")
        for point in response.key_points:
            console.print(f"  • {point}")
        
        console.print("\n[bold]Follow-up Questions:[/bold]")
        for q in response.follow_up_questions:
            console.print(f"  ? {q}")
        
        console.print(f"\n[dim]Tokens: {response.tokens_used} | Cost: ${response.cost_usd:.4f}[/dim]")
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@app.command()
def chat():
    """Modo interactivo"""
    console.print("[bold green]AI Assistant - Modo Chat[/bold green]")
    console.print("Escribe 'exit' para salir\n")
    
    while True:
        question = console.input("[bold blue]Tú:[/bold blue] ")
        if question.lower() == "exit":
            break
        
        ask(question)
        console.print()

if __name__ == "__main__":
    app()
```

**tests/test_assistant.py:**
```python
import pytest
from unittest.mock import Mock, patch
from src.assistant import ask_assistant
from src.models import AssistantRequest

@patch('src.assistant.client')
def test_ask_assistant(mock_client):
    """Test que ask_assistant procesa correctamente"""
    
    # Mock de la respuesta de OpenAI
    mock_response = Mock()
    mock_response.choices[0].message.content = '''
    {
        "summary": "Test summary",
        "key_points": ["Point 1", "Point 2"],
        "follow_up_questions": ["Question 1?"]
    }
    '''
    mock_response.usage.total_tokens = 100
    mock_client.chat.completions.create.return_value = mock_response
    
    # Ejecutar
    request = AssistantRequest(question="Test question")
    response = ask_assistant(request)
    
    # Verificar
    assert response.summary == "Test summary"
    assert len(response.key_points) == 2
    assert len(response.follow_up_questions) == 1
    assert response.tokens_used == 100
```

**Uso:**
```bash
# Instalar
pip install -r requirements.txt

# Configurar
cp .env.example .env
# Editar .env con tu API key

# Usar
python -m src.main ask "¿Qué es machine learning?"
python -m src.main chat

# Tests
pytest tests/ -v --cov=src
```

### ✅ Checklist del proyecto
- [ ] Arquitectura modular (config, models, assistant, main separados)
- [ ] Structured outputs (summary, key points, follow-ups)
- [ ] Logging completo (llamadas, errores, costos)
- [ ] Configuración via .env
- [ ] CLI con Rich (output bonito)
- [ ] Tests con >80% coverage
- [ ] README completo con ejemplos
- [ ] GitHub Actions (CI)
- [ ] Código limpio y documentado
- [ ] Subido a GitHub con release

**Este es tu primer proyecto AI real para el portfolio.** Dedícale tiempo a hacerlo bien.

---

## Semana 9: SQL + PostgreSQL Avanzado
**9-15 Diciembre 2026**

### 🎯 Objetivo
Dominar SQL y PostgreSQL para trabajar con datos (necesario para RAG).

### 📖 Conceptos clave

**SQL:** Lenguaje para interactuar con bases de datos relacionales.

**PostgreSQL:** Base de datos open-source muy potente. Soporta extensiones (como pgvector).

**CRUD en SQL:**
```sql
-- Create
INSERT INTO users (name, email) VALUES ('Marco', 'marco@example.com');

-- Read
SELECT * FROM users WHERE email LIKE '%@example.com';

-- Update
UPDATE users SET name = 'Marco Lopez' WHERE id = 1;

-- Delete
DELETE FROM users WHERE id = 1;
```

**Joins:** Combinar datos de múltiples tablas.
```sql
-- INNER JOIN: solo registros que matchean
SELECT orders.id, users.name
FROM orders
INNER JOIN users ON orders.user_id = users.id;

-- LEFT JOIN: todos los de la izquierda + matches
SELECT users.name, orders.id
FROM users
LEFT JOIN orders ON users.id = orders.user_id;
```

**Índices:** Aceleran búsquedas.
```sql
CREATE INDEX idx_email ON users(email);
```

**Transacciones:** Operaciones atómicas.
```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### 📚 Recursos

**Videos:**
- [SQL en 60 min - freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY) (1h)
- [PostgreSQL Tutorial](https://www.youtube.com/watch?v=qw--VYLpxG4) (1h)

**Interactivo:**
- [SQLBolt](https://sqlbolt.com/) - ejercicios interactivos ⭐
- [PostgreSQL Exercises](https://pgexercises.com/)

**Docs:**
- [PostgreSQL Tutorial oficial](https://www.postgresql.org/docs/current/tutorial.html)

### 🗓️ Plan día a día (6h total)

**Lunes (1.5h):**
- Ver SQL en 60min (hasta min 30)
- Completar SQLBolt lecciones 1-6

**Martes (1.5h):**
- Continuar SQL video (min 30-60)
- Completar SQLBolt lecciones 7-12

**Miércoles (1.5h):**
- Instalar PostgreSQL localmente o con Docker
- Conectar con psql o DBeaver
- Crear tu primera database y tablas

**Jueves (1h):**
- Hacer ejercicios de PostgreSQL Exercises (joins, aggregates)
- Experimentar con índices y performance

**Viernes (1.5h):**
- Proyecto: Database schema para una app de blog
  - Tablas: users, posts, comments, tags
  - Relaciones con foreign keys
  - Queries complejas con joins
  - Scripts de seed data

### 💻 Ejercicio principal: Blog Database

```sql
-- schema.sql

-- Tabla de usuarios
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de posts
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    published BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de comentarios
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    post_id INTEGER REFERENCES posts(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de tags
CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- Tabla intermedia (many-to-many)
CREATE TABLE post_tags (
    post_id INTEGER REFERENCES posts(id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (post_id, tag_id)
);

-- Índices para performance
CREATE INDEX idx_posts_user_id ON posts(user_id);
CREATE INDEX idx_comments_post_id ON comments(post_id);
CREATE INDEX idx_posts_published ON posts(published);

-- seed.sql

-- Insertar usuarios
INSERT INTO users (username, email) VALUES
    ('marco', 'marco@example.com'),
    ('ana', 'ana@example.com'),
    ('luis', 'luis@example.com');

-- Insertar posts
INSERT INTO posts (user_id, title, content, published) VALUES
    (1, 'Mi primer post', 'Contenido del post...', true),
    (1, 'Aprendiendo SQL', 'SQL es muy útil...', true),
    (2, 'PostgreSQL avanzado', 'Hoy aprendí sobre...', true);

-- Insertar tags
INSERT INTO tags (name) VALUES ('python'), ('sql'), ('tutorial');

-- Relacionar posts con tags
INSERT INTO post_tags (post_id, tag_id) VALUES
    (1, 3),
    (2, 2),
    (2, 3),
    (3, 2);

-- Insertar comentarios
INSERT INTO comments (post_id, user_id, content) VALUES
    (1, 2, 'Buen post!'),
    (1, 3, 'Muy útil, gracias'),
    (2, 3, 'Excelente explicación');
```

**Queries interesantes:**

```sql
-- 1. Posts de un usuario con conteo de comentarios
SELECT 
    p.id,
    p.title,
    u.username,
    COUNT(c.id) as comment_count
FROM posts p
JOIN users u ON p.user_id = u.id
LEFT JOIN comments c ON p.id = c.post_id
WHERE u.username = 'marco'
GROUP BY p.id, p.title, u.username;

-- 2. Posts con sus tags
SELECT 
    p.title,
    ARRAY_AGG(t.name) as tags
FROM posts p
LEFT JOIN post_tags pt ON p.id = pt.post_id
LEFT JOIN tags t ON pt.tag_id = t.id
GROUP BY p.id, p.title;

-- 3. Usuarios más activos (por posts + comentarios)
SELECT 
    u.username,
    COUNT(DISTINCT p.id) as posts_count,
    COUNT(DISTINCT c.id) as comments_count,
    COUNT(DISTINCT p.id) + COUNT(DISTINCT c.id) as total_activity
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
LEFT JOIN comments c ON u.id = c.user_id
GROUP BY u.id, u.username
ORDER BY total_activity DESC;

-- 4. Posts sin comentarios
SELECT p.title
FROM posts p
LEFT JOIN comments c ON p.id = c.post_id
WHERE c.id IS NULL;
```

**Script Python para conectar:**

```python
import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="blog_db",
        user="postgres",
        password="password"
    )

def get_user_posts(username: str):
    """Obtiene posts de un usuario con conteo de comentarios"""
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                SELECT 
                    p.id,
                    p.title,
                    p.content,
                    COUNT(c.id) as comment_count
                FROM posts p
                JOIN users u ON p.user_id = u.id
                LEFT JOIN comments c ON p.id = c.post_id
                WHERE u.username = %s
                GROUP BY p.id, p.title, p.content
            """, (username,))
            return cur.fetchall()
    finally:
        conn.close()

# Uso
posts = get_user_posts('marco')
for post in posts:
    print(f"{post['title']}: {post['comment_count']} comentarios")
```

### ✅ Checklist
- [ ] Domino SELECT, INSERT, UPDATE, DELETE
- [ ] Entiendo JOINs (INNER, LEFT, RIGHT)
- [ ] Sé usar GROUP BY y agregaciones
- [ ] He completado SQLBolt
- [ ] Blog database schema creado y funcional
- [ ] Puedo conectar PostgreSQL desde Python
- [ ] Código en GitHub

---

## Semana 10: SQLAlchemy ORM
**16-22 Diciembre 2026**

### 🎯 Objetivo
Usar SQLAlchemy para interactuar con PostgreSQL desde Python (no más SQL crudo).

### 📖 Conceptos clave

**ORM (Object-Relational Mapping):** Mapea tablas SQL a clases Python.

```python
# En vez de SQL:
cursor.execute("SELECT * FROM users WHERE email = %s", (email,))

# Usas Python:
session.query(User).filter(User.email == email).first()
```

**SQLAlchemy:** ORM más popular de Python.

**Models:** Clases que representan tablas.
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
```

**Session:** Objeto para hacer queries.
```python
from sqlalchemy.orm import Session

with Session(engine) as session:
    user = session.query(User).filter_by(username='marco').first()
    print(user.email)
```

**Relationships:** Relaciones entre tablas.
```python
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    posts = relationship("Post", back_populates="user")

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="posts")

# Ahora puedes hacer:
user = session.query(User).first()
for post in user.posts:
    print(post.title)
```

### 📚 Recursos

**Videos:**
- [SQLAlchemy Tutorial - Tech With Tim](https://www.youtube.com/watch?v=AKQ3XEDI9Mw) (30min)
- [SQLAlchemy ORM - ArjanCodes](https://www.youtube.com/watch?v=AKQ3XEDI9Mw) (20min)

**Docs:**
- [SQLAlchemy Tutorial oficial](https://docs.sqlalchemy.org/en/20/tutorial/)
- [FastAPI with Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/)

**Repos:**
- https://github.com/tiangolo/full-stack-fastapi-postgresql (mira models.py)

### 🗓️ Plan día a día (6h total)

**Lunes (1.5h):**
- Ver video SQLAlchemy Tutorial (30min)
- Leer SQLAlchemy Quickstart
- Instalar: `pip install sqlalchemy psycopg2-binary`

**Martes (1.5h):**
- Ejercicio: Convertir blog schema de semana pasada a SQLAlchemy models
- Crear engine y session

**Miércoles (1.5h):**
- Implementar CRUD operations con SQLAlchemy
- Create, Read, Update, Delete para User y Post

**Jueves (1h):**
- Aprender sobre relationships (one-to-many, many-to-many)
- Implementar relationships en blog models

**Viernes (1.5h):**
- Integrar SQLAlchemy con FastAPI
- Crear API endpoints que usen SQLAlchemy
- Dependency injection para session

### 💻 Ejercicio principal: FastAPI + SQLAlchemy Blog API

**Estructura:**
```
fastapi-sqlalchemy-blog/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
├── requirements.txt
└── README.md
```

**app/database.py:**
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/blog_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Dependency para FastAPI"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

**app/models.py:**
```python
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    posts = relationship("Post", back_populates="author", cascade="all, delete-orphan")
    comments = relationship("Comment", back_populates="author", cascade="all, delete-orphan")

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    published = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    post = relationship("Post", back_populates="comments")
    author = relationship("User", back_populates="comments")
```

**app/schemas.py** (Pydantic para API):
```python
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = False

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    user_id: int
    created_at: datetime
    author: User
    
    class Config:
        from_attributes = True

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    post_id: int

class Comment(CommentBase):
    id: int
    post_id: int
    user_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
```

**app/crud.py:**
```python
from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_post(db: Session, post: schemas.PostCreate, user_id: int):
    db_post = models.Post(**post.dict(), user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()

def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()
```

**app/main.py:**
```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, crud
from .database import engine, get_db

# Crear tablas
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog API")

@app.post("/users/", response_model=schemas.User, status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users/{user_id}/posts/", response_model=schemas.Post, status_code=201)
def create_post(user_id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_post(db=db, post=post, user_id=user_id)

@app.get("/posts/", response_model=List[schemas.Post])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, skip=skip, limit=limit)
    return posts

@app.get("/posts/{post_id}", response_model=schemas.Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post(db, post_id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
```

**Ejecutar:**
```bash
pip install fastapi sqlalchemy psycopg2-binary uvicorn

uvicorn app.main:app --reload
# Abrir http://localhost:8000/docs
```

### ✅ Checklist
- [ ] Entiendo qué es un ORM y por qué se usa
- [ ] Sé definir models con SQLAlchemy
- [ ] Sé hacer queries con Session
- [ ] Entiendo relationships (one-to-many, many-to-many)
- [ ] He integrado SQLAlchemy con FastAPI
- [ ] Blog API funciona completamente
- [ ] Código en GitHub

---

## Semana 11: Embeddings + Vector Similarity
**23-29 Diciembre 2026**

### 🎯 Objetivo
Entender embeddings (representaciones vectoriales de texto) y búsqueda por similitud (base de RAG).

### 📖 Conceptos clave

**Embedding:** Representación numérica de texto en un espacio vectorial.

```python
"perro" → [0.2, 0.8, 0.3, ..., 0.5]  # 1536 dimensiones
"gato"  → [0.3, 0.7, 0.4, ..., 0.4]  # similar a perro
"coche" → [0.9, 0.1, 0.8, ..., 0.2]  # diferente
```

**Por qué importan:** Permiten búsqueda semántica.
- Búsqueda tradicional: keywords exactas
- Búsqueda semántica: significado similar

```python
Query: "¿Cómo cocinar pasta?"
Documentos:
1. "Receta de spaghetti" ← MATCH (aunque no dice "pasta")
2. "Historia de Italia"  ← NO MATCH
```

**Cosine similarity:** Mide qué tan similares son 2 vectors.
```python
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

vec1 = np.array([[0.2, 0.8, 0.3]])
vec2 = np.array([[0.3, 0.7, 0.4]])

similarity = cosine_similarity(vec1, vec2)[0][0]
print(similarity)  # ~0.99 (muy similar)
```

**OpenAI Embeddings API:**
```python
from openai import OpenAI
client = OpenAI()

response = client.embeddings.create(
    model="text-embedding-3-small",
    input="Texto para convertir a vector"
)

embedding = response.data[0].embedding  # lista de 1536 números
```

### 📚 Recursos

**Videos:**
- [¿Qué son los embeddings? - Visual explanation](https://www.youtube.com/watch?v=wjZofJX0v4M) (10min)
- [Vector embeddings explained](https://www.youtube.com/watch?v=5MaWmXwxFNQ) (15min)
- [Semantic Search Tutorial](https://www.youtube.com/watch?v=OATCgQtNX2o) (20min)

**Artículos:**
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
- [Understanding Vector Embeddings](https://www.pinecone.io/learn/vector-embeddings/)

**Notebooks interactivos:**
- [OpenAI Cookbook - Embeddings](https://github.com/openai/openai-cookbook/blob/main/examples/Embedding_Wikipedia_articles_for_search.ipynb)

### 🗓️ Plan día a día (6h total)

**Lunes (1.5h):**
- Ver videos sobre embeddings
- Leer OpenAI Embeddings Guide
- Entender el concepto intuitivamente

**Martes (1.5h):**
- Generar tus primeros embeddings con OpenAI API
- Ejercicio: Embed 10 frases y visualizar similitudes

**Miércoles (1.5h):**
- Implementar búsqueda semántica básica
- Ejercicio: "Mini search engine" en memoria

**Jueves (1h):**
- Experimentar con diferentes textos
- Comparar embeddings de sinónimos, antónimos, etc.

**Viernes (1.5h):**
- Proyecto: Buscador semántico de películas
- Dataset: 50 descripciones de películas
- Query: "película de acción con explosiones"
- Devuelve top 5 matches

### 💻 Ejercicio principal: Semantic Movie Search

```python
# semantic_search.py
from openai import OpenAI
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Dataset de películas
MOVIES = [
    {"title": "Die Hard", "description": "Un policía lucha contra terroristas en un rascacielos"},
    {"title": "The Notebook", "description": "Una historia de amor que trasciende el tiempo"},
    {"title": "Inception", "description": "Ladrones que roban secretos dentro de sueños"},
    {"title": "Mad Max", "description": "Acción post-apocalíptica en un desierto"},
    {"title": "Titanic", "description": "Romance trágico en un barco que se hunde"},
    {"title": "The Matrix", "description": "Hacker descubre que vive en una simulación"},
    {"title": "Fast & Furious", "description": "Carreras de coches y muchas explosiones"},
    {"title": "Pride & Prejudice", "description": "Romance clásico en la Inglaterra del siglo XIX"},
    {"title": "Interstellar", "description": "Viaje espacial para salvar a la humanidad"},
    {"title": "John Wick", "description": "Asesino busca venganza con mucha acción"},
]

def get_embedding(text: str) -> list[float]:
    """Obtiene embedding de un texto"""
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def embed_movies(movies: list[dict]) -> list[dict]:
    """Genera embeddings para todas las películas"""
    print("Generando embeddings...")
    for movie in movies:
        movie['embedding'] = get_embedding(movie['description'])
    return movies

def search(query: str, movies: list[dict], top_k: int = 5) -> list[dict]:
    """Busca películas similares a la query"""
    # Embed query
    query_embedding = get_embedding(query)
    
    # Calcular similitudes
    query_vec = np.array([query_embedding])
    
    for movie in movies:
        movie_vec = np.array([movie['embedding']])
        similarity = cosine_similarity(query_vec, movie_vec)[0][0]
        movie['similarity'] = similarity
    
    # Ordenar por similitud
    movies.sort(key=lambda x: x['similarity'], reverse=True)
    
    return movies[:top_k]

def main():
    # Generar embeddings (solo una vez)
    movies = embed_movies(MOVIES)
    
    print("\n=== Semantic Movie Search ===\n")
    
    while True:
        query = input("Búsqueda (o 'exit' para salir): ")
        if query.lower() == 'exit':
            break
        
        results = search(query, movies, top_k=3)
        
        print(f"\nResultados para: '{query}'\n")
        for i, movie in enumerate(results, 1):
            print(f"{i}. {movie['title']}")
            print(f"   {movie['description']}")
            print(f"   Similitud: {movie['similarity']:.3f}\n")

if __name__ == "__main__":
    main()
```

**Pruebas interesantes:**
```python
# Queries a probar:
"película de acción con explosiones"
# → Die Hard, Fast & Furious, Mad Max

"historia de amor romántica"
# → The Notebook, Titanic, Pride & Prejudice

"ciencia ficción y tecnología"
# → The Matrix, Inception, Interstellar

"venganza y violencia"
# → John Wick, Mad Max, Die Hard
```

**Observaciones:**
- Aunque "explosiones" no aparece en ninguna descripción, encuentra las correctas
- Entiende sinónimos: "amor" vs "romance"
- Agrupa por temática aunque las palabras sean diferentes

### 💻 Ejercicio extra: Visualizar embeddings

```python
# visualize_embeddings.py
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

def visualize_embeddings(movies: list[dict]):
    """Visualiza embeddings en 2D usando PCA"""
    
    # Extraer embeddings
    embeddings = np.array([m['embedding'] for m in movies])
    
    # Reducir de 1536 dimensiones a 2
    pca = PCA(n_components=2)
    embeddings_2d = pca.fit_transform(embeddings)
    
    # Plot
    plt.figure(figsize=(12, 8))
    plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], s=100)
    
    for i, movie in enumerate(movies):
        plt.annotate(
            movie['title'],
            (embeddings_2d[i, 0], embeddings_2d[i, 1]),
            fontsize=9
        )
    
    plt.title("Movie Embeddings en 2D")
    plt.xlabel("Componente 1")
    plt.ylabel("Componente 2")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("embeddings_visualization.png")
    plt.show()

# Usar después de embed_movies()
visualize_embeddings(movies)
```

Verás que películas similares están más cerca en el espacio.

### ✅ Checklist
- [ ] Entiendo qué son embeddings conceptualmente
- [ ] Sé generar embeddings con OpenAI API
- [ ] Entiendo cosine similarity
- [ ] He implementado búsqueda semántica
- [ ] Movie search funciona correctamente
- [ ] Puedo explicar por qué RAG necesita embeddings
- [ ] Código en GitHub

---

## Semana 12: Recap Fase 1 + Mini Proyecto
**30 Diciembre 2026 - 5 Enero 2027**

### 🎯 Objetivo
Consolidar todo lo aprendido en Fase 1 y construir un mini proyecto integrando todo.

### 📋 Checklist de Fase 1

Antes de continuar a Fase 2, verifica que dominas:

**Python Moderno:**
- [ ] Async/await
- [ ] Type hints
- [ ] Pydantic models
- [ ] Context managers
- [ ] Decorators

**APIs y Backend:**
- [ ] FastAPI (routing, dependency injection)
- [ ] Request/Response models
- [ ] Error handling
- [ ] Testing con TestClient
- [ ] Documentación automática

**LLMs:**
- [ ] OpenAI API
- [ ] System vs User prompts
- [ ] Temperature y parámetros
- [ ] Structured outputs
- [ ] Prompt engineering basics

**Databases:**
- [ ] SQL (CRUD, joins, indices)
- [ ] PostgreSQL
- [ ] SQLAlchemy ORM
- [ ] Relationships

**Embeddings:**
- [ ] Qué son y para qué sirven
- [ ] Generar con OpenAI
- [ ] Cosine similarity
- [ ] Búsqueda semántica

**DevOps Básico:**
- [ ] Docker (Dockerfile, compose)
- [ ] Git (branches, PRs)
- [ ] Testing (pytest)
- [ ] Logging
- [ ] CI/CD básico

### 🗓️ Plan de la semana (6h)

**Día 1-2 (2h):**
- Revisar tus 11 semanas de código
- Identificar puntos débiles
- Repasar conceptos que no tengas 100% claros

**Día 3-5 (4h):**
- Mini proyecto integrador: "Smart Notes"
  - API FastAPI
  - CRUD de notas en PostgreSQL
  - Búsqueda semántica de notas
  - Sugerencias generadas por LLM
  - Dockerizado

### 💻 Proyecto: Smart Notes API

**Funcionalidad:**
1. Crear/editar/borrar notas
2. Buscar notas por similitud semántica
3. Generar resumen automático de una nota
4. Sugerir notas relacionadas

**Stack:**
- FastAPI
- SQLAlchemy + PostgreSQL
- OpenAI (embeddings + chat)
- Docker

**Estructura:**
```
smart-notes/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── ai.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

**app/models.py:**
```python
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql import func
from .database import Base

class Note(Base):
    __tablename__ = "notes"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    embedding = Column(ARRAY(Float))  # vector de 1536 dimensiones
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
```

**app/ai.py:**
```python
from openai import OpenAI
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_embedding(text: str) -> list[float]:
    """Genera embedding de un texto"""
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def summarize_note(content: str) -> str:
    """Genera resumen de una nota"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Resume el siguiente texto en 2-3 frases."},
            {"role": "user", "content": content}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content

def find_similar_notes(query_embedding: list[float], notes: list) -> list:
    """Encuentra notas similares por embedding"""
    query_vec = np.array([query_embedding])
    
    for note in notes:
        if note.embedding:
            note_vec = np.array([note.embedding])
            similarity = cosine_similarity(query_vec, note_vec)[0][0]
            note.similarity = similarity
        else:
            note.similarity = 0.0
    
    notes.sort(key=lambda x: x.similarity, reverse=True)
    return notes[:5]
```

**app/main.py:**
```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, crud, ai
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Notes API")

@app.post("/notes/", response_model=schemas.Note, status_code=201)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    # Generar embedding
    embedding = ai.get_embedding(f"{note.title} {note.content}")
    return crud.create_note(db, note, embedding)

@app.get("/notes/", response_model=List[schemas.Note])
def get_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_notes(db, skip=skip, limit=limit)

@app.get("/notes/{note_id}", response_model=schemas.Note)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = crud.get_note(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@app.post("/notes/search", response_model=List[schemas.NoteWithSimilarity])
def search_notes(query: str, db: Session = Depends(get_db)):
    """Búsqueda semántica"""
    query_embedding = ai.get_embedding(query)
    all_notes = crud.get_notes(db)
    similar_notes = ai.find_similar_notes(query_embedding, all_notes)
    return similar_notes

@app.get("/notes/{note_id}/summary")
def get_summary(note_id: int, db: Session = Depends(get_db)):
    """Genera resumen de una nota"""
    note = crud.get_note(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    summary = ai.summarize_note(note.content)
    return {"summary": summary}

@app.get("/notes/{note_id}/related", response_model=List[schemas.Note])
def get_related_notes(note_id: int, db: Session = Depends(get_db)):
    """Encuentra notas relacionadas"""
    note = crud.get_note(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    all_notes = [n for n in crud.get_notes(db) if n.id != note_id]
    similar = ai.find_similar_notes(note.embedding, all_notes)
    return similar[:3]
```

**Funcionalidades implementadas:**
✅ CRUD de notas
✅ Embeddings automáticos al crear
✅ Búsqueda semántica
✅ Resumen automático por LLM
✅ Sugerencias de notas relacionadas

**Para ejecutar:**
```bash
docker-compose up --build
# Probar en http://localhost:8000/docs
```

### ✅ Checklist Final de Fase 1
- [ ] Proyecto CLI AI Assistant completado
- [ ] Smart Notes API funcionando
- [ ] Todos los conceptos de Fase 1 dominados
- [ ] Portfolio con 2 proyectos públicos en GitHub
- [ ] Entiendo el panorama general de AI Engineer
- [ ] Listo para Fase 2 (RAG completo)

---

# FASE 2: BACKEND + RAG
## Enero - Marzo 2027 (12 semanas)

### Objetivo de la fase
Construir sistemas RAG completos: chunking, embeddings, vector databases, retrieval avanzado, y deployment con FastAPI + PostgreSQL + pgvector.

**Proyecto final:** Docs Q&A Platform (upload PDFs, chat sobre ellos)

---

## Semana 13: Vector Databases - pgvector
**6-12 Enero 2027**

### 🎯 Objetivo
Aprender a usar pgvector para búsqueda vectorial eficiente en PostgreSQL (mejor que NumPy para escala).

### 📖 Conceptos clave

**Vector Database:** Base de datos optimizada para búsqueda por similitud de vectores.

**Por qué no usar NumPy:**
- NumPy: carga todos los embeddings en RAM → no escala
- Vector DB: índices optimizados para búsqueda rápida en millones de vectores

**pgvector:** Extensión de PostgreSQL para vectores.
```sql
CREATE EXTENSION vector;

CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    content TEXT,
    embedding VECTOR(1536)
);

-- Búsqueda por similitud
SELECT content FROM documents
ORDER BY embedding <-> '[0.1, 0.2, ...]'::vector
LIMIT 5;
```

**Operadores de similitud:**
- `<->` : L2 distance (Euclidean)
- `<=>` : Cosine distance
- `<#>` : Inner product

**Índices:** Aceleran búsqueda (necesario para >10K vectores)
```sql
CREATE INDEX ON documents USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100);
```

### 📚 Recursos

**Docs:**
- [pgvector GitHub](https://github.com/pgvector/pgvector)
- [pgvector Python Guide](https://github.com/pgvector/pgvector-python)

**Videos:**
- [Vector Databases explained](https://www.youtube.com/watch?v=dN0lsF2cvm4) (15min)
- [pgvector tutorial](https://www.youtube.com/watch?v=SQ0NW9CdxLY) (20min)

**Artículos:**
- [Why Vector Databases](https://www.pinecone.io/learn/vector-database/)
- [pgvector vs Pinecone vs Weaviate](https://superlinked.com/vector-db-comparison/)

### 🗓️ Plan día a día (6h total)

**Lunes (1.5h):**
- Ver videos sobre vector databases
- Leer pgvector docs
- Entender cuándo usar vector DB vs NumPy

**Martes (1.5h):**
- Instalar pgvector en PostgreSQL local
```bash
docker run -d \
  --name postgres-pgvector \
  -e POSTGRES_PASSWORD=password \
  -p 5432:5432 \
  ankane/pgvector
```
- Conectar y activar extensión
- Crear primera tabla con columna VECTOR

**Miércoles (1.5h):**
- Ejercicio: Migrar Movie Search (semana 11) a pgvector
- Insertar películas con embeddings en PostgreSQL
- Queries de similitud

**Jueves (1h):**
- Aprender sobre índices (ivfflat, hnsw)
- Benchmark: query sin índice vs con índice
- Experimentar con diferentes configuraciones

**Viernes (1.5h):**
- Proyecto: Knowledge Base API
  - Tabla de artículos con embeddings
  - Endpoint para agregar artículos
  - Endpoint de búsqueda semántica
  - Usar pgvector

### 💻 Ejercicio principal: Knowledge Base con pgvector

```python
# app/database.py
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pgvector.sqlalchemy import Vector

DATABASE_URL = "postgresql://postgres:password@localhost/knowledge_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Activar pgvector
with engine.connect() as conn:
    conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
    conn.commit()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

```python
# app/models.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from pgvector.sqlalchemy import Vector
from .database import Base

class Article(Base):
    __tablename__ = "articles"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)
    content = Column(Text, nullable=False)
    embedding = Column(Vector(1536))  # pgvector column
    created_at = Column(DateTime(timezone=True), server_default=func.now())
```

```python
# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
from openai import OpenAI
import os

from . import models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Knowledge Base API")
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_embedding(text: str) -> list[float]:
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

@app.post("/articles/", status_code=201)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    # Generar embedding
    text = f"{article.title}\n{article.content}"
    embedding = get_embedding(text)
    
    # Crear artículo
    db_article = models.Article(
        title=article.title,
        content=article.content,
        embedding=embedding
    )
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    
    return db_article

@app.get("/articles/search")
def search_articles(query: str, limit: int = 5, db: Session = Depends(get_db)):
    # Generar embedding de query
    query_embedding = get_embedding(query)
    
    # Búsqueda con pgvector (cosine similarity)
    results = db.execute(
        text("""
            SELECT 
                id, 
                title, 
                content,
                1 - (embedding <=> :embedding) as similarity
            FROM articles
            ORDER BY embedding <=> :embedding
            LIMIT :limit
        """),
        {"embedding": str(query_embedding), "limit": limit}
    ).fetchall()
    
    return [
        {
            "id": r[0],
            "title": r[1],
            "content": r[2],
            "similarity": float(r[3])
        }
        for r in results
    ]

@app.post("/articles/create-index")
def create_index(db: Session = Depends(get_db)):
    """Crea índice ivfflat para acelerar búsquedas"""
    try:
        db.execute(text("""
            CREATE INDEX IF NOT EXISTS articles_embedding_idx 
            ON articles USING ivfflat (embedding vector_cosine_ops)
            WITH (lists = 100)
        """))
        db.commit()
        return {"message": "Index created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

**Prueba con datos:**

```python
# seed_data.py
import requests

ARTICLES = [
    {
        "title": "Introducción a Python",
        "content": "Python es un lenguaje de programación interpretado de alto nivel..."
    },
    {
        "title": "FastAPI Tutorial",
        "content": "FastAPI es un framework moderno para construir APIs con Python..."
    },
    {
        "title": "Machine Learning Basics",
        "content": "El machine learning es una rama de la IA que permite a las máquinas aprender..."
    },
    {
        "title": "SQL for Data Science",
        "content": "SQL es esencial para manipular y consultar bases de datos relacionales..."
    },
    {
        "title": "Docker Essentials",
        "content": "Docker permite empaquetar aplicaciones en contenedores portables..."
    }
]

for article in ARTICLES:
    response = requests.post("http://localhost:8000/articles/", json=article)
    print(f"Created: {response.json()['title']}")

# Crear índice
requests.post("http://localhost:8000/articles/create-index")

# Buscar
query = "cómo construir APIs web"
response = requests.get("http://localhost:8000/articles/search", params={"query": query})
print(f"\nResults for: '{query}'")
for result in response.json():
    print(f"- {result['title']} (similarity: {result['similarity']:.3f})")
```

**Benchmark de índices:**

```python
# benchmark.py
import time
from sqlalchemy import text

def benchmark_search(db, query_embedding, with_index=True):
    """Mide tiempo de búsqueda"""
    
    if not with_index:
        # Drop index
        db.execute(text("DROP INDEX IF EXISTS articles_embedding_idx"))
    
    start = time.time()
    
    db.execute(
        text("""
            SELECT id, title
            FROM articles
            ORDER BY embedding <=> :embedding
            LIMIT 10
        """),
        {"embedding": str(query_embedding)}
    ).fetchall()
    
    end = time.time()
    
    return (end - start) * 1000  # ms

# Insertar 10K artículos primero
# Sin índice: ~800ms
# Con índice: ~15ms (53x más rápido)
```

### ✅ Checklist
- [ ] Entiendo qué es una vector database
- [ ] Sé cuándo usar pgvector vs otras opciones
- [ ] pgvector instalado y funcionando
- [ ] Domino los operadores de similitud
- [ ] Knowledge Base API funciona
- [ ] Entiendo índices ivfflat/hnsw
- [ ] Código en GitHub

---

## Semana 14: Document Processing - Chunking
**13-19 Enero 2027**

### 🎯 Objetivo
Aprender a procesar documentos (PDFs, Markdown, txt) y dividirlos en chunks para RAG.

### 📖 Conceptos clave

**Chunking:** Dividir documentos largos en pedazos (chunks) manejables.

**¿Por qué chunking?**
- LLMs tienen context window limitado (ej. 128K tokens ≈ 300 páginas)
- Búsqueda semántica más precisa con chunks pequeños
- Cada chunk se convierte en un embedding

**Estrategias de chunking:**

1. **Fixed-size:** Tamaño fijo (ej. 500 caracteres)
   ```python
   chunks = [text[i:i+500] for i in range(0, len(text), 500)]
   ```
   - ✅ Simple
   - ❌ Puede cortar en medio de una oración

2. **Semantic:** Por párrafos/secciones
   ```python
   chunks = text.split('\n\n')
   ```
   - ✅ Respeta estructura
   - ❌ Chunks de tamaño variable

3. **Recursive:** Intenta por delimitadores (párrafos → frases → palabras)
   - ✅ Balance entre tamaño y semántica
   - ✅ Es la más usada (LangChain lo hace así)

**Overlap:** Superponer chunks para no perder contexto
```python
chunk1: "...machine learning is..."
chunk2: "...learning is a branch..."
         ^^^^^^^^^ overlap
```

**Metadata:** Información extra por chunk
```python
{
    "text": "contenido del chunk",
    "page": 5,
    "section": "Introduction",
    "source": "documento.pdf"
}
```

### 📚 Recursos

**Videos:**
- [Chunking strategies for RAG](https://www.youtube.com/watch?v=8OJC21T2SL4) (15min)
- [Document processing pipeline](https://www.youtube.com/watch?v=5aRZ1eQVE0Y) (20min)

**Artículos:**
- [LangChain Text Splitters](https://python.langchain.com/docs/modules/data_connection/document_transformers/)
- [Chunking strategies compared](https://www.pinecone.io/learn/chunking-strategies/)

**Librerías:**
- PyPDF2, pdfplumber (parseo de PDFs)
- tiktoken (contar tokens)
- LangChain TextSplitters

### 🗓️ Plan día a día (6h total)

**Lunes (1.5h):**
- Ver videos sobre chunking
- Leer sobre estrategias
- Experimentar manualmente con un texto largo

**Martes (1.5h):**
- Instalar librerías: `pip install pypdf2 tiktoken langchain`
- Ejercicio: Parsear un PDF y extraer texto
- Probar diferentes estrategias de chunking

**Miércoles (1.5h):**
- Implementar chunker recursivo desde cero (sin LangChain)
- Entender la lógica interna

**Jueves (1h):**
- Usar LangChain TextSplitters
- Comparar resultados con tu implementación
- Experimentar con overlap

**Viernes (1.5h):**
- Proyecto: Document Processor
  - Upload PDF endpoint
  - Parse y chunk automático
  - Guarda chunks en DB con metadata
  - Endpoints para ver chunks

### 💻 Ejercicio principal: Document Chunking Pipeline

```python
# chunker.py
from typing import List, Dict
import re

class RecursiveChunker:
    """Chunker recursivo que intenta mantener semántica"""
    
    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
        separators: List[str] = None
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separators = separators or ["\n\n", "\n", ". ", " ", ""]
    
    def split_text(self, text: str) -> List[str]:
        """Divide texto recursivamente"""
        chunks = []
        
        # Intentar separar por cada separador en orden
        for separator in self.separators:
            if separator == "":
                # Último recurso: partir por carácter
                chunks = self._split_by_character(text)
                break
            
            if separator in text:
                splits = text.split(separator)
                good_splits = self._merge_splits(splits, separator)
                
                if len(good_splits) > 1:
                    chunks = good_splits
                    break
        
        # Añadir overlap
        if self.chunk_overlap > 0:
            chunks = self._add_overlap(chunks)
        
        return chunks
    
    def _merge_splits(self, splits: List[str], separator: str) -> List[str]:
        """Combina splits para llegar al chunk_size ideal"""
        chunks = []
        current_chunk = []
        current_length = 0
        
        for split in splits:
            split_length = len(split)
            
            if current_length + split_length > self.chunk_size:
                if current_chunk:
                    chunks.append(separator.join(current_chunk))
                    current_chunk = [split]
                    current_length = split_length
                else:
                    chunks.append(split)
            else:
                current_chunk.append(split)
                current_length += split_length + len(separator)
        
        if current_chunk:
            chunks.append(separator.join(current_chunk))
        
        return chunks
    
    def _split_by_character(self, text: str) -> List[str]:
        """Último recurso: partir por caracteres"""
        return [
            text[i:i+self.chunk_size] 
            for i in range(0, len(text), self.chunk_size)
        ]
    
    def _add_overlap(self, chunks: List[str]) -> List[str]:
        """Añade overlap entre chunks"""
        overlapped = []
        
        for i, chunk in enumerate(chunks):
            if i > 0:
                prev_chunk = chunks[i-1]
                overlap_text = prev_chunk[-self.chunk_overlap:]
                chunk = overlap_text + chunk
            
            overlapped.append(chunk)
        
        return overlapped

# Ejemplo de uso
if __name__ == "__main__":
    text = """
    Machine learning is a subset of artificial intelligence.
    
    It focuses on the development of algorithms that can learn from data.
    
    There are three main types of machine learning:
    1. Supervised learning
    2. Unsupervised learning
    3. Reinforcement learning
    
    Each type has its own use cases and applications.
    """
    
    chunker = RecursiveChunker(chunk_size=100, chunk_overlap=20)
    chunks = chunker.split_text(text)
    
    for i, chunk in enumerate(chunks, 1):
        print(f"\n=== Chunk {i} ===")
        print(chunk)
```

**Comparación con LangChain:**

```python
# chunker_comparison.py
from langchain.text_splitter import RecursiveCharacterTextSplitter
from chunker import RecursiveChunker

text = open("sample_document.txt").read()

# Tu implementación
my_chunker = RecursiveChunker(chunk_size=500, chunk_overlap=50)
my_chunks = my_chunker.split_text(text)

# LangChain
lc_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", ". ", " ", ""]
)
lc_chunks = lc_splitter.split_text(text)

print(f"Tu chunker: {len(my_chunks)} chunks")
print(f"LangChain:  {len(lc_chunks)} chunks")

# Ver diferencias
for i in range(min(3, len(my_chunks))):
    print(f"\n=== Chunk {i+1} ===")
    print("Tuyo:")
    print(my_chunks[i][:100] + "...")
    print("\nLangChain:")
    print(lc_chunks[i][:100] + "...")
```

**PDF Processing:**

```python
# pdf_processor.py
import pypdf
from typing import List, Dict

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extrae todo el texto de un PDF"""
    reader = pypdf.PdfReader(pdf_path)
    text = ""
    
    for page in reader.pages:
        text += page.extract_text() + "\n\n"
    
    return text

def extract_with_metadata(pdf_path: str) -> List[Dict]:
    """Extrae texto con metadata de página"""
    reader = pypdf.PdfReader(pdf_path)
    pages = []
    
    for i, page in enumerate(reader.pages, 1):
        pages.append({
            "text": page.extract_text(),
            "page": i,
            "source": pdf_path
        })
    
    return pages

def chunk_pdf(
    pdf_path: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 200
) -> List[Dict]:
    """Procesa PDF completo en chunks con metadata"""
    pages = extract_with_metadata(pdf_path)
    chunker = RecursiveChunker(chunk_size, chunk_overlap)
    
    all_chunks = []
    
    for page_data in pages:
        page_text = page_data["text"]
        chunks = chunker.split_text(page_text)
        
        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "text": chunk,
                "page": page_data["page"],
                "chunk_index": i,
                "source": page_data["source"]
            })
    
    return all_chunks

# Uso
if __name__ == "__main__":
    chunks = chunk_pdf("sample.pdf", chunk_size=500)
    
    print(f"Total chunks: {len(chunks)}")
    print(f"\nPrimer chunk:")
    print(chunks[0])
```

**API para Document Processing:**

```python
# app/main.py
from fastapi import FastAPI, UploadFile, File
from typing import List
import tempfile
import os

app = FastAPI(title="Document Processor API")

@app.post("/process-pdf")
async def process_pdf(
    file: UploadFile = File(...),
    chunk_size: int = 1000,
    chunk_overlap: int = 200
):
    """Procesa PDF y devuelve chunks"""
    
    # Guardar temporalmente
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name
    
    try:
        # Procesar
        chunks = chunk_pdf(tmp_path, chunk_size, chunk_overlap)
        
        return {
            "filename": file.filename,
            "total_chunks": len(chunks),
            "chunks": chunks
        }
    finally:
        os.unlink(tmp_path)

@app.post("/analyze-chunking")
async def analyze_chunking(
    file: UploadFile = File(...),
    sizes: List[int] = [500, 1000, 2000]
):
    """Compara diferentes estrategias de chunking"""
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name
    
    try:
        results = {}
        
        for size in sizes:
            chunks = chunk_pdf(tmp_path, chunk_size=size, chunk_overlap=size//5)
            results[f"size_{size}"] = {
                "num_chunks": len(chunks),
                "avg_chunk_length": sum(len(c["text"]) for c in chunks) / len(chunks),
                "min_chunk_length": min(len(c["text"]) for c in chunks),
                "max_chunk_length": max(len(c["text"]) for c in chunks)
            }
        
        return results
    finally:
        os.unlink(tmp_path)
```

### ✅ Checklist
- [ ] Entiendo por qué es necesario chunking
- [ ] Conozco las diferentes estrategias
- [ ] He implementado un chunker recursivo desde cero
- [ ] Sé usar LangChain TextSplitters
- [ ] Puedo procesar PDFs y extraer texto
- [ ] Document Processor API funciona
- [ ] Entiendo el trade-off entre chunk size y precisión
- [ ] Código en GitHub

---

## Semana 15-17: Proyecto 2 - Docs Q&A Platform (Parte 1)
**20 Enero - 9 Febrero 2027**

### 🎯 Objetivo
Construir la primera mitad del proyecto principal de Fase 2: sistema RAG completo para hacer Q&A sobre documentos.

### 📋 Especificaciones

**Funcionalidad completa (3 semanas):**
- Upload PDFs/Markdown
- Chunking automático
- Embeddings y almacenamiento en pgvector
- API de búsqueda semántica
- Endpoint de Q&A con contexto (RAG)
- UI básica con streaming
- Docker compose completo
- Tests

**Semana 15-16: Backend completo**
**Semana 17: Q&A con RAG + Tests**

### 📚 Conceptos de RAG

**RAG (Retrieval-Augmented Generation):**
1. User hace pregunta
2. Sistema busca chunks relevantes (retrieval)
3. Chunks se pasan como contexto al LLM
4. LLM genera respuesta basada en contexto (generation)

```
User: "¿Qué es FastAPI?"

Retrieval: 
→ Busca embeddings similares a la pregunta
→ Encuentra chunks: ["FastAPI es un framework...", "FastAPI usa Pydantic..."]

Generation:
→ Prompt: "Basándote en estos documentos: {chunks}, responde: {pregunta}"
→ LLM genera respuesta fundamentada
```

**Ventajas vs LLM solo:**
- ✅ Información actualizada (tus documentos)
- ✅ Respuestas fundamentadas (cita fuentes)
- ✅ No hay alucinaciones (LLM limitado a contexto)
- ✅ Privacidad (datos no van al entrenamiento)

### 🗓️ Plan por semana

#### Semana 15 (20-26 Enero)

**Día 1-2 (3h):**
- Diseñar arquitectura completa
- Esquema de base de datos:
  - `documents` table (metadata)
  - `chunks` table (texto + embeddings + FK a documents)
- Setup inicial del proyecto

**Día 3-5 (3h):**
- Implementar models y schemas
- Endpoint para upload de documentos
- Procesamiento: PDF → chunks → embeddings → DB

#### Semana 16 (27 Enero - 2 Febrero)

**Día 1-2 (3h):**
- Endpoint de búsqueda semántica
- Ranking de resultados
- Filtros (por documento, por fecha, etc.)

**Día 3-5 (3h):**
- Implementar RAG pipeline
- Endpoint de Q&A
- Streaming de respuesta
- Citations (qué chunks se usaron)

#### Semana 17 (3-9 Febrero)

**Día 1-3 (4h):**
- Tests completos (pytest)
- Tests de integración para RAG
- Docker compose con todos los servicios

**Día 4-5 (2h):**
- README completo
- Documentación de API
- Ejemplos de uso
- Subir a GitHub

### 💻 Implementación

**Estructura del proyecto:**
```
docs-qa-platform/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── document_processor.py
│   ├── embeddings.py
│   └── rag.py
├── tests/
│   ├── __init__.py
│   ├── test_processing.py
│   ├── test_retrieval.py
│   └── test_rag.py
├── uploads/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

**app/models.py:**
```python
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from pgvector.sqlalchemy import Vector
from .database import Base

class Document(Base):
    __tablename__ = "documents"
    
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(500), nullable=False)
    filetype = Column(String(50))  # pdf, markdown, txt
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
    
    chunks = relationship("Chunk", back_populates="document", cascade="all, delete-orphan")

class Chunk(Base):
    __tablename__ = "chunks"
    
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
    content = Column(Text, nullable=False)
    embedding = Column(Vector(1536))
    chunk_index = Column(Integer)  # orden dentro del documento
    page = Column(Integer, nullable=True)  # para PDFs
    metadata = Column(Text, nullable=True)  # JSON con info extra
    
    document = relationship("Document", back_populates="chunks")
```

**app/schemas.py:**
```python
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class DocumentBase(BaseModel):
    filename: str
    filetype: str

class DocumentCreate(DocumentBase):
    pass

class Document(DocumentBase):
    id: int
    uploaded_at: datetime
    chunk_count: Optional[int] = None
    
    class Config:
        from_attributes = True

class ChunkBase(BaseModel):
    content: str
    chunk_index: int
    page: Optional[int] = None

class Chunk(ChunkBase):
    id: int
    document_id: int
    similarity: Optional[float] = None
    
    class Config:
        from_attributes = True

class SearchQuery(BaseModel):
    query: str
    top_k: int = 5
    document_id: Optional[int] = None

class SearchResult(BaseModel):
    chunks: List[Chunk]
    query: str

class QARequest(BaseModel):
    question: str
    document_id: Optional[int] = None
    top_k: int = 3

class QAResponse(BaseModel):
    question: str
    answer: str
    sources: List[Chunk]
    tokens_used: int
```

**app/document_processor.py:**
```python
import pypdf
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List, Dict

class DocumentProcessor:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
    
    def process_pdf(self, file_path: str) -> List[Dict]:
        """Procesa PDF y devuelve chunks con metadata"""
        reader = pypdf.PdfReader(file_path)
        chunks = []
        
        for page_num, page in enumerate(reader.pages, 1):
            text = page.extract_text()
            page_chunks = self.text_splitter.split_text(text)
            
            for i, chunk in enumerate(page_chunks):
                chunks.append({
                    "content": chunk,
                    "page": page_num,
                    "chunk_index": len(chunks)
                })
        
        return chunks
    
    def process_markdown(self, file_path: str) -> List[Dict]:
        """Procesa Markdown"""
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        text_chunks = self.text_splitter.split_text(text)
        
        return [
            {
                "content": chunk,
                "page": None,
                "chunk_index": i
            }
            for i, chunk in enumerate(text_chunks)
        ]
    
    def process_file(self, file_path: str, filetype: str) -> List[Dict]:
        """Router para procesar según tipo"""
        if filetype == "pdf":
            return self.process_pdf(file_path)
        elif filetype in ["markdown", "md"]:
            return self.process_markdown(file_path)
        elif filetype == "txt":
            return self.process_markdown(file_path)  # mismo proceso
        else:
            raise ValueError(f"Filetype not supported: {filetype}")
```

**app/embeddings.py:**
```python
from openai import OpenAI
import os
from typing import List

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_embedding(text: str) -> List[float]:
    """Genera embedding de un texto"""
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def get_embeddings_batch(texts: List[str]) -> List[List[float]]:
    """Genera embeddings en batch (más eficiente)"""
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    return [item.embedding for item in response.data]
```

**app/rag.py:**
```python
from openai import OpenAI
from typing import List, Dict
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_answer(question: str, context_chunks: List[Dict]) -> Dict:
    """Genera respuesta basada en chunks recuperados"""
    
    # Construir contexto
    context = "\n\n".join([
        f"[Documento: {chunk['document_filename']}, Página: {chunk.get('page', 'N/A')}]\n{chunk['content']}"
        for chunk in context_chunks
    ])
    
    # Prompt
    system_prompt = """Eres un asistente que responde preguntas basándote SOLO en el contexto proporcionado.

Reglas:
1. Usa SOLO información del contexto
2. Si la respuesta no está en el contexto, di "No tengo información suficiente"
3. Cita las fuentes (documento y página) al responder
4. Sé conciso pero completo"""

    user_prompt = f"""Contexto:
{context}

Pregunta: {question}

Responde de forma clara y citando las fuentes."""

    # Llamada a LLM
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3,
        max_tokens=1000
    )
    
    return {
        "answer": response.choices[0].message.content,
        "tokens_used": response.usage.total_tokens
    }

def generate_answer_streaming(question: str, context_chunks: List[Dict]):
    """Versión con streaming (para UI en tiempo real)"""
    
    context = "\n\n".join([
        f"[Doc: {chunk['document_filename']}]\n{chunk['content']}"
        for chunk in context_chunks
    ])
    
    system_prompt = """Responde basándote SOLO en el contexto proporcionado.
Si no sabes, di "No tengo información suficiente"."""

    user_prompt = f"""Contexto:
{context}

Pregunta: {question}"""

    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3,
        stream=True
    )
    
    for chunk in stream:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content
```

**app/main.py (endpoints principales):**
```python
from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from sqlalchemy import text
import tempfile
import os
from typing import List

from . import models, schemas, crud
from .database import engine, get_db
from .document_processor import DocumentProcessor
from .embeddings import get_embeddings_batch
from .rag import generate_answer, generate_answer_streaming

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Docs Q&A Platform")
processor = DocumentProcessor()

@app.post("/documents/upload", response_model=schemas.Document, status_code=201)
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """Upload y procesa un documento"""
    
    # Validar tipo
    filetype = file.filename.split('.')[-1].lower()
    if filetype not in ['pdf', 'md', 'txt']:
        raise HTTPException(400, "Filetype not supported")
    
    # Guardar temporalmente
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{filetype}") as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name
    
    try:
        # Procesar
        chunks_data = processor.process_file(tmp_path, filetype)
        
        # Crear documento en DB
        doc = models.Document(filename=file.filename, filetype=filetype)
        db.add(doc)
        db.commit()
        db.refresh(doc)
        
        # Generar embeddings en batch
        texts = [chunk["content"] for chunk in chunks_data]
        embeddings = get_embeddings_batch(texts)
        
        # Guardar chunks
        for chunk_data, embedding in zip(chunks_data, embeddings):
            chunk = models.Chunk(
                document_id=doc.id,
                content=chunk_data["content"],
                embedding=embedding,
                chunk_index=chunk_data["chunk_index"],
                page=chunk_data.get("page")
            )
            db.add(chunk)
        
        db.commit()
        
        return doc
        
    finally:
        os.unlink(tmp_path)

@app.get("/documents", response_model=List[schemas.Document])
def get_documents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Lista documentos"""
    docs = db.query(models.Document).offset(skip).limit(limit).all()
    
    # Añadir chunk count
    for doc in docs:
        doc.chunk_count = len(doc.chunks)
    
    return docs

@app.post("/search", response_model=schemas.SearchResult)
def search(query: schemas.SearchQuery, db: Session = Depends(get_db)):
    """Búsqueda semántica"""
    from .embeddings import get_embedding
    
    # Embed query
    query_embedding = get_embedding(query.query)
    
    # SQL query con filtro opcional por documento
    sql = """
        SELECT 
            c.id,
            c.document_id,
            c.content,
            c.chunk_index,
            c.page,
            d.filename,
            1 - (c.embedding <=> :embedding) as similarity
        FROM chunks c
        JOIN documents d ON c.document_id = d.id
    """
    
    params = {"embedding": str(query_embedding), "limit": query.top_k}
    
    if query.document_id:
        sql += " WHERE c.document_id = :doc_id"
        params["doc_id"] = query.document_id
    
    sql += """
        ORDER BY c.embedding <=> :embedding
        LIMIT :limit
    """
    
    results = db.execute(text(sql), params).fetchall()
    
    chunks = [
        schemas.Chunk(
            id=r[0],
            document_id=r[1],
            content=r[2],
            chunk_index=r[3],
            page=r[4],
            similarity=float(r[6])
        )
        for r in results
    ]
    
    return schemas.SearchResult(query=query.query, chunks=chunks)

@app.post("/qa", response_model=schemas.QAResponse)
def question_answer(request: schemas.QARequest, db: Session = Depends(get_db)):
    """Q&A con RAG"""
    from .embeddings import get_embedding
    
    # 1. Retrieval
    query_embedding = get_embedding(request.question)
    
    sql = """
        SELECT 
            c.id, c.content, c.page, c.chunk_index,
            d.filename
        FROM chunks c
        JOIN documents d ON c.document_id = d.id
    """
    
    params = {"embedding": str(query_embedding), "limit": request.top_k}
    
    if request.document_id:
        sql += " WHERE c.document_id = :doc_id"
        params["doc_id"] = request.document_id
    
    sql += " ORDER BY c.embedding <=> :embedding LIMIT :limit"
    
    results = db.execute(text(sql), params).fetchall()
    
    context_chunks = [
        {
            "id": r[0],
            "content": r[1],
            "page": r[2],
            "chunk_index": r[3],
            "document_filename": r[4]
        }
        for r in results
    ]
    
    # 2. Generation
    rag_result = generate_answer(request.question, context_chunks)
    
    # 3. Preparar respuesta
    sources = [
        schemas.Chunk(
            id=c["id"],
            document_id=0,  # placeholder
            content=c["content"],
            chunk_index=c["chunk_index"],
            page=c["page"]
        )
        for c in context_chunks
    ]
    
    return schemas.QAResponse(
        question=request.question,
        answer=rag_result["answer"],
        sources=sources,
        tokens_used=rag_result["tokens_used"]
    )

@app.post("/qa/stream")
async def question_answer_stream(request: schemas.QARequest, db: Session = Depends(get_db)):
    """Q&A con respuesta en streaming"""
    from .embeddings import get_embedding
    
    # Retrieval (igual que arriba)
    query_embedding = get_embedding(request.question)
    
    sql = """
        SELECT c.id, c.content, c.page, d.filename
        FROM chunks c
        JOIN documents d ON c.document_id = d.id
        ORDER BY c.embedding <=> :embedding
        LIMIT :limit
    """
    
    results = db.execute(
        text(sql),
        {"embedding": str(query_embedding), "limit": request.top_k}
    ).fetchall()
    
    context_chunks = [
        {"id": r[0], "content": r[1], "page": r[2], "document_filename": r[3]}
        for r in results
    ]
    
    # Streaming
    return StreamingResponse(
        generate_answer_streaming(request.question, context_chunks),
        media_type="text/event-stream"
    )
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  db:
    image: ankane/pgvector
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
      POSTGRES_DB: docs_qa_db
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5

  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://postgres:password@db:5432/docs_qa_db
      OPENAI_API_KEY: ${OPENAI_API_KEY}
    depends_on:
      db:
        condition: service_healthy
    volumes:
      - ./app:/app/app
      - ./uploads:/app/uploads

volumes:
  postgres_data:
```

**Tests (tests/test_rag.py):**
```python
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_document():
    """Test upload de PDF"""
    with open("test_data/sample.pdf", "rb") as f:
        response = client.post(
            "/documents/upload",
            files={"file": ("sample.pdf", f, "application/pdf")}
        )
    
    assert response.status_code == 201
    data = response.json()
    assert data["filename"] == "sample.pdf"
    assert data["filetype"] == "pdf"
    return data["id"]

def test_search():
    """Test búsqueda semántica"""
    doc_id = test_upload_document()
    
    response = client.post("/search", json={
        "query": "What is FastAPI?",
        "top_k": 3,
        "document_id": doc_id
    })
    
    assert response.status_code == 200
    data = response.json()
    assert len(data["chunks"]) > 0
    assert data["chunks"][0]["similarity"] > 0.5

def test_qa():
    """Test Q&A end-to-end"""
    doc_id = test_upload_document()
    
    response = client.post("/qa", json={
        "question": "What is FastAPI used for?",
        "document_id": doc_id,
        "top_k": 3
    })
    
    assert response.status_code == 200
    data = response.json()
    assert len(data["answer"]) > 0
    assert len(data["sources"]) > 0
    assert data["tokens_used"] > 0
```

### ✅ Checklist del Proyecto
- [ ] Upload de documentos funciona (PDF, MD, TXT)
- [ ] Chunking automático
- [ ] Embeddings generados y guardados en pgvector
- [ ] Búsqueda semántica funciona correctamente
- [ ] Q&A con RAG devuelve respuestas fundamentadas
- [ ] Streaming de respuestas implementado
- [ ] Cita fuentes (documento y página)
- [ ] Docker compose levanta todo
- [ ] Tests completos (>80% coverage)
- [ ] README con ejemplos de uso
- [ ] Código en GitHub

**Este es tu proyecto STAR para el portfolio.** Dedícale 3 semanas completas.

---

*(Continuaría con las semanas 18-24 de Fase 2, Fase 3 (Producción + Agents), Fase 4 (Deploy + Empleo), Recursos Generales, Networking Madrid, y Preparación de Entrevistas...)*

*Dado el límite de longitud, he creado una base MUY sólida y detallada de las primeras 17 semanas. El documento completo de 48 semanas seguiría este mismo nivel de detalle.*

---

## Continuación recomendada

Para las semanas restantes (18-48), el documento seguiría con:

**Fase 2 (continúa):**
- Semana 18: LangChain avanzado
- Semana 19: Reranking y hybrid search
- Semana 20: Optimización de RAG (chunking strategies avanzadas)
- Semana 21-24: Mejorar Docs Q&A con UI, auth, y features avanzadas

**Fase 3: Producción + Agents (Abr-Jun):**
- LLM observability (Langfuse)
- Evaluations y benchmarking
- Safety (guardrails, content moderation)
- AI Agents con LangGraph
- Tool calling
- Memory y state
- Proyecto 3: Production Support Bot

**Fase 4: Deploy + Empleo (Jul-Sep):**
- AWS (EC2, S3, RDS, ECS)
- CI/CD con GitHub Actions
- Monitoring y alertas
- Proyecto final: AI Micro-SaaS deployado
- Preparación intensiva de entrevistas
- Networking activo
- Aplicaciones a empresas

---

## SEMANA 18: LangChain Deep Dive

### 🎯 Objetivo
Dominar LangChain más allá de los tutoriales: chains, memory, callbacks y debugging.

### 📖 Conceptos clave

**¿Qué es LangChain realmente?**
No es magia. Es un framework que:
- **Abstrae** las llamadas a LLMs (OpenAI, Anthropic, etc.)
- **Encadena** prompts y operaciones (chains)
- **Gestiona** memoria de conversaciones
- **Integra** herramientas externas (tools)

**Componentes principales:**
1. **LLMs/ChatModels**: wrappers sobre APIs
2. **PromptTemplates**: prompts reutilizables con variables
3. **Chains**: secuencias de operaciones
4. **Memory**: mantener contexto entre llamadas
5. **Agents**: LLMs que deciden qué herramientas usar

**Por qué importa:**
Muchas empresas usan LangChain. Pero ojo: también debes entender qué hace por debajo para cuando falle o necesites customizar.

### 📚 Recursos

**Documentación oficial:**
- [LangChain Docs](https://python.langchain.com/docs/get_started/introduction) - Lee "Quickstart" + "Core concepts" (45min)
- [LangChain Expression Language (LCEL)](https://python.langchain.com/docs/expression_language/) (30min)

**Videos:**
- [LangChain Crash Course - FreeCodeCamp](https://www.youtube.com/watch?v=lG7Uxts9SXs) (1h30 - ver primera hora)
- [LangChain Expression Language Explained](https://www.youtube.com/watch?v=hGXhFMWgJBI) (20min)

**Repositorio de referencia:**
- [langchain-tutorials GitHub](https://github.com/gkamradt/langchain-tutorials) - ejemplos prácticos

### 🗓️ Plan semanal (6h)

**Lunes (1.5h): Fundamentos LangChain**
- Instalar: `pip install langchain langchain-openai langchain-community`
- Ver primer video hasta minuto 30
- Leer docs "Core concepts"
- Ejercicio: convertir tu CLI anterior a usar LangChain en vez de OpenAI SDK directo

**Martes (1.5h): Chains y LCEL**
```python
# chains_example.py
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

# Define chain usando LCEL (| operator)
llm = ChatOpenAI(model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_template(
    "Eres un asistente técnico. Explica {concept} en 2 párrafos."
)

chain = prompt | llm | StrOutputParser()

# Ejecutar
result = chain.invoke({"concept": "RAG"})
print(result)

# Chain con múltiples pasos
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

# Paso 1: generar idea
idea_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Dame una idea de proyecto AI sobre {topic}"
)
idea_chain = LLMChain(llm=llm, prompt=idea_prompt, output_key="idea")

# Paso 2: crear plan
plan_prompt = PromptTemplate(
    input_variables=["idea"],
    template="Crea un plan de implementación para: {idea}"
)
plan_chain = LLMChain(llm=llm, prompt=plan_prompt, output_key="plan")

# Combinar
full_chain = SequentialChain(
    chains=[idea_chain, plan_chain],
    input_variables=["topic"],
    output_variables=["idea", "plan"],
    verbose=True
)

result = full_chain({"topic": "salud mental"})
print(result)
```

Ejercicio: crea 3 chains diferentes (summarize, Q&A, code generation).

**Miércoles (1.5h): Memory**
```python
# memory_example.py
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

# Buffer memory (guarda todo)
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

print(conversation.predict(input="Hola, me llamo Marco"))
print(conversation.predict(input="¿Cuál es mi nombre?"))
print(conversation.predict(input="¿De qué hemos hablado?"))

# Ver el historial
print("\nMemoria:")
print(memory.buffer)

# Summary memory (resume conversaciones largas)
summary_memory = ConversationSummaryMemory(llm=llm)
conversation_summary = ConversationChain(
    llm=llm,
    memory=summary_memory,
    verbose=True
)

# Simula una conversación larga
for i in range(5):
    conversation_summary.predict(input=f"Cuéntame sobre el tema {i}")

print("\nResumen:", summary_memory.buffer)
```

**Tipos de memory:**
- `ConversationBufferMemory`: guarda todo (caro con conversaciones largas)
- `ConversationBufferWindowMemory`: solo últimas K interacciones
- `ConversationSummaryMemory`: resume periódicamente
- `ConversationSummaryBufferMemory`: híbrido (recomendado)

Ejercicio: implementa chatbot con memory que recuerde preferencias del usuario.

**Jueves (1h): Callbacks y debugging**
```python
# callbacks_example.py
from langchain.callbacks.base import BaseCallbackHandler
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

class MyCallback(BaseCallbackHandler):
    def on_llm_start(self, serialized, prompts, **kwargs):
        print(f"🚀 LLM Start: {prompts}")
    
    def on_llm_end(self, response, **kwargs):
        print(f"✅ LLM End: {response.generations[0][0].text[:100]}")
    
    def on_llm_error(self, error, **kwargs):
        print(f"❌ Error: {error}")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    callbacks=[MyCallback()]
)

response = llm.invoke([HumanMessage(content="Hola")])
print(response.content)
```

**Por qué importa:**
Los callbacks te permiten:
- Logging detallado
- Tracking de tokens/costos
- Streaming de respuestas
- Debugging

Ejercicio: añade callback que cuente tokens usados.

**Viernes (1.5h): Migrar Docs Q&A a LangChain**
Refactoriza tu proyecto anterior usando:
- `ChatOpenAI` en vez de cliente directo
- `PromptTemplate` para query reformulation
- `ConversationChain` con memory para follow-up questions

Compara código antes/después. ¿Más legible? ¿Más flexible?

### ✅ Checklist de dominio

- [ ] Entiendes qué problema soluciona LangChain
- [ ] Has creado chains con LCEL (| operator)
- [ ] Implementaste conversación con memory
- [ ] Usaste callbacks para debugging
- [ ] Sabes cuándo usar LangChain vs código custom
- [ ] Migraste un proyecto anterior a LangChain

---

## SEMANA 19: Optimización RAG I - Chunking y Metadata

### 🎯 Objetivo
Mejorar calidad de retrieval: chunking inteligente, metadata filtering, hybrid search.

### 📖 Conceptos clave

**El problema del chunking naive:**
Tu implementación actual probablemente hace:
```python
chunks = text.split("\n\n")  # ❌ Muy básico
```

**Problemas:**
- Pierde contexto semántico
- Corta frases a mitad
- No respeta estructura del documento
- Chunks muy desiguales

**Estrategias mejores:**

1. **Recursive Character Text Splitter** (LangChain):
   - Intenta dividir por párrafos
   - Si no cabe, por frases
   - Si no, por caracteres
   
2. **Semantic Chunking**:
   - Agrupa texto por similitud semántica
   - Más costoso pero mejor calidad

3. **Document-aware chunking**:
   - Respeta headers, secciones
   - Mantiene jerarquía

**Metadata:**
Cada chunk debe llevar:
```python
{
    "text": "...",
    "source": "manual.pdf",
    "page": 5,
    "section": "Installation",
    "chunk_id": "uuid",
    "char_count": 450,
    "embedding": [0.1, 0.2, ...]
}
```

**Por qué importa:**
Permite filtrar antes de buscar: "busca solo en sección X" o "documentos de 2024".

**Hybrid Search:**
Combina:
- **Dense retrieval** (embeddings): entiende semántica
- **Sparse retrieval** (BM25/keyword): busca términos exactos

Mejor recall y precision.

### 📚 Recursos

**Artículos:**
- [Chunking Strategies for RAG - Pinecone](https://www.pinecone.io/learn/chunking-strategies/) (15min)
- [Advanced RAG Techniques - LlamaIndex](https://docs.llamaindex.ai/en/stable/optimizing/production_rag/) (20min)
- [Hybrid Search Explained](https://www.algolia.com/blog/ai/what-is-hybrid-search/) (10min)

**Videos:**
- [RAG Chunking Best Practices](https://www.youtube.com/watch?v=8OJC21T2SL4) (25min)
- [Metadata Filtering in Vector DBs](https://www.youtube.com/watch?v=gTCU9I6QqCE) (15min)

**Papers (opcional pero recomendado):**
- [Lost in the Middle](https://arxiv.org/abs/2307.03172) - por qué el orden de chunks importa

### 🗓️ Plan semanal (6h)

**Lunes (1.5h): Chunking inteligente**
```python
# smart_chunking.py
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    CharacterTextSplitter
)
import tiktoken

# Contador de tokens real
def count_tokens(text: str, model: str = "gpt-4o-mini") -> int:
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

# Splitter básico
basic_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=500,
    chunk_overlap=50
)

# Splitter recursivo (mejor)
recursive_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", ". ", " ", ""],  # Orden de prioridad
    chunk_size=500,
    chunk_overlap=100,  # Overlap importante para contexto
    length_function=count_tokens,  # Usa tokens reales
    is_separator_regex=False
)

# Ejemplo
doc = """
# Introduction to RAG

Retrieval Augmented Generation (RAG) is a technique...

## How it works

RAG combines retrieval with generation...

## Benefits

The main benefits are...
"""

chunks_basic = basic_splitter.split_text(doc)
chunks_recursive = recursive_splitter.split_text(doc)

print("Basic chunks:", len(chunks_basic))
for i, chunk in enumerate(chunks_basic):
    print(f"\nChunk {i}:\n{chunk[:100]}...")

print("\n\nRecursive chunks:", len(chunks_recursive))
for i, chunk in enumerate(chunks_recursive):
    print(f"\nChunk {i} ({count_tokens(chunk)} tokens):\n{chunk[:100]}...")
```

Ejercicio: procesa un PDF largo con ambos métodos y compara resultados.

**Martes (1.5h): Metadata extraction**
```python
# metadata_enrichment.py
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from datetime import datetime
import hashlib
import re

def extract_section_from_text(text: str) -> str:
    """Intenta extraer título de sección"""
    # Busca headers markdown
    match = re.search(r'^#+\s+(.+)$', text, re.MULTILINE)
    if match:
        return match.group(1)
    # Busca línea en mayúsculas
    match = re.search(r'^([A-Z\s]{5,})$', text, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return "Unknown"

def enrich_chunks(chunks, source_file: str, doc_metadata: dict = None):
    """Añade metadata rica a cada chunk"""
    enriched = []
    
    for i, chunk in enumerate(chunks):
        chunk_id = hashlib.md5(chunk.encode()).hexdigest()[:12]
        
        metadata = {
            "chunk_id": chunk_id,
            "source": source_file,
            "chunk_index": i,
            "total_chunks": len(chunks),
            "char_count": len(chunk),
            "word_count": len(chunk.split()),
            "section": extract_section_from_text(chunk),
            "ingested_at": datetime.now().isoformat(),
        }
        
        # Merge con metadata del documento
        if doc_metadata:
            metadata.update(doc_metadata)
        
        enriched.append({
            "text": chunk,
            "metadata": metadata
        })
    
    return enriched

# Uso
loader = PyPDFLoader("manual.pdf")
pages = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

all_enriched_chunks = []
for page in pages:
    chunks = splitter.split_text(page.page_content)
    
    doc_meta = {
        "page_number": page.metadata.get("page", 0),
        "document_type": "manual",
        "version": "2.0"
    }
    
    enriched = enrich_chunks(chunks, "manual.pdf", doc_meta)
    all_enriched_chunks.extend(enriched)

# Ver resultado
print(all_enriched_chunks[0])
```

Ejercicio: crea pipeline que procese múltiples PDFs y extraiga metadata automáticamente.

**Miércoles (1.5h): Metadata filtering en pgvector**
```python
# metadata_filtering.py
from sqlalchemy import create_engine, Column, Integer, String, JSON, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pgvector.sqlalchemy import Vector

Base = declarative_base()

class DocumentChunk(Base):
    __tablename__ = 'document_chunks_v2'
    
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    embedding = Column(Vector(1536))  # text-embedding-3-small
    source = Column(String)
    page_number = Column(Integer)
    section = Column(String)
    document_type = Column(String)
    metadata_json = Column(JSON)  # Resto de metadata

# Conexión
engine = create_engine("postgresql://user:pass@localhost/dbname")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Query con filtros
def search_with_filters(
    query_embedding,
    filters: dict = None,
    limit: int = 5
):
    query = session.query(DocumentChunk).order_by(
        DocumentChunk.embedding.cosine_distance(query_embedding)
    )
    
    # Aplicar filtros
    if filters:
        if "source" in filters:
            query = query.filter(DocumentChunk.source == filters["source"])
        if "document_type" in filters:
            query = query.filter(DocumentChunk.document_type == filters["document_type"])
        if "section" in filters:
            query = query.filter(DocumentChunk.section.ilike(f"%{filters['section']}%"))
    
    return query.limit(limit).all()

# Uso
from openai import OpenAI
client = OpenAI()

query = "How do I install the software?"
query_embedding = client.embeddings.create(
    input=query,
    model="text-embedding-3-small"
).data[0].embedding

# Buscar solo en manual, sección installation
results = search_with_filters(
    query_embedding,
    filters={
        "document_type": "manual",
        "section": "Installation"
    }
)

for result in results:
    print(f"\n[{result.source} - {result.section}]")
    print(result.text[:200])
```

Ejercicio: implementa filtros por fecha, autor, idioma.

**Jueves (1.5h): Hybrid Search con BM25**
```python
# hybrid_search.py
from rank_bm25 import BM25Okapi
import numpy as np
from typing import List, Tuple

class HybridRetriever:
    def __init__(self, documents: List[str], embeddings: List[List[float]]):
        self.documents = documents
        self.embeddings = np.array(embeddings)
        
        # Preparar BM25
        tokenized_docs = [doc.lower().split() for doc in documents]
        self.bm25 = BM25Okapi(tokenized_docs)
    
    def dense_search(self, query_embedding: List[float], top_k: int = 10) -> List[Tuple[int, float]]:
        """Búsqueda por embeddings"""
        similarities = np.dot(self.embeddings, query_embedding)
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        return [(idx, similarities[idx]) for idx in top_indices]
    
    def sparse_search(self, query: str, top_k: int = 10) -> List[Tuple[int, float]]:
        """Búsqueda keyword (BM25)"""
        tokenized_query = query.lower().split()
        scores = self.bm25.get_scores(tokenized_query)
        top_indices = np.argsort(scores)[::-1][:top_k]
        
        return [(idx, scores[idx]) for idx in top_indices]
    
    def hybrid_search(
        self,
        query: str,
        query_embedding: List[float],
        top_k: int = 5,
        alpha: float = 0.5  # Balance: 0=solo sparse, 1=solo dense
    ) -> List[Tuple[int, float]]:
        """Combina ambos métodos"""
        dense_results = dict(self.dense_search(query_embedding, top_k * 2))
        sparse_results = dict(self.sparse_search(query, top_k * 2))
        
        # Normalizar scores
        all_indices = set(dense_results.keys()) | set(sparse_results.keys())
        
        combined_scores = {}
        for idx in all_indices:
            dense_score = dense_results.get(idx, 0)
            sparse_score = sparse_results.get(idx, 0)
            
            # Combinar con alpha
            combined_scores[idx] = alpha * dense_score + (1 - alpha) * sparse_score
        
        # Ordenar
        sorted_results = sorted(
            combined_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        return sorted_results[:top_k]

# Ejemplo de uso
documents = [
    "Python is a programming language",
    "FastAPI is a web framework for Python",
    "Machine learning uses algorithms",
    "Deep learning is a subset of ML"
]

# Simula embeddings (en real, usa OpenAI)
embeddings = np.random.rand(len(documents), 1536)

retriever = HybridRetriever(documents, embeddings.tolist())

query = "Python web framework"
query_embedding = np.random.rand(1536).tolist()  # En real: OpenAI

results = retriever.hybrid_search(query, query_embedding, alpha=0.7)

print("Hybrid search results:")
for idx, score in results:
    print(f"{score:.3f}: {documents[idx]}")
```

**Instalar:** `pip install rank-bm25`

Ejercicio: integra hybrid search en tu proyecto Docs Q&A.

**Viernes (1h): Refactorizar proyecto con mejoras**
Actualiza tu Docs Q&A Platform:
1. Reemplaza chunking básico por RecursiveCharacterTextSplitter
2. Añade metadata rica (source, page, section, timestamps)
3. Implementa filtros en queries
4. (Bonus) Añade hybrid search

Mide mejora en calidad de respuestas con 5 preguntas de test.

### ✅ Checklist de dominio

- [ ] Entiendes diferencia entre chunking naive y recursivo
- [ ] Implementaste metadata extraction automática
- [ ] Añadiste filtros por metadata en búsqueda
- [ ] Probaste hybrid search (dense + sparse)
- [ ] Refactorizaste proyecto anterior con mejoras
- [ ] Mediste mejora en calidad de retrieval

---

## SEMANA 20: Optimización RAG II - Reranking y Query Enhancement

### 🎯 Objetivo
Técnicas avanzadas: query reformulation, reranking, parent-child retrieval.

### 📖 Conceptos clave

**El problema:**
El vector search inicial puede traer documentos no óptimos. Necesitas una segunda pasada.

**Reranking:**
1. Primera pasada: retrieval rápido (top 20-50 candidatos)
2. Segunda pasada: reranker preciso (top 3-5 finales)

**Modelos de reranking:**
- **Cross-encoders** (BERT, etc.): muy precisos pero lentos
- **Cohere Rerank API**: fácil de usar, buena calidad
- **Custom scoring**: reglas de negocio + similarity

**Query Enhancement:**

1. **Query Expansion:**
   ```
   Query: "error de instalación"
   Expanded: "error de instalación" OR "problema instalando" OR "fallo durante setup"
   ```

2. **Hypothetical Document Embeddings (HyDE):**
   - Genera respuesta hipotética a la query
   - Busca documentos similares a esa respuesta
   - Funciona sorprendentemente bien

3. **Multi-Query:**
   - Genera variaciones de la pregunta
   - Busca con todas
   - Combina resultados

**Parent-Child Retrieval:**
- Embeddings de chunks pequeños (mejor precisión)
- Pero retorna chunks grandes o documento completo (mejor contexto)

### 📚 Recursos

**Artículos:**
- [Reranking in RAG - Cohere](https://txt.cohere.com/rerank/) (15min)
- [HyDE Explained](https://blog.llamaindex.ai/llms-as-a-retrieval-mechanism-hyde-84bd368e6ae8) (10min)
- [Advanced RAG Patterns](https://blog.langchain.dev/deconstructing-rag/) (20min)

**Videos:**
- [Query Rewriting for Better RAG](https://www.youtube.com/watch?v=5vqPM6qNpxA) (18min)
- [Reranking Tutorial](https://www.youtube.com/watch?v=_AYT5s_4f8I) (25min)

**Papers:**
- [HyDE: Precise Zero-Shot Dense Retrieval](https://arxiv.org/abs/2212.10496) (opcional)

### 🗓️ Plan semanal (6h)

**Lunes (1.5h): Query reformulation**
```python
# query_enhancement.py
from openai import OpenAI
from typing import List

client = OpenAI()

def expand_query_multiquery(query: str, num_variations: int = 3) -> List[str]:
    """Genera variaciones de la query"""
    prompt = f"""Generate {num_variations} different versions of this question to retrieve relevant documents:

Original: {query}

Variations:"""
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    
    variations = response.choices[0].message.content.strip().split("\n")
    variations = [v.strip("- 1234567890.") for v in variations if v.strip()]
    
    return [query] + variations[:num_variations]

def hyde_query(query: str) -> str:
    """Genera documento hipotético (HyDE)"""
    prompt = f"""Write a detailed passage that would perfectly answer this question:

Question: {query}

Passage:"""
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=200
    )
    
    return response.choices[0].message.content.strip()

def decompose_query(query: str) -> List[str]:
    """Descompone query compleja en sub-queries"""
    prompt = f"""Break down this complex question into simpler sub-questions:

Question: {query}

Sub-questions:"""
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    
    subqueries = response.choices[0].message.content.strip().split("\n")
    return [q.strip("- 1234567890.") for q in subqueries if q.strip()]

# Ejemplos
query = "¿Cómo soluciono errores de autenticación en producción?"

print("Multi-Query:")
for q in expand_query_multiquery(query):
    print(f"  - {q}")

print("\nHyDE:")
print(hyde_query(query))

print("\nDecomposed:")
for q in decompose_query(query):
    print(f"  - {q}")
```

Ejercicio: implementa función que combine resultados de múltiples queries (fusión por score).

**Martes (1.5h): Reranking con Cohere**
```python
# reranking.py
import cohere
from typing import List, Tuple
import os

# Necesitas API key de Cohere (tiene free tier)
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def rerank_results(
    query: str,
    documents: List[str],
    top_n: int = 3
) -> List[Tuple[str, float]]:
    """Reordena documentos por relevancia"""
    
    results = co.rerank(
        model="rerank-english-v3.0",  # o rerank-multilingual-v3.0
        query=query,
        documents=documents,
        top_n=top_n,
        return_documents=True
    )
    
    reranked = [
        (result.document.text, result.relevance_score)
        for result in results.results
    ]
    
    return reranked

# Ejemplo
query = "How do I deploy a FastAPI app?"

# Simula resultados de vector search (algunos buenos, otros no tanto)
candidates = [
    "FastAPI is a modern Python web framework.",
    "To deploy FastAPI, you can use Docker with Gunicorn and Uvicorn workers.",
    "Python has many web frameworks like Django and Flask.",
    "Deployment options include AWS, GCP, and Azure. For FastAPI specifically, use containers.",
    "Machine learning models can be served via APIs."
]

print("Before reranking:")
for i, doc in enumerate(candidates):
    print(f"{i+1}. {doc}")

reranked = rerank_results(query, candidates, top_n=3)

print("\nAfter reranking:")
for doc, score in reranked:
    print(f"{score:.3f}: {doc}")
```

**Setup:**
```bash
pip install cohere
# Consigue API key en https://dashboard.cohere.com/
export COHERE_API_KEY="your-key"
```

**Alternativa sin Cohere (cross-encoder manual):**
```python
from sentence_transformers import CrossEncoder

model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def rerank_with_crossencoder(query: str, documents: List[str], top_n: int = 3):
    pairs = [[query, doc] for doc in documents]
    scores = model.predict(pairs)
    
    # Ordenar por score
    ranked = sorted(zip(documents, scores), key=lambda x: x[1], reverse=True)
    return ranked[:top_n]

# Uso igual que antes
```

Ejercicio: compara resultados con/sin reranking en tu proyecto.

**Miércoles (1.5h): Parent-Child Retrieval**
```python
# parent_child_retrieval.py
from typing import List, Dict
from dataclasses import dataclass
import uuid

@dataclass
class Chunk:
    id: str
    text: str
    embedding: List[float]
    parent_id: str
    
@dataclass
class Document:
    id: str
    text: str
    chunks: List[Chunk]

def chunk_with_parents(document_text: str, chunk_size: int = 200) -> Document:
    """Crea chunks pequeños pero mantiene referencia al documento completo"""
    doc_id = str(uuid.uuid4())
    
    # Chunking simple (mejorar con RecursiveCharacterTextSplitter)
    words = document_text.split()
    chunks = []
    
    for i in range(0, len(words), chunk_size):
        chunk_text = " ".join(words[i:i+chunk_size])
        
        chunk = Chunk(
            id=str(uuid.uuid4()),
            text=chunk_text,
            embedding=get_embedding(chunk_text),  # Tu función de embeddings
            parent_id=doc_id
        )
        chunks.append(chunk)
    
    return Document(
        id=doc_id,
        text=document_text,
        chunks=chunks
    )

# Base de datos
class ParentChildStore:
    def __init__(self):
        self.documents: Dict[str, Document] = {}
        self.chunks: Dict[str, Chunk] = {}
    
    def add_document(self, doc: Document):
        self.documents[doc.id] = doc
        for chunk in doc.chunks:
            self.chunks[chunk.id] = chunk
    
    def search_and_retrieve_parent(
        self,
        query_embedding: List[float],
        top_k: int = 3
    ) -> List[Document]:
        """Busca por chunks pero retorna documentos completos"""
        
        # 1. Buscar mejores chunks
        chunk_scores = []
        for chunk in self.chunks.values():
            similarity = cosine_similarity(query_embedding, chunk.embedding)
            chunk_scores.append((chunk, similarity))
        
        chunk_scores.sort(key=lambda x: x[1], reverse=True)
        top_chunks = chunk_scores[:top_k]
        
        # 2. Recuperar documentos padres (únicos)
        parent_ids = set(chunk.parent_id for chunk, _ in top_chunks)
        parent_docs = [self.documents[pid] for pid in parent_ids]
        
        return parent_docs

def cosine_similarity(a: List[float], b: List[float]) -> float:
    import numpy as np
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Uso
store = ParentChildStore()

doc_text = """
[Documento largo con múltiples secciones...]
"""

doc = chunk_with_parents(doc_text)
store.add_document(doc)

# Buscar
query_emb = get_embedding("How to configure?")
results = store.search_and_retrieve_parent(query_emb, top_k=2)

for doc in results:
    print(f"Document ID: {doc.id}")
    print(f"Full text: {doc.text[:200]}...")
```

**Ventaja:**
- Embeddings de chunks pequeños = mejor precisión en búsqueda
- Pero LLM recibe documento completo = mejor contexto

Ejercicio: implementa variante "sentence window" (busca por frase, retorna párrafo).

**Jueves (1.5h): Pipeline completo de RAG avanzado**
```python
# advanced_rag_pipeline.py
from typing import List, Dict
from openai import OpenAI
import cohere

client = OpenAI()
co = cohere.Client()

class AdvancedRAGPipeline:
    def __init__(self, vector_store):
        self.vector_store = vector_store
    
    def query(self, user_query: str, top_k: int = 5) -> Dict:
        """Pipeline completo con todas las optimizaciones"""
        
        # 1. Query Enhancement: generar variaciones
        queries = self.expand_query(user_query)
        print(f"Generated {len(queries)} query variations")
        
        # 2. Multi-query retrieval
        all_candidates = []
        for query in queries:
            query_emb = self.get_embedding(query)
            results = self.vector_store.search(query_emb, top_k=20)
            all_candidates.extend(results)
        
        # Deduplicar
        unique_docs = {doc['id']: doc for doc in all_candidates}.values()
        print(f"Retrieved {len(unique_docs)} unique candidates")
        
        # 3. Reranking
        reranked = self.rerank(user_query, list(unique_docs), top_n=top_k)
        print(f"Reranked to top {len(reranked)}")
        
        # 4. Generar respuesta con contexto
        context = "\n\n".join([doc['text'] for doc, score in reranked])
        answer = self.generate_answer(user_query, context)
        
        return {
            "answer": answer,
            "sources": [
                {
                    "text": doc['text'][:200],
                    "metadata": doc.get('metadata', {}),
                    "relevance_score": score
                }
                for doc, score in reranked
            ],
            "query_variations": queries
        }
    
    def expand_query(self, query: str) -> List[str]:
        """Multi-query + HyDE"""
        # Multi-query
        variations = self.multiquery(query, num=2)
        
        # HyDE
        hyde_doc = self.hyde(query)
        
        return [query] + variations + [hyde_doc]
    
    def multiquery(self, query: str, num: int = 2) -> List[str]:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"Generate {num} variations of: {query}"
            }],
            temperature=0.7
        )
        variations = response.choices[0].message.content.strip().split("\n")
        return [v.strip("- 1234567890.") for v in variations if v.strip()][:num]
    
    def hyde(self, query: str) -> str:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"Write a passage that answers: {query}"
            }],
            temperature=0.3,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    
    def rerank(self, query: str, documents: List[Dict], top_n: int = 5):
        doc_texts = [doc['text'] for doc in documents]
        
        results = co.rerank(
            model="rerank-multilingual-v3.0",
            query=query,
            documents=doc_texts,
            top_n=top_n
        )
        
        reranked = [
            (documents[result.index], result.relevance_score)
            for result in results.results
        ]
        
        return reranked
    
    def generate_answer(self, query: str, context: str) -> str:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Answer based only on the provided context. Include source references."
                },
                {
                    "role": "user",
                    "content": f"Context:\n{context}\n\nQuestion: {query}"
                }
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    
    def get_embedding(self, text: str) -> List[float]:
        response = client.embeddings.create(
            input=text,
            model="text-embedding-3-small"
        )
        return response.data[0].embedding

# Uso
pipeline = AdvancedRAGPipeline(your_vector_store)
result = pipeline.query("How do I handle authentication errors?")

print("Answer:", result['answer'])
print("\nSources:")
for source in result['sources']:
    print(f"  [{source['relevance_score']:.2f}] {source['text']}")
```

Ejercicio: integra este pipeline en tu proyecto Docs Q&A.

**Viernes (1.5h): Evaluación de mejoras**

Crea benchmark para comparar versiones:

```python
# rag_evaluation.py
from typing import List, Dict
import json

# Test cases
TEST_QUERIES = [
    {
        "query": "How do I install the software?",
        "expected_keywords": ["installation", "setup", "requirements"],
        "expected_source": "installation_guide.md"
    },
    {
        "query": "What are the API rate limits?",
        "expected_keywords": ["rate", "limit", "requests per"],
        "expected_source": "api_docs.md"
    },
    # ... más casos
]

def evaluate_rag_system(pipeline, test_cases: List[Dict]) -> Dict:
    results = {
        "total": len(test_cases),
        "correct_sources": 0,
        "keyword_matches": 0,
        "avg_relevance": 0.0
    }
    
    for test in test_cases:
        result = pipeline.query(test["query"])
        
        # Check si el source correcto está en top 3
        sources = [s['metadata'].get('source', '') for s in result['sources'][:3]]
        if test["expected_source"] in sources:
            results["correct_sources"] += 1
        
        # Check keywords en respuesta
        answer_lower = result['answer'].lower()
        if any(kw in answer_lower for kw in test["expected_keywords"]):
            results["keyword_matches"] += 1
        
        # Avg relevance score
        if result['sources']:
            results["avg_relevance"] += result['sources'][0]['relevance_score']
    
    results["avg_relevance"] /= len(test_cases)
    
    print(f"""
RAG Evaluation Results:
-----------------------
Correct Sources: {results['correct_sources']}/{results['total']} ({results['correct_sources']/results['total']*100:.1f}%)
Keyword Matches: {results['keyword_matches']}/{results['total']} ({results['keyword_matches']/results['total']*100:.1f}%)
Avg Relevance: {results['avg_relevance']:.3f}
    """)
    
    return results

# Comparar versión básica vs avanzada
print("=== Basic RAG ===")
evaluate_rag_system(basic_pipeline, TEST_QUERIES)

print("\n=== Advanced RAG ===")
evaluate_rag_system(advanced_pipeline, TEST_QUERIES)
```

Documenta mejoras en README del proyecto.

### ✅ Checklist de dominio

- [ ] Implementaste multi-query retrieval
- [ ] Probaste HyDE (hypothetical document embeddings)
- [ ] Añadiste reranking (Cohere o cross-encoder)
- [ ] Implementaste parent-child retrieval
- [ ] Creaste pipeline RAG avanzado completo
- [ ] Evaluaste mejoras cuantitativamente
- [ ] Documentaste diferencias de calidad

---

## SEMANA 21: Proyecto 2 - Docs Q&A Production Ready

### 🎯 Objetivo
Refactorizar proyecto Docs Q&A con todas las mejoras aprendidas. Código limpio, testeado, documentado.

### 📖 Conceptos clave

**De prototipo a producción:**

❌ **Código prototipo:**
- Funciona solo en tu máquina
- Sin tests
- Configuración hardcodeada
- Sin logs
- Sin manejo de errores
- Un solo archivo de 500 líneas

✅ **Código producción:**
- Dockerizado y portable
- Tests (unit + integration)
- Config via env vars
- Logging estructurado
- Error handling robusto
- Modular y extensible
- Documentado

**Arquitectura objetivo:**
```
docs-qa-platform/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app
│   ├── config.py            # Settings
│   ├── models.py            # Pydantic schemas
│   ├── database.py          # DB connection
│   ├── ingestion/
│   │   ├── __init__.py
│   │   ├── chunking.py
│   │   ├── embedding.py
│   │   └── metadata.py
│   ├── retrieval/
│   │   ├── __init__.py
│   │   ├── vector_search.py
│   │   ├── reranking.py
│   │   └── query_enhancement.py
│   └── generation/
│       ├── __init__.py
│       └── answer_generation.py
├── tests/
│   ├── test_ingestion.py
│   ├── test_retrieval.py
│   └── test_api.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
└── README.md
```

### 📚 Recursos

**Best Practices:**
- [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices) (30min)
- [Python Project Structure](https://docs.python-guide.org/writing/structure/) (15min)
- [Testing FastAPI](https://fastapi.tiangolo.com/tutorial/testing/) (20min)

**Videos:**
- [Production FastAPI Tutorial](https://www.youtube.com/watch?v=cbASjoZZGIw) (45min)

### 🗓️ Plan semanal (6h)

**Lunes (1.5h): Arquitectura y estructura**

Crea estructura del proyecto:

```bash
mkdir docs-qa-platform
cd docs-qa-platform

# Estructura
mkdir -p app/{ingestion,retrieval,generation} tests

touch app/{__init__,main,config,models,database}.py
touch app/ingestion/{__init__,chunking,embedding,metadata}.py
touch app/retrieval/{__init__,vector_search,reranking,query_enhancement}.py
touch app/generation/{__init__,answer_generation}.py
touch tests/{__init__,test_ingestion,test_retrieval,test_api}.py
```

**config.py:**
```python
# app/config.py
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # App
    app_name: str = "Docs Q&A Platform"
    debug: bool = False
    
    # Database
    database_url: str
    
    # OpenAI
    openai_api_key: str
    openai_model: str = "gpt-4o-mini"
    embedding_model: str = "text-embedding-3-small"
    
    # Cohere (opcional)
    cohere_api_key: str | None = None
    
    # RAG Config
    chunk_size: int = 500
    chunk_overlap: int = 100
    retrieval_top_k: int = 20
    rerank_top_n: int = 5
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    return Settings()
```

**models.py:**
```python
# app/models.py
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

class DocumentUpload(BaseModel):
    filename: str
    content: str
    metadata: Optional[Dict] = None

class QueryRequest(BaseModel):
    query: str = Field(..., min_length=3, max_length=500)
    filters: Optional[Dict] = None
    top_k: int = Field(default=5, ge=1, le=20)

class Source(BaseModel):
    text: str
    metadata: Dict
    relevance_score: float

class QueryResponse(BaseModel):
    answer: str
    sources: List[Source]
    query_variations: Optional[List[str]] = None
    processing_time_ms: float

class DocumentInfo(BaseModel):
    id: str
    filename: str
    chunk_count: int
    ingested_at: datetime
    metadata: Dict
```

Ejercicio: crea `.env.example` con todas las variables necesarias.

**Martes (1.5h): Módulo de ingestion**

**chunking.py:**
```python
# app/ingestion/chunking.py
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
import tiktoken
from app.config import get_settings

settings = get_settings()

def count_tokens(text: str, model: str = "gpt-4o-mini") -> int:
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

class DocumentChunker:
    def __init__(
        self,
        chunk_size: int = None,
        chunk_overlap: int = None
    ):
        self.chunk_size = chunk_size or settings.chunk_size
        self.chunk_overlap = chunk_overlap or settings.chunk_overlap
        
        self.splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n", "\n", ". ", " ", ""],
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=count_tokens
        )
    
    def chunk_document(self, text: str) -> List[str]:
        """Split document into chunks"""
        chunks = self.splitter.split_text(text)
        return chunks
    
    def chunk_with_metadata(
        self,
        text: str,
        source_metadata: dict
    ) -> List[dict]:
        """Chunk and enrich with metadata"""
        chunks = self.chunk_document(text)
        
        enriched = []
        for i, chunk in enumerate(chunks):
            chunk_meta = {
                **source_metadata,
                "chunk_index": i,
                "total_chunks": len(chunks),
                "char_count": len(chunk),
                "token_count": count_tokens(chunk)
            }
            
            enriched.append({
                "text": chunk,
                "metadata": chunk_meta
            })
        
        return enriched
```

**embedding.py:**
```python
# app/ingestion/embedding.py
from openai import OpenAI
from typing import List
import numpy as np
from app.config import get_settings
import logging

logger = logging.getLogger(__name__)
settings = get_settings()

class EmbeddingGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.embedding_model
    
    def generate(self, text: str) -> List[float]:
        """Generate embedding for single text"""
        try:
            response = self.client.embeddings.create(
                input=text,
                model=self.model
            )
            return response.data[0].embedding
        except Exception as e:
            logger.error(f"Error generating embedding: {e}")
            raise
    
    def generate_batch(self, texts: List[str], batch_size: int = 100) -> List[List[float]]:
        """Generate embeddings in batches"""
        embeddings = []
        
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i+batch_size]
            
            try:
                response = self.client.embeddings.create(
                    input=batch,
                    model=self.model
                )
                batch_embeddings = [item.embedding for item in response.data]
                embeddings.extend(batch_embeddings)
                
                logger.info(f"Generated embeddings for batch {i//batch_size + 1}")
            
            except Exception as e:
                logger.error(f"Error in batch {i//batch_size + 1}: {e}")
                raise
        
        return embeddings
```

Ejercicio: añade rate limiting y retry logic a `generate_batch`.

**Miércoles (1.5h): Módulo de retrieval**

**vector_search.py:**
```python
# app/retrieval/vector_search.py
from sqlalchemy.orm import Session
from typing import List, Dict, Optional
from app.database import DocumentChunk
import logging

logger = logging.getLogger(__name__)

class VectorSearcher:
    def __init__(self, db: Session):
        self.db = db
    
    def search(
        self,
        query_embedding: List[float],
        top_k: int = 20,
        filters: Optional[Dict] = None
    ) -> List[Dict]:
        """Vector similarity search with optional metadata filters"""
        
        query = self.db.query(DocumentChunk).order_by(
            DocumentChunk.embedding.cosine_distance(query_embedding)
        )
        
        # Apply filters
        if filters:
            if "source" in filters:
                query = query.filter(DocumentChunk.source == filters["source"])
            if "document_type" in filters:
                query = query.filter(DocumentChunk.document_type == filters["document_type"])
            # Add more filters as needed
        
        results = query.limit(top_k).all()
        
        return [
            {
                "id": r.id,
                "text": r.text,
                "metadata": {
                    "source": r.source,
                    "page_number": r.page_number,
                    "section": r.section,
                    "document_type": r.document_type
                }
            }
            for r in results
        ]
```

**reranking.py:**
```python
# app/retrieval/reranking.py
from typing import List, Dict, Tuple
import cohere
from app.config import get_settings
import logging

logger = logging.getLogger(__name__)
settings = get_settings()

class Reranker:
    def __init__(self):
        if settings.cohere_api_key:
            self.client = cohere.Client(settings.cohere_api_key)
            self.enabled = True
        else:
            logger.warning("Cohere API key not set. Reranking disabled.")
            self.enabled = False
    
    def rerank(
        self,
        query: str,
        documents: List[Dict],
        top_n: int = 5
    ) -> List[Tuple[Dict, float]]:
        """Rerank documents by relevance"""
        
        if not self.enabled or len(documents) <= top_n:
            # Return as-is with dummy scores
            return [(doc, 1.0) for doc in documents[:top_n]]
        
        doc_texts = [doc['text'] for doc in documents]
        
        try:
            results = self.client.rerank(
                model="rerank-multilingual-v3.0",
                query=query,
                documents=doc_texts,
                top_n=top_n,
                return_documents=False
            )
            
            reranked = [
                (documents[result.index], result.relevance_score)
                for result in results.results
            ]
            
            logger.info(f"Reranked {len(documents)} docs to top {top_n}")
            return reranked
        
        except Exception as e:
            logger.error(f"Reranking failed: {e}. Returning original order.")
            return [(doc, 1.0) for doc in documents[:top_n]]
```

**query_enhancement.py:**
```python
# app/retrieval/query_enhancement.py
from openai import OpenAI
from typing import List
from app.config import get_settings
import logging

logger = logging.getLogger(__name__)
settings = get_settings()

class QueryEnhancer:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)
    
    def expand_multiquery(self, query: str, num_variations: int = 2) -> List[str]:
        """Generate query variations"""
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{
                    "role": "user",
                    "content": f"Generate {num_variations} different phrasings of: {query}"
                }],
                temperature=0.7,
                max_tokens=100
            )
            
            variations = response.choices[0].message.content.strip().split("\n")
            variations = [v.strip("- 1234567890.") for v in variations if v.strip()]
            
            return [query] + variations[:num_variations]
        
        except Exception as e:
            logger.error(f"Query expansion failed: {e}")
            return [query]
```

**Jueves (1.5h): Módulo de generation + API endpoints**

**answer_generation.py:**
```python
# app/generation/answer_generation.py
from openai import OpenAI
from typing import List, Dict
from app.config import get_settings
import logging

logger = logging.getLogger(__name__)
settings = get_settings()

class AnswerGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_model
    
    def generate(
        self,
        query: str,
        context_docs: List[Dict],
        include_citations: bool = True
    ) -> str:
        """Generate answer from context"""
        
        # Build context
        context_parts = []
        for i, doc in enumerate(context_docs):
            source = doc['metadata'].get('source', 'Unknown')
            context_parts.append(f"[{i+1}] Source: {source}\n{doc['text']}")
        
        context = "\n\n".join(context_parts)
        
        # System prompt
        system_prompt = """You are a helpful assistant that answers questions based on provided documentation.

Guidelines:
- Answer ONLY based on the provided context
- If the context doesn't contain the answer, say so
- Include source references [1], [2], etc.
- Be concise but complete"""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
                ],
                temperature=0.3,
                max_tokens=500
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            logger.error(f"Answer generation failed: {e}")
            raise
```

**main.py (API endpoints):**
```python
# app/main.py
from fastapi import FastAPI, HTTPException, Depends, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import time
import logging

from app.config import get_settings
from app.models import *
from app.database import get_db
from app.ingestion.chunking import DocumentChunker
from app.ingestion.embedding import EmbeddingGenerator
from app.retrieval.vector_search import VectorSearcher
from app.retrieval.reranking import Reranker
from app.retrieval.query_enhancement import QueryEnhancer
from app.generation.answer_generation import AnswerGenerator

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

settings = get_settings()
app = FastAPI(title=settings.app_name)

# Initialize components
chunker = DocumentChunker()
embedder = EmbeddingGenerator()
reranker = Reranker()
query_enhancer = QueryEnhancer()
answer_gen = AnswerGenerator()

@app.get("/")
def root():
    return {"message": "Docs Q&A Platform API", "version": "2.0"}

@app.post("/documents/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """Upload and process document"""
    try:
        # Read file
        content = await file.read()
        text = content.decode("utf-8")
        
        # Chunk
        chunks_with_meta = chunker.chunk_with_metadata(
            text,
            {"source": file.filename, "document_type": "manual"}
        )
        
        # Embed
        texts = [c['text'] for c in chunks_with_meta]
        embeddings = embedder.generate_batch(texts)
        
        # Store in DB (implementation depends on your DB model)
        # ...
        
        logger.info(f"Uploaded {file.filename}: {len(chunks_with_meta)} chunks")
        
        return {
            "filename": file.filename,
            "chunks_created": len(chunks_with_meta),
            "status": "success"
        }
    
    except Exception as e:
        logger.error(f"Upload failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query", response_model=QueryResponse)
def query_documents(
    request: QueryRequest,
    db: Session = Depends(get_db)
):
    """Query documents with advanced RAG"""
    start_time = time.time()
    
    try:
        # 1. Query enhancement
        queries = query_enhancer.expand_multiquery(request.query)
        logger.info(f"Enhanced query: {len(queries)} variations")
        
        # 2. Multi-query retrieval
        searcher = VectorSearcher(db)
        all_results = []
        
        for q in queries:
            q_embedding = embedder.generate(q)
            results = searcher.search(
                q_embedding,
                top_k=settings.retrieval_top_k,
                filters=request.filters
            )
            all_results.extend(results)
        
        # Deduplicate
        unique_results = {r['id']: r for r in all_results}.values()
        
        # 3. Reranking
        reranked = reranker.rerank(
            request.query,
            list(unique_results),
            top_n=request.top_k
        )
        
        # 4. Generate answer
        top_docs = [doc for doc, score in reranked]
        answer = answer_gen.generate(request.query, top_docs)
        
        # Build response
        processing_time = (time.time() - start_time) * 1000
        
        return QueryResponse(
            answer=answer,
            sources=[
                Source(
                    text=doc['text'][:300],
                    metadata=doc['metadata'],
                    relevance_score=score
                )
                for doc, score in reranked
            ],
            query_variations=queries,
            processing_time_ms=processing_time
        )
    
    except Exception as e:
        logger.error(f"Query failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "healthy"}
```

**Viernes (1.5h): Tests + Docker**

**test_api.py:**
```python
# tests/test_api.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_query_endpoint():
    response = client.post(
        "/query",
        json={
            "query": "How do I install?",
            "top_k": 3
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "sources" in data
    assert len(data["sources"]) <= 3
```

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY app/ ./app/

# Expose port
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  db:
    image: ankane/pgvector:latest
    environment:
      POSTGRES_DB: docsqa
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
  
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://user:password@db:5432/docsqa
      OPENAI_API_KEY: ${OPENAI_API_KEY}
      COHERE_API_KEY: ${COHERE_API_KEY}
    depends_on:
      - db

volumes:
  pgdata:
```

Ejercicio: ejecuta tests con `pytest` y levanta el stack con `docker-compose up`.

### ✅ Checklist de dominio

- [ ] Refactorizaste proyecto con arquitectura modular
- [ ] Añadiste configuración por environment variables
- [ ] Implementaste logging estructurado
- [ ] Escribiste tests (unit + integration)
- [ ] Dockerizaste la aplicación
- [ ] Documentaste API endpoints
- [ ] Todo funciona end-to-end en Docker

---

## FASE 3: PRODUCCIÓN Y AGENTES (Semanas 22-33)

### Resumen Fase 3

En las próximas 12 semanas aprenderás:
- **Observability**: Langfuse, tracing, evals
- **Safety**: Sentry, rate limiting, guardrails
- **AI Agents**: tools, memory, planning con LangGraph
- **Optimization**: caching, async, streaming
- **Proyecto 3**: Production Support Bot

---

## SEMANA 22: Observability con Langfuse

### 🎯 Objetivo
Instrumentar tu RAG pipeline con tracing y observability.

### 📖 Conceptos clave

**¿Por qué observability?**

Sin observability:
- ❓ "¿Por qué esta respuesta es mala?"
- ❓ "¿Cuánto cuesta cada query?"
- ❓ "¿Dónde está el bottleneck?"
- ❓ "¿Cómo ha cambiado la calidad?"

Con observability:
- ✅ Ves cada paso del pipeline (query → retrieval → rerank → generation)
- ✅ Tracking de tokens, latencia, costos
- ✅ Comparar versiones de prompts
- ✅ Detectar degradación de calidad

**Langfuse:**
Open-source LLM observability platform.

**Features clave:**
- **Tracing**: ver cascada de llamadas LLM
- **Prompts**: versioning y A/B testing
- **Evaluations**: medir calidad
- **Datasets**: test cases reutilizables
- **Analytics**: costos, latencia, scores

### 📚 Recursos

**Documentación:**
- [Langfuse Docs](https://langfuse.com/docs) (30min)
- [Langfuse + LangChain Integration](https://langfuse.com/docs/integrations/langchain) (20min)

**Videos:**
- [Langfuse Tutorial](https://www.youtube.com/watch?v=3_x8u1fJIqc) (25min)

**GitHub:**
- [Langfuse Examples](https://github.com/langfuse/langfuse-docs/tree/main/cookbook)

### 🗓️ Plan semanal (6h)

**Lunes (1.5h): Setup Langfuse**

**Opción 1: Cloud (más fácil)**
1. Regístrate en [https://cloud.langfuse.com](https://cloud.langfuse.com)
2. Crea proyecto
3. Copia API keys

**Opción 2: Self-hosted**
```yaml
# docker-compose.langfuse.yml
version: '3.8'

services:
  langfuse-server:
    image: langfuse/langfuse:latest
    ports:
      - "3000:3000"
    environment:
      DATABASE_URL: postgresql://user:password@db:5432/langfuse
      NEXTAUTH_URL: http://localhost:3000
      NEXTAUTH_SECRET: your-secret-key-here
    depends_on:
      - db
```

**Instalar SDK:**
```bash
pip install langfuse
```

**Configuración básica:**
```python
# app/observability.py
from langfuse import Langfuse
from app.config import get_settings
import os

settings = get_settings()

langfuse = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")
)

# Test connection
def test_connection():
    trace = langfuse.trace(name="test")
    trace.span(name="test-span")
    langfuse.flush()
    print("✅ Langfuse connected")

if __name__ == "__main__":
    test_connection()
```

Añade a `.env`:
```
LANGFUSE_PUBLIC_KEY=pk-...
LANGFUSE_SECRET_KEY=sk-...
LANGFUSE_HOST=https://cloud.langfuse.com
```

**Martes (1.5h): Tracing básico**

```python
# app/observability.py (extended)
from functools import wraps
from langfuse.decorators import observe, langfuse_context
import time

@observe()
def generate_embedding(text: str) -> list[float]:
    """Wrapper for embedding generation with tracing"""
    from app.ingestion.embedding import EmbeddingGenerator
    embedder = EmbeddingGenerator()
    return embedder.generate(text)

@observe()
def vector_search(query_embedding: list[float], top_k: int = 20):
    """Wrapper for vector search with tracing"""
    from app.retrieval.vector_search import VectorSearcher
    from app.database import get_db
    
    db = next(get_db())
    searcher = VectorSearcher(db)
    return searcher.search(query_embedding, top_k=top_k)

@observe()
def rerank_documents(query: str, documents: list[dict], top_n: int = 5):
    """Wrapper for reranking with tracing"""
    from app.retrieval.reranking import Reranker
    reranker = Reranker()
    return reranker.rerank(query, documents, top_n=top_n)

@observe()
def generate_answer(query: str, context_docs: list[dict]) -> str:
    """Wrapper for answer generation with tracing"""
    from app.generation.answer_generation import AnswerGenerator
    generator = AnswerGenerator()
    return generator.generate(query, context_docs)

# Main RAG pipeline con tracing completo
@observe()
def rag_pipeline(query: str, top_k: int = 5):
    """End-to-end RAG with full observability"""
    
    # 1. Generate embedding
    query_embedding = generate_embedding(query)
    langfuse_context.update_current_observation(
        metadata={"query_length": len(query)}
    )
    
    # 2. Vector search
    candidates = vector_search(query_embedding, top_k=20)
    langfuse_context.update_current_observation(
        metadata={"candidates_found": len(candidates)}
    )
    
    # 3. Rerank
    reranked = rerank_documents(query, candidates, top_n=top_k)
    langfuse_context.update_current_observation(
        metadata={"reranked_count": len(reranked)}
    )
    
    # 4. Generate answer
    top_docs = [doc for doc, score in reranked]
    answer = generate_answer(query, top_docs)
    
    # Add scores
    langfuse_context.score_current_observation(
        name="relevance",
        value=reranked[0][1] if reranked else 0.0
    )
    
    return {
        "answer": answer,
        "sources": top_docs,
        "relevance_scores": [score for _, score in reranked]
    }
```

**Actualizar endpoint:**
```python
# app/main.py
from app.observability import rag_pipeline

@app.post("/query", response_model=QueryResponse)
@observe()  # Añadir decorator
def query_documents(request: QueryRequest):
    result = rag_pipeline(request.query, top_k=request.top_k)
    # ... rest of the code
```

Ejercicio: ejecuta queries y revisa traces en Langfuse UI.

**Miércoles (1.5h): Prompt management**

```python
# app/generation/answer_generation.py (updated)
from langfuse import Langfuse

langfuse = Langfuse()

class AnswerGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_model
        
        # Fetch prompt from Langfuse
        self.system_prompt = self.get_prompt("rag-system-prompt")
    
    def get_prompt(self, name: str, version: int = None) -> str:
        """Fetch prompt from Langfuse"""
        try:
            prompt = langfuse.get_prompt(name, version=version)
            return prompt.prompt
        except:
            # Fallback
            return self.default_system_prompt()
    
    def default_system_prompt(self) -> str:
        return """You are a helpful assistant..."""
    
    @observe()
    def generate(self, query: str, context_docs: list[dict]) -> str:
        # Build context
        context = self.build_context(context_docs)
        
        # Use managed prompt
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
            ],
            temperature=0.3
        )
        
        answer = response.choices[0].message.content
        
        # Log to Langfuse
        langfuse_context.update_current_observation(
            input={"query": query, "context_length": len(context)},
            output={"answer": answer},
            usage={
                "input_tokens": response.usage.prompt_tokens,
                "output_tokens": response.usage.completion_tokens,
                "total_cost": self.calculate_cost(response.usage)
            }
        )
        
        return answer
    
    def calculate_cost(self, usage) -> float:
        # Prices for gpt-4o-mini (example, update as needed)
        input_cost = (usage.prompt_tokens / 1000) * 0.00015
        output_cost = (usage.completion_tokens / 1000) * 0.0006
        return input_cost + output_cost
```

**En Langfuse UI:**
1. Ve a "Prompts"
2. Crea prompt "rag-system-prompt"
3. Añade versiones
4. Compara performance entre versiones

Ejercicio: crea 2 versiones del system prompt y mide cuál funciona mejor.

**Jueves (1.5h): Evaluations**

```python
# app/evaluations.py
from langfuse import Langfuse
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)
langfuse = Langfuse()

def create_evaluation_dataset():
    """Create test dataset in Langfuse"""
    dataset_name = "rag-qa-test"
    
    test_cases = [
        {
            "input": {"query": "How do I install the software?"},
            "expected_output": {
                "keywords": ["installation", "setup", "requirements"],
                "source_file": "installation_guide.md"
            }
        },
        {
            "input": {"query": "What are the API rate limits?"},
            "expected_output": {
                "keywords": ["rate", "limit", "requests"],
                "source_file": "api_docs.md"
            }
        },
        # Add more test cases
    ]
    
    # Create dataset
    dataset = langfuse.create_dataset(name=dataset_name)
    
    for case in test_cases:
        dataset.create_item(
            input=case["input"],
            expected_output=case["expected_output"]
        )
    
    logger.info(f"Created dataset with {len(test_cases)} cases")
    return dataset

def evaluate_rag_quality(trace_id: str, expected_keywords: List[str], actual_answer: str) -> float:
    """Evaluate if answer contains expected keywords"""
    answer_lower = actual_answer.lower()
    matches = sum(1 for kw in expected_keywords if kw.lower() in answer_lower)
    score = matches / len(expected_keywords) if expected_keywords else 0.0
    
    # Log score to Langfuse
    langfuse.score(
        trace_id=trace_id,
        name="keyword_coverage",
        value=score,
        comment=f"Matched {matches}/{len(expected_keywords)} keywords"
    )
    
    return score

def run_evaluation_suite():
    """Run evaluation on dataset"""
    dataset = langfuse.get_dataset("rag-qa-test")
    
    results = []
    for item in dataset.items:
        query = item.input["query"]
        expected = item.expected_output
        
        # Run RAG pipeline
        from app.observability import rag_pipeline
        result = rag_pipeline(query)
        
        # Evaluate
        score = evaluate_rag_quality(
            trace_id=langfuse_context.get_current_trace_id(),
            expected_keywords=expected["keywords"],
            actual_answer=result["answer"]
        )
        
        results.append({
            "query": query,
            "score": score,
            "answer": result["answer"][:100]
        })
    
    # Summary
    avg_score = sum(r["score"] for r in results) / len(results)
    logger.info(f"Evaluation complete. Average score: {avg_score:.2f}")
    
    return results

# CLI command
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "create-dataset":
        create_evaluation_dataset()
    elif len(sys.argv) > 1 and sys.argv[1] == "evaluate":
        run_evaluation_suite()
    else:
        print("Usage: python evaluations.py [create-dataset|evaluate]")
```

Ejercicio: crea dataset con 10 test cases y ejecuta evaluación.

**Viernes (1.5h): User feedback loop**

```python
# app/models.py (add)
class FeedbackRequest(BaseModel):
    trace_id: str
    score: float = Field(..., ge=0, le=1)
    comment: Optional[str] = None

# app/main.py (add endpoint)
@app.post("/feedback")
def submit_feedback(feedback: FeedbackRequest):
    """Collect user feedback for traces"""
    try:
        langfuse.score(
            trace_id=feedback.trace_id,
            name="user_feedback",
            value=feedback.score,
            comment=feedback.comment
        )
        
        logger.info(f"Feedback received for trace {feedback.trace_id}: {feedback.score}")
        return {"status": "success"}
    
    except Exception as e:
        logger.error(f"Feedback submission failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Frontend (ejemplo simple)
@app.get("/query-ui")
def query_ui():
    return HTMLResponse("""
    <html>
    <body>
        <h1>Docs Q&A</h1>
        <input type="text" id="query" placeholder="Ask a question...">
        <button onclick="ask()">Ask</button>
        <div id="answer"></div>
        <div id="feedback" style="display:none">
            <p>Was this helpful?</p>
            <button onclick="sendFeedback(1)">👍 Yes</button>
            <button onclick="sendFeedback(0)">👎 No</button>
        </div>
        
        <script>
        let currentTraceId = null;
        
        async function ask() {
            const query = document.getElementById('query').value;
            const response = await fetch('/query', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({query: query, top_k: 3})
            });
            const data = await response.json();
            
            document.getElementById('answer').innerHTML = data.answer;
            document.getElementById('feedback').style.display = 'block';
            
            // Get trace ID from response headers (you'd need to add this)
            currentTraceId = response.headers.get('X-Trace-ID');
        }
        
        async function sendFeedback(score) {
            await fetch('/feedback', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    trace_id: currentTraceId,
                    score: score,
                    comment: ''
                })
            });
            alert('Thank you for your feedback!');
        }
        </script>
    </body>
    </html>
    """)
```

Ejercicio: añade botones de feedback y revisa scores en Langfuse.

### ✅ Checklist de dominio

- [ ] Configuraste Langfuse (cloud o self-hosted)
- [ ] Añadiste tracing a todo el pipeline RAG
- [ ] Implementaste prompt versioning
- [ ] Creaste evaluation dataset
- [ ] Configuraste user feedback loop
- [ ] Analizaste traces en Langfuse UI
- [ ] Detectaste bottleneck de latencia

---

## SEMANA 23: Safety y Error Handling

### 🎯 Objetivo
Hacer tu sistema robusto: rate limiting, input validation, error monitoring con Sentry.

### 📖 Conceptos clave

**Producción = Murphy's Law:**
Todo lo que puede fallar, fallará.

**Categorías de errores:**

1. **User errors**: input inválido, queries maliciosas
2. **System errors**: API down, DB timeout, OOM
3. **LLM errors**: rate limits, hallucinations, refusals
4. **Security**: injection attacks, PII leakage

**Defenses:**

- **Input validation**: Pydantic schemas
- **Rate limiting**: por usuario/IP
- **Guardrails**: detectar/bloquear contenido problemático
- **Error monitoring**: Sentry
- **Graceful degradation**: fallbacks
- **Circuit breakers**: detener cascading failures

### 📚 Recursos

**Artículos:**
- [LLM Security Best Practices](https://www.lakera.ai/blog/llm-security-guide) (20min)
- [Prompt Injection Attacks](https://simonwillison.net/2023/Apr/14/worst-that-can-happen/) (15min)
- [Rate Limiting Strategies](https://www.nginx.com/blog/rate-limiting-nginx/) (10min)

**Docs:**
- [Sentry Python](https://docs.sentry.io/platforms/python/) (15min)
- [FastAPI Middleware](https://fastapi.tiangolo.com/tutorial/middleware/) (20min)

**Tools:**
- [Guardrails AI](https://www.guardrailsai.com/) - output validation
- [LLM Guard](https://llm-guard.com/) - input/output sanitization

### 🗓️ Plan semanal (6h)

**Lunes (1.5h): Input validation y sanitization**

```python
# app/security/validation.py
from pydantic import BaseModel, Field, validator
from typing import Optional
import re

class QueryRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=3,
        max_length=1000,
        description="User query"
    )
    filters: Optional[dict] = None
    top_k: int = Field(default=5, ge=1, le=20)
    
    @validator('query')
    def validate_query(cls, v):
        # Check for empty/whitespace
        if not v.strip():
            raise ValueError("Query cannot be empty")
        
        # Check for potential injection
        suspicious_patterns = [
            r'<script',
            r'javascript:',
            r'onerror=',
            r'<!--',
            r'DROP TABLE',
            r'DELETE FROM',
            r'UNION SELECT'
        ]
        
        v_lower = v.lower()
        for pattern in suspicious_patterns:
            if re.search(pattern, v_lower):
                raise ValueError(f"Suspicious pattern detected: {pattern}")
        
        # Check for excessive special chars (possible obfuscation)
        special_char_ratio = sum(not c.isalnum() and not c.isspace() for c in v) / len(v)
        if special_char_ratio > 0.3:
            raise ValueError("Too many special characters")
        
        return v.strip()
    
    @validator('filters')
    def validate_filters(cls, v):
        if v is None:
            return v
        
        # Whitelist allowed filter keys
        allowed_keys = {'source', 'document_type', 'section', 'date_from', 'date_to'}
        if not set(v.keys()).issubset(allowed_keys):
            raise ValueError(f"Invalid filter keys. Allowed: {allowed_keys}")
        
        return v

# Test
try:
    req = QueryRequest(query="<script>alert('xss')</script>")
except ValueError as e:
    print(f"❌ Blocked: {e}")

try:
    req = QueryRequest(query="How do I install?")
    print(f"✅ Valid: {req.query}")
except ValueError as e:
    print(f"❌ Error: {e}")
```

**Sanitize output:**
```python
# app/security/sanitization.py
import re
from typing import Dict, List

class OutputSanitizer:
    """Remove PII and sensitive data from responses"""
    
    # Patterns
    EMAIL_PATTERN = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    PHONE_PATTERN = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    SSN_PATTERN = r'\b\d{3}-\d{2}-\d{4}\b'
    CREDIT_CARD_PATTERN = r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'
    
    @staticmethod
    def sanitize(text: str) -> str:
        """Remove sensitive patterns"""
        # Email
        text = re.sub(OutputSanitizer.EMAIL_PATTERN, '[EMAIL]', text)
        
        # Phone
        text = re.sub(OutputSanitizer.PHONE_PATTERN, '[PHONE]', text)
        
        # SSN
        text = re.sub(OutputSanitizer.SSN_PATTERN, '[SSN]', text)
        
        # Credit card
        text = re.sub(OutputSanitizer.CREDIT_CARD_PATTERN, '[CARD]', text)
        
        return text
    
    @staticmethod
    def sanitize_sources(sources: List[Dict]) -> List[Dict]:
        """Sanitize source documents"""
        sanitized = []
        for source in sources:
            source['text'] = OutputSanitizer.sanitize(source['text'])
            sanitized.append(source)
        return sanitized

# Usage in answer generation
from app.security.sanitization import OutputSanitizer

class AnswerGenerator:
    # ... existing code
    
    def generate(self, query: str, context_docs: list[dict]) -> str:
        # Generate answer
        answer = self._call_llm(query, context_docs)
        
        # Sanitize before returning
        sanitized_answer = OutputSanitizer.sanitize(answer)
        
        return sanitized_answer
```

Ejercicio: añade detector de PII a todo el pipeline.

**Martes (1.5h): Rate limiting**

```python
# app/middleware/rate_limiting.py
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from collections import defaultdict
from datetime import datetime, timedelta
import time

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, calls: int = 10, period: int = 60):
        super().__init__(app)
        self.calls = calls  # Max calls
        self.period = period  # Time window (seconds)
        self.requests = defaultdict(list)  # IP -> [timestamps]
    
    async def dispatch(self, request: Request, call_next):
        # Get client IP
        client_ip = request.client.host
        
        # Clean old entries
        self.cleanup_old_requests(client_ip)
        
        # Check rate limit
        if len(self.requests[client_ip]) >= self.calls:
            return JSONResponse(
                status_code=429,
                content={
                    "error": "Rate limit exceeded",
                    "retry_after": self.period
                },
                headers={"Retry-After": str(self.period)}
            )
        
        # Record request
        self.requests[client_ip].append(time.time())
        
        # Process request
        response = await call_next(request)
        return response
    
    def cleanup_old_requests(self, ip: str):
        """Remove requests outside the time window"""
        cutoff = time.time() - self.period
        self.requests[ip] = [
            ts for ts in self.requests[ip]
            if ts > cutoff
        ]

# Add to FastAPI app
# app/main.py
from app.middleware.rate_limiting import RateLimitMiddleware

app.add_middleware(
    RateLimitMiddleware,
    calls=10,  # 10 requests
    period=60  # per minute
)
```

**Token bucket con Redis (más escalable):**
```python
# app/middleware/rate_limiting_redis.py
import redis
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import time

class RedisRateLimiter(BaseHTTPMiddleware):
    def __init__(self, app, redis_url: str, calls: int = 10, period: int = 60):
        super().__init__(app)
        self.redis = redis.from_url(redis_url)
        self.calls = calls
        self.period = period
    
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        key = f"rate_limit:{client_ip}"
        
        # Get current count
        count = self.redis.get(key)
        
        if count is None:
            # First request, initialize
            self.redis.setex(key, self.period, 1)
        elif int(count) >= self.calls:
            # Limit exceeded
            ttl = self.redis.ttl(key)
            return JSONResponse(
                status_code=429,
                content={"error": "Rate limit exceeded", "retry_after": ttl}
            )
        else:
            # Increment
            self.redis.incr(key)
        
        response = await call_next(request)
        return response
```

Ejercicio: implementa rate limiting por endpoint y por usuario autenticado.

**Miércoles (1.5h): Sentry error monitoring**

```bash
pip install sentry-sdk[fastapi]
```

```python
# app/monitoring/sentry_config.py
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from app.config import get_settings
import logging

settings = get_settings()
logger = logging.getLogger(__name__)

def init_sentry():
    """Initialize Sentry monitoring"""
    sentry_sdk.init(
        dsn=settings.sentry_dsn,  # Add to config
        environment=settings.environment,  # "production", "staging", etc.
        integrations=[
            FastApiIntegration(),
            SqlalchemyIntegration(),
        ],
        traces_sample_rate=0.1,  # 10% of transactions
        profiles_sample_rate=0.1,
        before_send=filter_sensitive_data,
    )
    logger.info("Sentry initialized")

def filter_sensitive_data(event, hint):
    """Remove PII from error reports"""
    # Remove query parameters
    if 'request' in event:
        if 'query_string' in event['request']:
            event['request']['query_string'] = '[FILTERED]'
        
        # Remove sensitive headers
        if 'headers' in event['request']:
            sensitive_headers = ['Authorization', 'Cookie', 'X-API-Key']
            for header in sensitive_headers:
                if header in event['request']['headers']:
                    event['request']['headers'][header] = '[FILTERED]'
    
    return event

# app/main.py
from app.monitoring.sentry_config import init_sentry

# Initialize at startup
@app.on_event("startup")
async def startup():
    init_sentry()
    logger.info("Application started")
```

**Custom error tracking:**
```python
# app/errors.py
from sentry_sdk import capture_exception, capture_message, set_tag, set_context
import logging

logger = logging.getLogger(__name__)

class ErrorTracker:
    @staticmethod
    def track_exception(
        error: Exception,
        context: dict = None,
        level: str = "error"
    ):
        """Track exception with context"""
        # Add tags
        set_tag("error_type", type(error).__name__)
        
        # Add context
        if context:
            set_context("custom_context", context)
        
        # Capture
        capture_exception(error)
        logger.error(f"Exception tracked: {error}", exc_info=True)
    
    @staticmethod
    def track_warning(message: str, context: dict = None):
        """Track warning event"""
        if context:
            set_context("custom_context", context)
        
        capture_message(message, level="warning")
        logger.warning(message)

# Usage
try:
    result = risky_operation()
except Exception as e:
    ErrorTracker.track_exception(
        e,
        context={
            "user_query": query,
            "retrieval_count": len(docs),
            "endpoint": "/query"
        }
    )
    raise HTTPException(status_code=500, detail="Internal error")
```

Ejercicio: simula errores y verifica que aparecen en Sentry dashboard.

**Jueves (1.5h): Circuit breaker**

```python
# app/resilience/circuit_breaker.py
from enum import Enum
from datetime import datetime, timedelta
from typing import Callable, Any
import logging

logger = logging.getLogger(__name__)

class CircuitState(Enum):
    CLOSED = "closed"  # Normal operation
    OPEN = "open"      # Failing, reject requests
    HALF_OPEN = "half_open"  # Testing if recovered

class CircuitBreaker:
    def __init__(
        self,
        failure_threshold: int = 5,
        timeout: int = 60,
        expected_exception: Exception = Exception
    ):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.expected_exception = expected_exception
        
        self.failure_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED
    
    def call(self, func: Callable, *args, **kwargs) -> Any:
        """Execute function with circuit breaker protection"""
        
        if self.state == CircuitState.OPEN:
            if self._should_attempt_reset():
                self.state = CircuitState.HALF_OPEN
                logger.info("Circuit breaker entering HALF_OPEN state")
            else:
                raise Exception("Circuit breaker is OPEN")
        
        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        
        except self.expected_exception as e:
            self._on_failure()
            raise e
    
    def _on_success(self):
        """Reset on successful call"""
        self.failure_count = 0
        if self.state == CircuitState.HALF_OPEN:
            self.state = CircuitState.CLOSED
            logger.info("Circuit breaker CLOSED")
    
    def _on_failure(self):
        """Track failure"""
        self.failure_count += 1
        self.last_failure_time = datetime.now()
        
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN
            logger.error(f"Circuit breaker OPEN after {self.failure_count} failures")
    
    def _should_attempt_reset(self) -> bool:
        """Check if enough time has passed to retry"""
        return (
            self.last_failure_time is not None and
            datetime.now() - self.last_failure_time >= timedelta(seconds=self.timeout)
        )

# Usage
embedding_circuit = CircuitBreaker(failure_threshold=3, timeout=30)

class EmbeddingGenerator:
    def __init__(self):
        self.client = OpenAI()
        self.circuit_breaker = CircuitBreaker(failure_threshold=3, timeout=60)
    
    def generate(self, text: str) -> list[float]:
        """Generate embedding with circuit breaker"""
        try:
            return self.circuit_breaker.call(self._generate_impl, text)
        except Exception as e:
            logger.error(f"Circuit breaker prevented call: {e}")
            # Return cached embedding or raise
            raise HTTPException(
                status_code=503,
                detail="Embedding service temporarily unavailable"
            )
    
    def _generate_impl(self, text: str) -> list[float]:
        response = self.client.embeddings.create(
            input=text,
            model="text-embedding-3-small"
        )
        return response.data[0].embedding
```

Ejercicio: simula fallos de API y verifica que el circuit breaker se activa.

**Viernes (1.5h): Comprehensive error handling**

```python
# app/errors/handlers.py
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
from openai import OpenAIError
import logging

logger = logging.getLogger(__name__)

# Custom exceptions
class RAGException(Exception):
    """Base exception for RAG operations"""
    pass

class EmbeddingException(RAGException):
    """Embedding generation failed"""
    pass

class RetrievalException(RAGException):
    """Vector search failed"""
    pass

class GenerationException(RAGException):
    """Answer generation failed"""
    pass

# Exception handlers
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handle input validation errors"""
    logger.warning(f"Validation error: {exc.errors()}")
    return JSONResponse(
        status_code=422,
        content={
            "error": "Invalid input",
            "details": exc.errors()
        }
    )

@app.exception_handler(SQLAlchemyError)
async def database_exception_handler(request: Request, exc: SQLAlchemyError):
    """Handle database errors"""
    logger.error(f"Database error: {exc}")
    ErrorTracker.track_exception(exc, context={"endpoint": request.url.path})
    
    return JSONResponse(
        status_code=503,
        content={"error": "Database temporarily unavailable"}
    )

@app.exception_handler(OpenAIError)
async def openai_exception_handler(request: Request, exc: OpenAIError):
    """Handle OpenAI API errors"""
    logger.error(f"OpenAI error: {exc}")
    ErrorTracker.track_exception(exc)
    
    return JSONResponse(
        status_code=503,
        content={"error": "AI service temporarily unavailable"}
    )

@app.exception_handler(RAGException)
async def rag_exception_handler(request: Request, exc: RAGException):
    """Handle RAG pipeline errors"""
    logger.error(f"RAG error: {exc}")
    ErrorTracker.track_exception(exc)
    
    return JSONResponse(
        status_code=500,
        content={"error": "RAG pipeline error", "detail": str(exc)}
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    """Catch-all handler"""
    logger.critical(f"Unexpected error: {exc}", exc_info=True)
    ErrorTracker.track_exception(exc, context={"endpoint": request.url.path})
    
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )
```

**Health check avanzado:**
```python
# app/health.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from openai import OpenAI
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/health")
def health_check():
    """Basic health check"""
    return {"status": "healthy"}

@router.get("/health/detailed")
def detailed_health_check(db: Session = Depends(get_db)):
    """Detailed health check with dependencies"""
    health_status = {
        "status": "healthy",
        "checks": {}
    }
    
    # Check database
    try:
        db.execute("SELECT 1")
        health_status["checks"]["database"] = "ok"
    except Exception as e:
        logger.error(f"DB health check failed: {e}")
        health_status["checks"]["database"] = "error"
        health_status["status"] = "unhealthy"
    
    # Check OpenAI
    try:
        client = OpenAI()
        client.models.list()
        health_status["checks"]["openai"] = "ok"
    except Exception as e:
        logger.error(f"OpenAI health check failed: {e}")
        health_status["checks"]["openai"] = "error"
        health_status["status"] = "degraded"
    
    return health_status
```

### ✅ Checklist de dominio

- [ ] Implementaste input validation robusta
- [ ] Añadiste output sanitization (PII removal)
- [ ] Configuraste rate limiting
- [ ] Integraste Sentry error monitoring
- [ ] Implementaste circuit breakers
- [ ] Añadiste exception handlers globales
- [ ] Creaste health checks detallados
- [ ] Testeaste todos los edge cases

---

## 🤖 SEMANA 24: Fundamentos de AI Agents (15-21 Abril)

**Objetivo:** Entender qué son los AI agents, cómo funcionan, y construir tu primer agent con function calling.

### 📖 Conceptos clave

**¿Qué es un AI Agent?**
Un agent es un sistema que:
1. **Recibe** un objetivo del usuario
2. **Piensa** qué hacer (reasoning)
3. **Actúa** usando tools/functions
4. **Observa** el resultado
5. **Repite** hasta cumplir el objetivo

**ReAct Pattern (Reason + Act):**
```
User: "¿Cuál es el clima en Madrid y cuánto cuesta volar allí desde Barcelona?"

Agent reasoning: "Necesito dos cosas: clima y precio de vuelo"
Action 1: get_weather(location="Madrid")
Observation 1: "Soleado, 18°C"

Agent reasoning: "Ya tengo el clima. Ahora busco vuelos"
Action 2: search_flights(origin="Barcelona", destination="Madrid")
Observation 2: "Vuelos desde 45€"

Agent reasoning: "Ya tengo toda la información"
Final answer: "En Madrid hace sol con 18°C. Hay vuelos desde Barcelona por 45€."
```

**Function calling vs RAG:**
- **RAG**: recupera información (pasivo)
- **Agent**: ejecuta acciones (activo)

**Cuándo usar agents:**
- ✅ Tareas que requieren múltiples pasos
- ✅ Necesitas ejecutar acciones (enviar email, actualizar DB)
- ✅ Decisiones basadas en resultados previos
- ❌ Preguntas simples (usa RAG)
- ❌ Tareas críticas sin supervisión (los agents fallan)

### 📚 Recursos de estudio

**Videos:**
- [LangChain Agents Explained](https://www.youtube.com/watch?v=jSP-gSEyVeI) (15min) - explicación clara
- [Function Calling with OpenAI](https://www.youtube.com/watch?v=0lOSvOoF2to) (18min) - tutorial oficial
- [Building AI Agents from Scratch](https://www.youtube.com/watch?v=yqSW1fFqK5Y) (25min) - implementación

**Artículos:**
- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
- [ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629) - paper original
- [LangChain Agents Docs](https://python.langchain.com/docs/modules/agents/)

**Repos de referencia:**
- [openai-cookbook/examples/How_to_call_functions](https://github.com/openai/openai-cookbook)

### 🗓️ Plan día por día (6h total)

**Lunes (1.5h):** Teoría + Setup
- 0:45h: Ve los 2 primeros videos
- 0:45h: Lee OpenAI function calling guide + experimenta en playground

**Martes (1.5h):** Function calling básico
- Implementa weather tool + calculator tool
- Código abajo ↓

**Miércoles (1.5h):** ReAct loop manual
- Implementa un agent loop desde cero (sin frameworks)
- Entiende el ciclo reason→act→observe

**Jueves (1h):** LangChain agents
- Usa LangChain para simplificar
- Compara con tu implementación manual

**Viernes (1.5h):** Integración con tu proyecto
- Añade agent endpoint a Docs Q&A
- Tool: search_docs + get_weather

### 💻 Código: Tu primer agent con function calling

**1. Tools definition (OpenAI format):**
```python
# agent_tools.py
import json
import requests
from typing import List, Dict, Any

# Definición de tools en formato OpenAI
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City name, e.g. Madrid"
                    },
                    "units": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "Temperature units"
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Perform basic math operations",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Math expression to evaluate, e.g. '2 + 2 * 3'"
                    }
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_database",
            "description": "Search in the knowledge base",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query"
                    }
                },
                "required": ["query"]
            }
        }
    }
]

# Implementación de las funciones
def get_weather(location: str, units: str = "celsius") -> Dict[str, Any]:
    """
    Simula una llamada a weather API.
    En producción: usarías OpenWeatherMap API
    """
    # Datos simulados
    mock_data = {
        "madrid": {"temp": 18, "condition": "Soleado"},
        "barcelona": {"temp": 20, "condition": "Nublado"},
        "london": {"temp": 12, "condition": "Lluvioso"}
    }
    
    location_lower = location.lower()
    if location_lower in mock_data:
        data = mock_data[location_lower]
        return {
            "location": location,
            "temperature": data["temp"],
            "units": units,
            "condition": data["condition"]
        }
    
    return {"error": f"Weather data not available for {location}"}

def calculate(expression: str) -> Dict[str, Any]:
    """
    Evalúa expresiones matemáticas básicas.
    WARNING: eval() es peligroso en producción. Usa ast.literal_eval o una librería.
    """
    try:
        # Solo para demo. NO uses eval en producción
        result = eval(expression, {"__builtins__": {}}, {})
        return {
            "expression": expression,
            "result": result
        }
    except Exception as e:
        return {"error": f"Cannot evaluate: {str(e)}"}

def search_database(query: str) -> Dict[str, Any]:
    """
    Busca en tu knowledge base.
    En producción: conectarías con tu vector DB
    """
    # Mock data
    knowledge = {
        "python": "Python es un lenguaje de programación de alto nivel...",
        "fastapi": "FastAPI es un framework web moderno para Python...",
        "agents": "Los AI agents son sistemas que pueden razonar y actuar..."
    }
    
    for key, value in knowledge.items():
        if key in query.lower():
            return {
                "query": query,
                "result": value,
                "source": f"doc_{key}.md"
            }
    
    return {"query": query, "result": "No relevant information found"}

# Mapa de funciones ejecutables
available_functions = {
    "get_weather": get_weather,
    "calculate": calculate,
    "search_database": search_database
}
```

**2. Agent loop (ReAct implementation):**
```python
# agent.py
from openai import OpenAI
import json
from typing import List, Dict, Any
from agent_tools import tools, available_functions
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SimpleAgent:
    """
    Agent básico con ReAct pattern
    """
    
    def __init__(self, model: str = "gpt-4o-mini"):
        self.client = OpenAI()
        self.model = model
        self.max_iterations = 5
    
    def run(self, user_query: str) -> str:
        """
        Ejecuta el agent loop:
        1. User query
        2. LLM decides action
        3. Execute tool
        4. LLM sees result
        5. Repeat or answer
        """
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant with access to tools. "
                          "Use them when needed to answer user questions accurately."
            },
            {
                "role": "user",
                "content": user_query
            }
        ]
        
        iteration = 0
        
        while iteration < self.max_iterations:
            iteration += 1
            logger.info(f"--- Iteration {iteration} ---")
            
            # LLM call with tools
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=tools,
                tool_choice="auto"
            )
            
            response_message = response.choices[0].message
            messages.append(response_message)
            
            # Check if LLM wants to call a tool
            tool_calls = response_message.tool_calls
            
            if not tool_calls:
                # LLM has final answer
                logger.info("Agent finished reasoning")
                return response_message.content
            
            # Execute each tool call
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)
                
                logger.info(f"Calling tool: {function_name}")
                logger.info(f"Arguments: {function_args}")
                
                # Execute function
                function_to_call = available_functions[function_name]
                function_response = function_to_call(**function_args)
                
                logger.info(f"Tool response: {function_response}")
                
                # Add tool response to messages
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": function_name,
                    "content": json.dumps(function_response)
                })
        
        return "Agent exceeded maximum iterations without finding an answer."

# Usage
if __name__ == "__main__":
    agent = SimpleAgent()
    
    # Test cases
    queries = [
        "What's the weather in Madrid?",
        "Calculate 15 * 23 + 100",
        "What's the weather in Barcelona and how much is 50 + 50?",
        "Tell me about FastAPI"
    ]
    
    for query in queries:
        print(f"\n{'='*60}")
        print(f"Query: {query}")
        print(f"{'='*60}")
        answer = agent.run(query)
        print(f"Answer: {answer}\n")
```

**3. FastAPI endpoint:**
```python
# main.py - añade esto a tu proyecto
from fastapi import APIRouter
from pydantic import BaseModel
from agent import SimpleAgent

router = APIRouter(prefix="/agent", tags=["agent"])
agent = SimpleAgent()

class AgentQuery(BaseModel):
    question: str

@router.post("/ask")
def ask_agent(query: AgentQuery):
    """
    Agent endpoint que puede usar tools
    """
    try:
        answer = agent.run(query.question)
        return {
            "question": query.question,
            "answer": answer
        }
    except Exception as e:
        logger.error(f"Agent error: {e}")
        return {
            "error": str(e)
        }
```

**Testing:**
```bash
curl -X POST http://localhost:8000/agent/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the weather in Madrid and calculate 2+2?"}'
```

### 🧪 Ejercicios prácticos

1. **Tool nuevo:** Añade una función `get_current_time(timezone: str)` que devuelva la hora actual en diferentes zonas horarias.

2. **Error handling:** Modifica el agent para manejar errores de tools gracefully (si un tool falla, el agent debe intentar otra estrategia).

3. **Agent con memoria:** Extiende el agent para recordar interacciones previas del usuario.

4. **Multi-step planning:** Haz que el agent responda a: "Busca información sobre Python, luego calcula cuántos días hay en 3 semanas, y dame el clima de ambas ciudades mencionadas en el documento."

### ✅ Checklist de dominio

- [ ] Entiendes qué es function calling
- [ ] Implementaste tools en formato OpenAI
- [ ] Construiste un agent loop desde cero (ReAct)
- [ ] Usaste LangChain agents y comparaste
- [ ] Añadiste agent endpoint a tu API
- [ ] Manejaste errores de tools
- [ ] Testeaste queries multi-step

---

## 🔗 SEMANA 25: LangGraph - Workflows Complejos (22-28 Abril)

**Objetivo:** Dominar LangGraph para construir agents con workflows complejos, estados persistentes y routing condicional.

### 📖 Conceptos clave

**¿Por qué LangGraph?**
LangChain agents son buenos para tareas simples, pero tienen limitaciones:
- ❌ Difíciles de debuguear
- ❌ No control fino del flujo
- ❌ Estado implícito (no explícito)
- ❌ Hard de escalar

**LangGraph resuelve esto con:**
- ✅ **Grafos explícitos** de estados
- ✅ **Control total** del flujo
- ✅ **Estado tipado** y persistente
- ✅ **Checkpointing** (reanudar workflows)
- ✅ **Human-in-the-loop** fácil

**Conceptos clave:**
1. **Nodes**: funciones que procesan el estado
2. **Edges**: conexiones entre nodes
3. **State**: el objeto que pasa entre nodes
4. **Conditional edges**: routing basado en el estado
5. **Checkpointer**: guarda estado entre ejecuciones

**Ejemplo de flujo:**
```
User input → Classifier → [Route A o Route B] → Tools → Response
```

### 📚 Recursos de estudio

**Videos:**
- [LangGraph Tutorial - Build Complex Agents](https://www.youtube.com/watch?v=9BPCV5TYPmg) (30min)
- [LangGraph vs LangChain Agents](https://www.youtube.com/watch?v=bIjMGD8CZfk) (12min)
- [Building a Support Bot with LangGraph](https://www.youtube.com/watch?v=hvAPnpSfSGo) (35min)

**Documentación:**
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
- [LangGraph Quickstart](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
- [LangGraph Examples](https://github.com/langchain-ai/langgraph/tree/main/examples)

**Repos de referencia:**
- [langgraph/examples](https://github.com/langchain-ai/langgraph/tree/main/examples)

### 🗓️ Plan día por día (6h total)

**Lunes (1.5h):** Fundamentos LangGraph
- Video tutorial
- Quick start guide
- Instala y prueba ejemplo básico

**Martes (1.5h):** Estado y nodes
- Implementa un graph simple
- Experimenta con state mutations

**Miércoles (1.5h):** Conditional routing
- Implementa routing basado en clasificación
- Múltiples paths en el graph

**Jueves (1h):** Checkpointing y persistencia
- Guarda estado entre ejecuciones
- Reanuda workflows interrumpidos

**Viernes (1.5h):** Proyecto - Support Agent
- Construye un agent de soporte con routing
- Integra con tu Docs Q&A

### 💻 Código: Support Agent con LangGraph

**Instalación:**
```bash
pip install langgraph langchain-openai
```

**1. Estado del agent:**
```python
# support_agent.py
from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage
import operator

class AgentState(TypedDict):
    """
    Estado que se pasa entre todos los nodes del graph
    """
    messages: Annotated[Sequence[BaseMessage], operator.add]
    question_type: str  # "technical", "billing", "general"
    needs_human: bool
    documents_found: list
    final_answer: str
```

**2. Nodes (funciones de procesamiento):**
```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def classify_question(state: AgentState) -> AgentState:
    """
    Node 1: Clasifica el tipo de pregunta
    """
    messages = state["messages"]
    last_message = messages[-1].content
    
    classification_prompt = f"""
    Classify this customer question into one of these categories:
    - technical: questions about product features, how to use, bugs
    - billing: questions about payments, invoices, subscriptions
    - general: greetings, feedback, other
    
    Question: {last_message}
    
    Answer with just the category name.
    """
    
    response = llm.invoke([HumanMessage(content=classification_prompt)])
    question_type = response.content.strip().lower()
    
    return {
        **state,
        "question_type": question_type
    }

def search_docs(state: AgentState) -> AgentState:
    """
    Node 2a: Busca en documentación técnica (para questions "technical")
    """
    messages = state["messages"]
    question = messages[-1].content
    
    # Aquí conectarías con tu RAG system
    # Por ahora, mock data
    mock_docs = [
        {"content": "To reset your password, go to Settings > Security...", "source": "docs/security.md"},
        {"content": "API rate limits are 100 requests per minute...", "source": "docs/api.md"}
    ]
    
    return {
        **state,
        "documents_found": mock_docs
    }

def handle_billing(state: AgentState) -> AgentState:
    """
    Node 2b: Maneja preguntas de billing (requiere human)
    """
    return {
        **state,
        "needs_human": True,
        "final_answer": "I'm transferring you to our billing team who can help with this."
    }

def handle_general(state: AgentState) -> AgentState:
    """
    Node 2c: Responde preguntas generales directamente
    """
    messages = state["messages"]
    question = messages[-1].content
    
    response = llm.invoke([
        SystemMessage(content="You are a friendly customer support assistant."),
        HumanMessage(content=question)
    ])
    
    return {
        **state,
        "final_answer": response.content
    }

def generate_answer(state: AgentState) -> AgentState:
    """
    Node 3: Genera respuesta final basada en docs encontrados
    """
    messages = state["messages"]
    question = messages[-1].content
    docs = state.get("documents_found", [])
    
    context = "\n\n".join([f"Source: {doc['source']}\n{doc['content']}" for doc in docs])
    
    prompt = f"""
    Answer this customer question using the following documentation:
    
    {context}
    
    Question: {question}
    
    Provide a clear, helpful answer with source references.
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    
    return {
        **state,
        "final_answer": response.content
    }

def route_question(state: AgentState) -> str:
    """
    Conditional edge: decide qué path tomar
    """
    question_type = state.get("question_type", "general")
    
    if question_type == "technical":
        return "search_docs"
    elif question_type == "billing":
        return "handle_billing"
    else:
        return "handle_general"

def should_generate_answer(state: AgentState) -> str:
    """
    Decide si generar respuesta o escalar a humano
    """
    if state.get("needs_human"):
        return "end"
    return "generate_answer"
```

**3. Construir el graph:**
```python
from langgraph.graph import StateGraph, END

def create_support_graph():
    """
    Crea el workflow graph
    """
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("classify", classify_question)
    workflow.add_node("search_docs", search_docs)
    workflow.add_node("handle_billing", handle_billing)
    workflow.add_node("handle_general", handle_general)
    workflow.add_node("generate_answer", generate_answer)
    
    # Set entry point
    workflow.set_entry_point("classify")
    
    # Add conditional edges
    workflow.add_conditional_edges(
        "classify",
        route_question,
        {
            "search_docs": "search_docs",
            "handle_billing": "handle_billing",
            "handle_general": "handle_general"
        }
    )
    
    # Edges después de buscar docs
    workflow.add_conditional_edges(
        "search_docs",
        should_generate_answer,
        {
            "generate_answer": "generate_answer",
            "end": END
        }
    )
    
    # End edges
    workflow.add_edge("handle_billing", END)
    workflow.add_edge("handle_general", END)
    workflow.add_edge("generate_answer", END)
    
    return workflow.compile()

# Usage
if __name__ == "__main__":
    graph = create_support_graph()
    
    # Test
    initial_state = {
        "messages": [HumanMessage(content="How do I reset my API key?")],
        "question_type": "",
        "needs_human": False,
        "documents_found": [],
        "final_answer": ""
    }
    
    result = graph.invoke(initial_state)
    print(f"Final answer: {result['final_answer']}")
```

**4. Visualizar el graph:**
```python
from IPython.display import Image, display

# Genera imagen del graph
display(Image(graph.get_graph().draw_mermaid_png()))
```

**5. Con checkpointing (estado persistente):**
```python
from langgraph.checkpoint.sqlite import SqliteSaver

# Create checkpointer
memory = SqliteSaver.from_conn_string(":memory:")

# Compile con checkpointing
graph = workflow.compile(checkpointer=memory)

# Ejecuta con thread_id para persistencia
config = {"configurable": {"thread_id": "user-123"}}

# Primera llamada
result1 = graph.invoke(initial_state, config)

# Segunda llamada (recuerda contexto)
follow_up_state = {
    "messages": [HumanMessage(content="Can you explain that in more detail?")],
    "question_type": "",
    "needs_human": False,
    "documents_found": [],
    "final_answer": ""
}

result2 = graph.invoke(follow_up_state, config)  # Usa el mismo thread_id
```

**6. FastAPI integration:**
```python
# main.py
from fastapi import APIRouter
from pydantic import BaseModel
from support_agent import create_support_graph
from langchain_core.messages import HumanMessage

router = APIRouter(prefix="/support", tags=["support"])
support_graph = create_support_graph()

class SupportQuery(BaseModel):
    question: str
    user_id: str = "anonymous"

@router.post("/ask")
def ask_support(query: SupportQuery):
    """
    Support agent con LangGraph
    """
    initial_state = {
        "messages": [HumanMessage(content=query.question)],
        "question_type": "",
        "needs_human": False,
        "documents_found": [],
        "final_answer": ""
    }
    
    config = {"configurable": {"thread_id": query.user_id}}
    result = support_graph.invoke(initial_state, config)
    
    return {
        "question": query.question,
        "question_type": result["question_type"],
        "needs_human": result["needs_human"],
        "answer": result["final_answer"],
        "sources": [doc["source"] for doc in result.get("documents_found", [])]
    }
```

### 🧪 Ejercicios prácticos

1. **Añade un node** "escalate_to_human" que envíe notificación cuando `needs_human=True`

2. **Implementa retry logic**: si un tool falla, el graph debe reintentar o tomar un path alternativo

3. **Human-in-the-loop**: pausa el graph después de clasificar para que un humano apruebe el routing

4. **Multi-agent**: crea dos subgraphs (uno para soporte técnico, otro para ventas) y enruta entre ellos

### ✅ Checklist de dominio

- [ ] Entiendes la diferencia entre LangChain agents y LangGraph
- [ ] Definiste un State con TypedDict
- [ ] Creaste nodes (funciones de procesamiento)
- [ ] Implementaste conditional edges
- [ ] Añadiste checkpointing para persistencia
- [ ] Visualizaste el graph
- [ ] Integraste con FastAPI
- [ ] Manejaste errores en nodes

---

## 🧠 SEMANA 26: Memory y State Management (29 Abril - 5 Mayo)

**Objetivo:** Implementar diferentes tipos de memoria para agents: conversational memory, semantic memory, y episodic memory.

### 📖 Conceptos clave

**¿Por qué memoria?**
Los LLMs son **stateless** (sin estado). Cada llamada es independiente.
Para que un agent sea útil, necesita recordar:
- Conversaciones previas
- Hechos aprendidos sobre el usuario
- Acciones tomadas anteriormente

**Tipos de memoria:**

1. **Short-term (conversational):**
   - Últimos N mensajes
   - Context window limitado
   - Ejemplo: ChatGPT recuerda tu conversación actual

2. **Long-term (semantic):**
   - Hechos importantes almacenados en vector DB
   - Recuperados con similarity search
   - Ejemplo: "El usuario prefiere respuestas en español"

3. **Episodic:**
   - Historial de acciones/decisiones
   - Útil para debugging y auditoría
   - Ejemplo: "El usuario preguntó sobre X hace 2 días"

**Trade-offs:**
- Más memoria = más contexto = mejores respuestas
- Pero: más tokens = más caro + más lento
- Solución: **Selective memory** (solo lo relevante)

### 📚 Recursos de estudio

**Videos:**
- [Building Chatbots with Memory](https://www.youtube.com/watch?v=X05uK0TZozM) (20min)
- [LangChain Memory Types Explained](https://www.youtube.com/watch?v=dxO6pzlgJiY) (15min)

**Artículos:**
- [LangChain Memory Docs](https://python.langchain.com/docs/modules/memory/)
- [MemGPT Paper](https://arxiv.org/abs/2310.08560) - advanced memory management

**Repos:**
- [mem0ai/mem0](https://github.com/mem0ai/mem0) - memoria para AI agents

### 🗓️ Plan día por día (6h total)

**Lunes (1.5h):** Conversational memory básica
- Implementa buffer memory
- Experimenta con summary memory

**Martes (1.5h):** Semantic memory con vector DB
- Almacena facts en pgvector
- Retrieval basado en similarity

**Miércoles (1.5h):** Memory management
- Implementa token counting
- Truncate/summarize cuando excedes límite

**Jueves (1h):** Episodic memory
- Log de acciones en PostgreSQL
- Query historial para debugging

**Viernes (1.5h):** Integración completa
- Añade memory a tu support agent
- Testing con conversaciones largas

### 💻 Código: Sistema de memoria completo

**1. Schema de base de datos:**
```sql
-- migrations/add_memory.sql

-- Conversational memory (buffer reciente)
CREATE TABLE conversation_history (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL,  -- 'user' o 'assistant'
    content TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tokens_used INTEGER
);

-- Semantic memory (facts importantes)
CREATE TABLE user_facts (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    fact TEXT NOT NULL,
    embedding vector(1536),
    importance FLOAT DEFAULT 0.5,  -- 0-1, qué tan importante es este fact
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Episodic memory (historial de acciones)
CREATE TABLE agent_actions (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    session_id VARCHAR(255),
    action_type VARCHAR(100),  -- 'search', 'tool_call', 'escalation'
    action_data JSONB,
    result JSONB,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices
CREATE INDEX idx_conv_user_time ON conversation_history(user_id, timestamp DESC);
CREATE INDEX idx_facts_user ON user_facts(user_id);
CREATE INDEX idx_actions_user_session ON agent_actions(user_id, session_id);

-- Vector similarity index
CREATE INDEX idx_facts_embedding ON user_facts USING ivfflat (embedding vector_cosine_ops);
```

**2. Memory Manager class:**
```python
# memory_manager.py
from sqlalchemy.orm import Session
from sqlalchemy import text, desc
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import tiktoken
from openai import OpenAI
import logging

logger = logging.getLogger(__name__)

class MemoryManager:
    """
    Gestiona todos los tipos de memoria para agents
    """
    
    def __init__(self, db: Session, user_id: str):
        self.db = db
        self.user_id = user_id
        self.openai_client = OpenAI()
        self.encoding = tiktoken.encoding_for_model("gpt-4")
        self.max_tokens = 4000  # Límite para context window
    
    def add_message(self, role: str, content: str):
        """
        Añade mensaje a conversational memory
        """
        tokens = len(self.encoding.encode(content))
        
        self.db.execute(
            text("""
                INSERT INTO conversation_history (user_id, role, content, tokens_used)
                VALUES (:user_id, :role, :content, :tokens)
            """),
            {
                "user_id": self.user_id,
                "role": role,
                "content": content,
                "tokens": tokens
            }
        )
        self.db.commit()
    
    def get_recent_messages(self, limit: int = 10) -> List[Dict]:
        """
        Recupera últimos N mensajes (short-term memory)
        """
        result = self.db.execute(
            text("""
                SELECT role, content, timestamp
                FROM conversation_history
                WHERE user_id = :user_id
                ORDER BY timestamp DESC
                LIMIT :limit
            """),
            {"user_id": self.user_id, "limit": limit}
        )
        
        messages = []
        for row in result:
            messages.append({
                "role": row[0],
                "content": row[1],
                "timestamp": row[2]
            })
        
        return list(reversed(messages))  # Cronológico
    
    def get_relevant_messages(self, query: str, max_tokens: int = 2000) -> List[Dict]:
        """
        Recupera mensajes relevantes hasta un límite de tokens
        (Mejor que simplemente "últimos N")
        """
        # Primero, embed la query
        query_embedding = self._get_embedding(query)
        
        # Busca mensajes similares
        result = self.db.execute(
            text("""
                WITH message_embeddings AS (
                    SELECT 
                        role, 
                        content, 
                        timestamp,
                        tokens_used
                    FROM conversation_history
                    WHERE user_id = :user_id
                    AND timestamp > NOW() - INTERVAL '7 days'
                    ORDER BY timestamp DESC
                    LIMIT 50
                )
                SELECT * FROM message_embeddings
                ORDER BY timestamp DESC
            """),
            {"user_id": self.user_id}
        )
        
        messages = []
        total_tokens = 0
        
        for row in result:
            msg_tokens = row[3]
            if total_tokens + msg_tokens > max_tokens:
                break
            
            messages.append({
                "role": row[0],
                "content": row[1]
            })
            total_tokens += msg_tokens
        
        return list(reversed(messages))
    
    def add_fact(self, fact: str, importance: float = 0.5):
        """
        Añade un fact importante a semantic memory
        """
        embedding = self._get_embedding(fact)
        
        self.db.execute(
            text("""
                INSERT INTO user_facts (user_id, fact, embedding, importance)
                VALUES (:user_id, :fact, :embedding, :importance)
            """),
            {
                "user_id": self.user_id,
                "fact": fact,
                "embedding": embedding,
                "importance": importance
            }
        )
        self.db.commit()
        logger.info(f"Stored fact for {self.user_id}: {fact}")
    
    def get_relevant_facts(self, query: str, top_k: int = 5) -> List[str]:
        """
        Recupera facts relevantes usando similarity search
        """
        query_embedding = self._get_embedding(query)
        
        result = self.db.execute(
            text("""
                SELECT fact, importance, 
                       1 - (embedding <=> :query_embedding::vector) as similarity
                FROM user_facts
                WHERE user_id = :user_id
                ORDER BY embedding <=> :query_embedding::vector
                LIMIT :top_k
            """),
            {
                "user_id": self.user_id,
                "query_embedding": query_embedding,
                "top_k": top_k
            }
        )
        
        facts = [row[0] for row in result if row[2] > 0.7]  # Similarity threshold
        
        # Update last_accessed
        if facts:
            self.db.execute(
                text("""
                    UPDATE user_facts
                    SET last_accessed = NOW()
                    WHERE user_id = :user_id AND fact = ANY(:facts)
                """),
                {"user_id": self.user_id, "facts": facts}
            )
            self.db.commit()
        
        return facts
    
    def log_action(self, action_type: str, action_data: Dict, result: Dict, session_id: str):
        """
        Log de acciones para episodic memory
        """
        self.db.execute(
            text("""
                INSERT INTO agent_actions 
                (user_id, session_id, action_type, action_data, result)
                VALUES (:user_id, :session_id, :action_type, :action_data, :result)
            """),
            {
                "user_id": self.user_id,
                "session_id": session_id,
                "action_type": action_type,
                "action_data": action_data,
                "result": result
            }
        )
        self.db.commit()
    
    def get_action_history(self, session_id: Optional[str] = None, limit: int = 20) -> List[Dict]:
        """
        Recupera historial de acciones
        """
        query_text = """
            SELECT action_type, action_data, result, timestamp
            FROM agent_actions
            WHERE user_id = :user_id
        """
        
        params = {"user_id": self.user_id, "limit": limit}
        
        if session_id:
            query_text += " AND session_id = :session_id"
            params["session_id"] = session_id
        
        query_text += " ORDER BY timestamp DESC LIMIT :limit"
        
        result = self.db.execute(text(query_text), params)
        
        return [
            {
                "action_type": row[0],
                "action_data": row[1],
                "result": row[2],
                "timestamp": row[3]
            }
            for row in result
        ]
    
    def extract_and_store_facts(self, conversation: List[Dict]):
        """
        Extrae facts importantes de una conversación usando LLM
        """
        conversation_text = "\n".join([
            f"{msg['role']}: {msg['content']}" 
            for msg in conversation
        ])
        
        prompt = f"""
        Extract important facts about the user from this conversation.
        Focus on preferences, personal info, recurring needs, or important context.
        
        Conversation:
        {conversation_text}
        
        List facts as bullet points, one per line. If no important facts, return "None".
        """
        
        response = self.openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        
        facts_text = response.choices[0].message.content.strip()
        
        if facts_text.lower() != "none":
            facts = [f.strip("- ") for f in facts_text.split("\n") if f.strip()]
            for fact in facts:
                self.add_fact(fact, importance=0.7)
    
    def _get_embedding(self, text: str) -> List[float]:
        """
        Genera embedding para text
        """
        response = self.openai_client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return response.data[0].embedding
    
    def summarize_old_messages(self, days_old: int = 7):
        """
        Resume mensajes antiguos para ahorrar espacio
        (Advanced: no prioritario ahora)
        """
        # TODO: implementar summarization de mensajes > 7 días
        pass
```

**3. Integrar memoria con agent:**
```python
# agent_with_memory.py
from memory_manager import MemoryManager
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from sqlalchemy.orm import Session
import uuid

class AgentWithMemory:
    """
    Agent que usa memoria de 3 tipos
    """
    
    def __init__(self, db: Session, user_id: str):
        self.db = db
        self.user_id = user_id
        self.memory = MemoryManager(db, user_id)
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
        self.session_id = str(uuid.uuid4())
    
    def chat(self, user_message: str) -> str:
        """
        Procesa mensaje con memoria completa
        """
        # 1. Guardar mensaje del usuario
        self.memory.add_message("user", user_message)
        
        # 2. Recuperar contexto relevante
        recent_messages = self.memory.get_relevant_messages(user_message, max_tokens=2000)
        relevant_facts = self.memory.get_relevant_facts(user_message, top_k=5)
        recent_actions = self.memory.get_action_history(self.session_id, limit=5)
        
        # 3. Construir system prompt con contexto
        system_content = "You are a helpful assistant with memory of past conversations."
        
        if relevant_facts:
            system_content += "\n\nImportant facts about this user:\n"
            system_content += "\n".join([f"- {fact}" for fact in relevant_facts])
        
        if recent_actions:
            system_content += "\n\nRecent actions taken:\n"
            for action in recent_actions[:3]:
                system_content += f"- {action['action_type']}: {action['action_data']}\n"
        
        # 4. Construir messages para LLM
        messages = [SystemMessage(content=system_content)]
        
        for msg in recent_messages:
            if msg["role"] == "user":
                messages.append(HumanMessage(content=msg["content"]))
            else:
                messages.append(AIMessage(content=msg["content"]))
        
        messages.append(HumanMessage(content=user_message))
        
        # 5. Llamar LLM
        response = self.llm.invoke(messages)
        assistant_message = response.content
        
        # 6. Guardar respuesta
        self.memory.add_message("assistant", assistant_message)
        
        # 7. Log action
        self.memory.log_action(
            action_type="chat_response",
            action_data={"user_message": user_message},
            result={"response": assistant_message},
            session_id=self.session_id
        )
        
        # 8. Extraer y guardar facts cada 5 mensajes
        message_count = len(recent_messages)
        if message_count % 10 == 0:
            self.memory.extract_and_store_facts(recent_messages[-10:])
        
        return assistant_message

# FastAPI endpoint
from fastapi import Depends
from app.database import get_db

@router.post("/chat")
def chat_with_memory(
    message: str,
    user_id: str,
    db: Session = Depends(get_db)
):
    """
    Chat endpoint con memoria persistente
    """
    agent = AgentWithMemory(db, user_id)
    response = agent.chat(message)
    
    return {
        "user_id": user_id,
        "message": message,
        "response": response
    }
```

**Testing:**
```python
# test_memory.py
import pytest
from memory_manager import MemoryManager

def test_conversational_memory(db_session):
    memory = MemoryManager(db_session, "test-user")
    
    # Simula conversación
    memory.add_message("user", "My name is Marco")
    memory.add_message("assistant", "Nice to meet you, Marco!")
    memory.add_message("user", "I'm studying data science")
    
    messages = memory.get_recent_messages(limit=10)
    assert len(messages) == 3
    assert messages[0]["content"] == "My name is Marco"

def test_semantic_memory(db_session):
    memory = MemoryManager(db_session, "test-user")
    
    memory.add_fact("User is studying data science at IE Business School", importance=0.8)
    memory.add_fact("User prefers Python over R", importance=0.6)
    
    facts = memory.get_relevant_facts("What programming languages does the user like?")
    assert any("Python" in fact for fact in facts)

def test_episodic_memory(db_session):
    memory = MemoryManager(db_session, "test-user")
    
    memory.log_action(
        action_type="search",
        action_data={"query": "FastAPI tutorial"},
        result={"docs_found": 5},
        session_id="session-123"
    )
    
    actions = memory.get_action_history(session_id="session-123")
    assert len(actions) == 1
    assert actions[0]["action_type"] == "search"
```

### 🧪 Ejercicios prácticos

1. **Fact importance decay:** Implementa lógica para que facts antiguos y no accedidos pierdan importancia con el tiempo

2. **Memory compression:** Cuando la conversación excede 10k tokens, resume automáticamente usando un LLM

3. **Cross-session memory:** Prueba que un usuario pueda retomar una conversación días después y el agent recuerde contexto

4. **Privacy controls:** Añade endpoint para que el usuario pueda borrar toda su memoria

### ✅ Checklist de dominio

- [ ] Implementaste conversational memory (buffer reciente)
- [ ] Añadiste semantic memory con vector similarity
- [ ] Creaste episodic memory (log de acciones)
- [ ] Integraste los 3 tipos en un agent
- [ ] Implementaste extracción automática de facts
- [ ] Manejaste límites de tokens (truncate/summarize)
- [ ] Testeaste memoria cross-session
- [ ] Añadiste índices en la DB para performance

---

## 🏗️ SEMANAS 27-30: Proyecto 3 - Production Support Bot (6-31 Mayo)

**Objetivo:** Construir un support bot completo de producción con todo lo aprendido: RAG, agents, LangGraph, memory, monitoring, safety.

Este es tu proyecto estrella para el portfolio. Va a combinar TODO.

### 📋 Especificaciones del proyecto

**Nombre:** IntelliSupport AI

**Descripción:**
Sistema de atención al cliente que:
- Clasifica y enruta preguntas
- Busca en documentación (RAG)
- Ejecuta acciones (agents con tools)
- Recuerda contexto del usuario (memory)
- Escala a humanos cuando es necesario
- Monitored con Langfuse
- Safe con guardrails y Sentry

**Stack técnico:**
- FastAPI
- PostgreSQL + pgvector
- LangGraph para workflows
- OpenAI API
- Langfuse
- Sentry
- Docker

**Funcionalidades core:**

1. **Multi-intent classification**
   - Técnico / Billing / General
   - Multi-idioma (EN/ES)

2. **RAG integrado**
   - Upload docs (PDF/Markdown)
   - Hybrid search (keyword + semantic)
   - Reranking
   - Citations

3. **Tools disponibles para el agent:**
   - `search_docs()` - busca en knowledge base
   - `check_order_status(order_id)` - mock de sistema externo
   - `create_ticket(issue)` - crea ticket en sistema de soporte
   - `schedule_callback(time)` - agenda llamada con agente humano

4. **Memory system:**
   - Recuerda conversaciones previas
   - Almacena preferencias del usuario
   - Tracking de issues reportados

5. **Safety:**
   - Input validation (max length, no injection)
   - PII detection y redaction
   - Content moderation
   - Rate limiting por usuario

6. **Monitoring:**
   - Langfuse tracing completo
   - Metrics: latency, success rate, escalation rate
   - User feedback loop

### 🗓️ Plan por semanas

#### **Semana 27 (6-12 Mayo): Arquitectura + Setup**

**Objetivos:**
- Diseñar arquitectura completa
- Setup infrastructure
- Implementar esquema DB

**Día por día:**

**Lunes (1.5h):**
- Dibuja arquitectura del sistema (usa Excalidraw o similar)
- Define APIs (endpoints, request/response schemas)
- Escribe README con especificaciones

**Martes (1.5h):**
- Setup proyecto FastAPI desde cero
- Estructura de carpetas pro:
```
intellisupport/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models/          # SQLAlchemy models
│   ├── schemas/         # Pydantic schemas
│   ├── routers/         # API endpoints
│   ├── services/        # Business logic
│   │   ├── rag/
│   │   ├── agent/
│   │   ├── memory/
│   │   └── monitoring/
│   └── utils/
├── tests/
├── docs/                # Documentation to be indexed
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

**Miércoles (1.5h):**
- Schema completo de PostgreSQL:
```sql
-- Docs (de RAG)
CREATE TABLE documents (...);
CREATE TABLE document_chunks (...);

-- Conversations & memory
CREATE TABLE users (
    id VARCHAR PRIMARY KEY,
    created_at TIMESTAMP,
    preferences JSONB
);

CREATE TABLE conversations (
    id UUID PRIMARY KEY,
    user_id VARCHAR REFERENCES users(id),
    started_at TIMESTAMP,
    last_message_at TIMESTAMP,
    status VARCHAR  -- 'active', 'resolved', 'escalated'
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    conversation_id UUID REFERENCES conversations(id),
    role VARCHAR,
    content TEXT,
    metadata JSONB,  -- tool calls, thinking, etc.
    timestamp TIMESTAMP
);

CREATE TABLE user_facts (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR REFERENCES users(id),
    fact TEXT,
    embedding vector(1536),
    importance FLOAT,
    created_at TIMESTAMP
);

-- Tickets & escalations
CREATE TABLE support_tickets (
    id SERIAL PRIMARY KEY,
    conversation_id UUID REFERENCES conversations(id),
    user_id VARCHAR,
    title TEXT,
    description TEXT,
    status VARCHAR,  -- 'open', 'in_progress', 'resolved'
    created_at TIMESTAMP,
    assigned_to VARCHAR  -- human agent
);

-- Monitoring & feedback
CREATE TABLE user_feedback (
    id SERIAL PRIMARY KEY,
    conversation_id UUID,
    rating INTEGER,  -- 1-5
    feedback_text TEXT,
    timestamp TIMESTAMP
);
```

**Jueves (1h):**
- Docker setup completo
- `docker-compose.yml` con FastAPI + PostgreSQL + pgvector
- Verifica que todo levanta correctamente

**Viernes (1.5h):**
- Config management con Pydantic Settings
- Environment variables
- Health check endpoint básico

**Código inicial:**
```python
# app/config.py
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # API
    app_name: str = "IntelliSupport AI"
    debug: bool = False
    
    # Database
    database_url: str
    
    # OpenAI
    openai_api_key: str
    openai_model: str = "gpt-4o-mini"
    
    # Langfuse
    langfuse_public_key: str
    langfuse_secret_key: str
    langfuse_host: str = "https://cloud.langfuse.com"
    
    # Sentry
    sentry_dsn: str | None = None
    
    # Limits
    max_message_length: int = 2000
    rate_limit_per_minute: int = 20
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()
```

#### **Semana 28 (13-19 Mayo): RAG System + Tools**

**Objetivos:**
- Implementar sistema RAG completo
- Crear tools para el agent
- Integración básica

**Lunes (1.5h):** RAG service
- Reutiliza código de semanas anteriores
- Adapta para este proyecto
- Hybrid search + reranking

**Martes (1.5h):** Tools implementation
```python
# app/services/tools.py
from typing import Dict, Any

def search_docs(query: str, top_k: int = 5) -> Dict[str, Any]:
    """
    Busca en knowledge base usando RAG
    """
    # Conecta con tu RAG service
    pass

def check_order_status(order_id: str) -> Dict[str, Any]:
    """
    Consulta estado de pedido (mock)
    """
    # En producción: API call a sistema de orders
    mock_orders = {
        "ORD-123": {"status": "shipped", "eta": "2024-05-15"},
        "ORD-456": {"status": "processing", "eta": "2024-05-20"}
    }
    return mock_orders.get(order_id, {"error": "Order not found"})

def create_ticket(title: str, description: str, user_id: str) -> Dict[str, Any]:
    """
    Crea ticket de soporte
    """
    # Insertar en DB
    pass

def schedule_callback(user_id: str, preferred_time: str) -> Dict[str, Any]:
    """
    Agenda llamada con agente humano
    """
    # En producción: integración con calendario
    return {
        "status": "scheduled",
        "time": preferred_time,
        "message": "An agent will call you at the specified time"
    }

# Tool definitions en formato OpenAI
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_docs",
            "description": "Search the knowledge base for information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"}
                },
                "required": ["query"]
            }
        }
    },
    # ... resto de tools
]
```

**Miércoles (1.5h):** Memory service
- Adapta MemoryManager de semana 26
- Integra con nuevo schema

**Jueves (1h):** Testing de componentes individuales
- Tests para RAG
- Tests para tools
- Tests para memory

**Viernes (1.5h):** Integration
- Conecta todos los servicios
- Verifica que se comunican correctamente

#### **Semana 29 (20-26 Mayo): LangGraph Workflow + Agent Logic**

**Objetivos:**
- Implementar LangGraph workflow completo
- Lógica de routing y decisión
- Multi-turn conversations

**Lunes (1.5h):** Diseñar el graph
- Nodes: classify, search, use_tool, generate_response, escalate
- Conditional edges basados en clasificación e intención

**Martes (1.5h):** Implementar nodes
```python
# app/services/agent/nodes.py
from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage
import operator

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    user_id: str
    conversation_id: str
    intent: str  # 'technical', 'billing', 'general', 'order_status'
    needs_escalation: bool
    tools_used: list
    final_answer: str
    sources: list

def classify_intent(state: AgentState) -> AgentState:
    """Clasifica la intención del usuario"""
    pass

def retrieve_memory(state: AgentState) -> AgentState:
    """Carga memoria relevante del usuario"""
    pass

def search_knowledge(state: AgentState) -> AgentState:
    """Busca en docs usando RAG"""
    pass

def use_tool(state: AgentState) -> AgentState:
    """Ejecuta tool según intención"""
    pass

def generate_response(state: AgentState) -> AgentState:
    """Genera respuesta final"""
    pass

def escalate_to_human(state: AgentState) -> AgentState:
    """Crea ticket y notifica"""
    pass
```

**Miércoles (1.5h):** Construir y compilar graph
```python
# app/services/agent/graph.py
from langgraph.graph import StateGraph, END
from .nodes import *

def create_support_graph():
    workflow = StateGraph(AgentState)
    
    # Nodes
    workflow.add_node("classify", classify_intent)
    workflow.add_node("retrieve_memory", retrieve_memory)
    workflow.add_node("search", search_knowledge)
    workflow.add_node("use_tool", use_tool)
    workflow.add_node("generate", generate_response)
    workflow.add_node("escalate", escalate_to_human)
    
    # Entry
    workflow.set_entry_point("classify")
    
    # Conditional routing
    workflow.add_conditional_edges(
        "classify",
        route_by_intent,
        {
            "search": "retrieve_memory",
            "tool": "use_tool",
            "escalate": "escalate",
            "simple": "generate"
        }
    )
    
    workflow.add_edge("retrieve_memory", "search")
    workflow.add_edge("search", "generate")
    workflow.add_edge("use_tool", "generate")
    workflow.add_edge("generate", END)
    workflow.add_edge("escalate", END)
    
    return workflow.compile()
```

**Jueves (1h):** Testing del graph
- Casos de test para cada path
- Verifica routing correcto

**Viernes (1.5h):** Multi-turn support
- Checkpointing para conversaciones largas
- Follow-up questions

#### **Semana 30 (27-31 Mayo): Safety, Monitoring & Polish**

**Objetivos:**
- Implementar guardrails completos
- Integrar Langfuse y Sentry
- Polish UX

**Lunes (1.5h):** Safety layer
```python
# app/services/safety.py
import re
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

class SafetyGuard:
    def __init__(self):
        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()
        self.max_length = 2000
    
    def validate_input(self, text: str) -> tuple[bool, str]:
        """
        Valida input del usuario
        Returns: (is_valid, error_message)
        """
        # Length check
        if len(text) > self.max_length:
            return False, f"Message too long (max {self.max_length} chars)"
        
        # Injection patterns
        injection_patterns = [
            r"ignore previous instructions",
            r"system:",
            r"<\|im_start\|>",
            r"###",
        ]
        
        for pattern in injection_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return False, "Invalid input detected"
        
        return True, ""
    
    def detect_pii(self, text: str) -> list:
        """
        Detecta PII en el texto
        """
        results = self.analyzer.analyze(
            text=text,
            entities=["PHONE_NUMBER", "EMAIL_ADDRESS", "CREDIT_CARD", "PERSON"],
            language="en"
        )
        return results
    
    def anonymize(self, text: str) -> str:
        """
        Anonimiza PII detectado
        """
        pii = self.detect_pii(text)
        if pii:
            anonymized = self.anonymizer.anonymize(text=text, analyzer_results=pii)
            return anonymized.text
        return text
```

**Martes (1.5h):** Langfuse integration
```python
# app/services/monitoring/langfuse_client.py
from langfuse import Langfuse
from functools import wraps

langfuse = Langfuse()

def trace_agent(func):
    """
    Decorator para tracing con Langfuse
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        trace = langfuse.trace(name=func.__name__)
        try:
            result = func(*args, **kwargs, trace=trace)
            trace.update(output=result)
            return result
        except Exception as e:
            trace.update(level="ERROR", status_message=str(e))
            raise
    return wrapper

# Usage en tu agent
@trace_agent
def handle_user_message(message: str, user_id: str, trace=None):
    span = trace.span(name="classify_intent")
    # ... tu código
    span.end(output={"intent": intent})
    
    # Más spans para cada step...
```

**Miércoles (1.5h):** Sentry integration
```python
# app/main.py
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration

sentry_sdk.init(
    dsn=settings.sentry_dsn,
    integrations=[FastApiIntegration()],
    traces_sample_rate=0.1,
    profiles_sample_rate=0.1,
)
```

**Jueves (1h):** Feedback loop
```python
# app/routers/feedback.py
@router.post("/feedback")
def submit_feedback(
    conversation_id: str,
    rating: int,
    feedback: str = ""
):
    """
    Usuario califica la conversación
    """
    # Store en DB
    # Send to Langfuse como score
    langfuse.score(
        trace_id=conversation_id,
        name="user_rating",
        value=rating
    )
```

**Viernes (1.5h):** Documentation + README
- Documenta toda la API (usa FastAPI auto-docs)
- README con arquitectura, setup, usage
- Demo video/GIF

### ✅ Checklist de dominio del Proyecto 3

- [ ] Arquitectura completa documentada
- [ ] Setup con Docker funcional
- [ ] RAG system integrado
- [ ] 4+ tools implementados y funcionales
- [ ] LangGraph workflow completo
- [ ] Memory system (conversational + semantic)
- [ ] Safety guardrails (validation, PII, moderation)
- [ ] Langfuse tracing completo
- [ ] Sentry error tracking
- [ ] Tests (unit + integration)
- [ ] README profesional con setup instructions
- [ ] Demo funcionando
- [ ] Deployed (aunque sea local con ngrok)

---

## ☁️ FASE 4: DEPLOYMENT & EMPLEO (Junio-Septiembre)

A partir de aquí el foco cambia: ya sabes construir. Ahora necesitas:
1. Deployar para que otros lo vean
2. Prepararte para entrevistas
3. Conseguir trabajo

---

## 🚀 SEMANA 31: AWS Fundamentals (1-7 Junio)

**Objetivo:** Dominar los servicios de AWS esenciales para deployar tu aplicación AI.

### 📖 Conceptos clave

**¿Por qué AWS?**
- El cloud provider más usado en Europa
- Más ofertas de trabajo lo requieren
- Tiene servicios específicos para ML/AI (aunque no los necesites aún)

**Servicios que SÍ necesitas:**
1. **EC2**: servidores virtuales (donde corre tu app)
2. **RDS**: PostgreSQL managed (tu database)
3. **S3**: almacenamiento de archivos (PDFs, logs)
4. **ECS/App Runner**: container orchestration (Docker)
5. **IAM**: permisos y seguridad
6. **CloudWatch**: logs y monitoring

**Servicios que NO necesitas ahora:**
- Kubernetes (EKS) - overkill
- Lambda - no sirve para LLMs (timeout)
- SageMaker - para entrenar modelos (tú no entrenas)

**Conceptos importantes:**
- **Regions**: Madrid está en eu-west-1 (Ireland)
- **VPC**: red privada virtual para tus recursos
- **Security Groups**: firewall para controlar acceso
- **IAM Roles**: permisos sin contraseñas hardcodeadas

### 📚 Recursos de estudio

**Videos:**
- [AWS in 10 Minutes](https://www.youtube.com/watch?v=JIbIYCM48to) (10min) - overview
- [AWS EC2 Tutorial](https://www.youtube.com/watch?v=iHX-jtKIVNA) (20min)
- [AWS RDS Setup](https://www.youtube.com/watch?v=Ng_zi11N4_c) (15min)
- [Docker on AWS ECS](https://www.youtube.com/watch?v=zs3tyVgiBQQ) (25min)

**Cursos:**
- [AWS Free Tier](https://aws.amazon.com/free/) - crea cuenta (gratis 12 meses)
- AWS Academy Graduate (ya lo tienes según CV)

**Docs:**
- [AWS EC2 User Guide](https://docs.aws.amazon.com/ec2/)
- [AWS RDS PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html)

### 🗓️ Plan día por día (6h total)

**Lunes (1.5h):** Setup AWS account
- Crea cuenta AWS (free tier)
- Configura MFA (seguridad)
- Instala AWS CLI
- Configura credentials

**Martes (1.5h):** EC2 basics
- Lanza tu primera EC2 instance
- SSH a la instance
- Instala Python + Docker
- Deploy "Hello World" FastAPI

**Miércoles (1.5h):** RDS + S3
- Crea RDS PostgreSQL instance
- Conecta desde tu local
- Crea S3 bucket
- Sube/descarga archivos

**Jueves (1h):** Security & Networking
- Configura Security Groups
- VPC basics
- IAM roles

**Viernes (1.5h):** Deploy Docs Q&A en EC2
- Sube tu código
- Config DB connection a RDS
- Prueba que funciona desde internet

### 💻 Código: Deploy en AWS

**1. AWS CLI setup:**
```bash
# Instalar AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Configurar credentials
aws configure
# AWS Access Key ID: [tu key]
# AWS Secret Access Key: [tu secret]
# Default region: eu-west-1
# Default output format: json

# Test
aws s3 ls  # Lista tus buckets
```

**2. Crear EC2 instance:**
```bash
# Via AWS CLI (o usa la web console)
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \  # Ubuntu 22.04
  --instance-type t2.micro \  # Free tier
  --key-name my-key-pair \
  --security-group-ids sg-xxxxxxxx \
  --subnet-id subnet-xxxxxxxx \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=DocsQA-Server}]'
```

**3. SSH y setup:**
```bash
# SSH a tu instance
ssh -i "my-key-pair.pem" ubuntu@ec2-xx-xx-xx-xx.eu-west-1.compute.amazonaws.com

# Una vez dentro:
sudo apt update
sudo apt install -y python3-pip docker.io docker-compose git

# Clone tu repo
git clone https://github.com/tu-usuario/docs-qa-platform.git
cd docs-qa-platform

# Setup .env con RDS connection
nano .env
# DATABASE_URL=postgresql://user:pass@your-rds-instance.xxx.eu-west-1.rds.amazonaws.com:5432/docsqa
# OPENAI_API_KEY=sk-...

# Build y run
docker-compose up -d

# Verifica
curl localhost:8000/health
```

**4. RDS PostgreSQL:**
```bash
# Crear RDS via CLI
aws rds create-db-instance \
  --db-instance-identifier docsqa-db \
  --db-instance-class db.t3.micro \  # Free tier
  --engine postgres \
  --engine-version 15.4 \
  --master-username admin \
  --master-user-password YourStrongPassword123! \
  --allocated-storage 20 \
  --vpc-security-group-ids sg-xxxxxxxx \
  --publicly-accessible \
  --backup-retention-period 7

# Espera ~10 min hasta que esté disponible
aws rds describe-db-instances --db-instance-identifier docsqa-db

# Conecta desde tu local para testing
psql -h docsqa-db.xxxxx.eu-west-1.rds.amazonaws.com -U admin -d postgres

# Run migrations
alembic upgrade head
```

**5. S3 para storage:**
```python
# app/services/storage.py
import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

class S3Storage:
    def __init__(self, bucket_name: str):
        self.s3_client = boto3.client('s3')
        self.bucket = bucket_name
    
    def upload_file(self, file_path: str, object_name: str = None):
        """Upload file to S3"""
        if object_name is None:
            object_name = file_path
        
        try:
            self.s3_client.upload_file(file_path, self.bucket, object_name)
            logger.info(f"Uploaded {file_path} to s3://{self.bucket}/{object_name}")
            return True
        except ClientError as e:
            logger.error(f"Error uploading to S3: {e}")
            return False
    
    def download_file(self, object_name: str, file_path: str):
        """Download file from S3"""
        try:
            self.s3_client.download_file(self.bucket, object_name, file_path)
            return True
        except ClientError as e:
            logger.error(f"Error downloading from S3: {e}")
            return False
    
    def get_presigned_url(self, object_name: str, expiration=3600):
        """Generate presigned URL for temporary access"""
        try:
            url = self.s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': self.bucket, 'Key': object_name},
                ExpiresIn=expiration
            )
            return url
        except ClientError as e:
            logger.error(f"Error generating presigned URL: {e}")
            return None

# Usage en tu API
storage = S3Storage(bucket_name="docsqa-documents")

@router.post("/upload")
async def upload_document(file: UploadFile):
    # Save temporary
    temp_path = f"/tmp/{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())
    
    # Upload to S3
    s3_key = f"documents/{uuid.uuid4()}_{file.filename}"
    storage.upload_file(temp_path, s3_key)
    
    # Process document (chunking, embedding, etc.)
    # ...
    
    return {"message": "Document uploaded", "s3_key": s3_key}
```

**6. IAM Role para EC2 → S3:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::docsqa-documents",
        "arn:aws:s3:::docsqa-documents/*"
      ]
    }
  ]
}
```

Asigna este role a tu EC2 instance para que pueda acceder a S3 sin hardcodear credentials.

**7. Security Groups (firewall):**
```bash
# Crear security group
aws ec2 create-security-group \
  --group-name docsqa-sg \
  --description "Security group for DocsQA API"

# Allow HTTP (puerto 80)
aws ec2 authorize-security-group-ingress \
  --group-id sg-xxxxxxxx \
  --protocol tcp \
  --port 80 \
  --cidr 0.0.0.0/0

# Allow HTTPS (puerto 443)
aws ec2 authorize-security-group-ingress \
  --group-id sg-xxxxxxxx \
  --protocol tcp \
  --port 443 \
  --cidr 0.0.0.0/0

# Allow SSH solo desde tu IP
aws ec2 authorize-security-group-ingress \
  --group-id sg-xxxxxxxx \
  --protocol tcp \
  --port 22 \
  --cidr TU_IP/32
```

### 🧪 Ejercicios prácticos

1. **Deploy completo:** Despliega Docs Q&A Platform en EC2 + RDS + S3
2. **Backups automatizados:** Configura RDS automated backups
3. **CloudWatch alarms:** Crea alarma si CPU > 80% o errores en logs
4. **Cost estimation:** Calcula cuánto costaría correr esto en producción (usa AWS Pricing Calculator)

### ✅ Checklist de dominio

- [ ] Cuenta AWS creada y configurada
- [ ] AWS CLI instalado y funcional
- [ ] Lanzaste EC2 instance y conectaste por SSH
- [ ] Creaste RDS PostgreSQL y conectaste
- [ ] Creaste S3 bucket y subiste archivos
- [ ] Configuraste Security Groups correctamente
- [ ] Entiendes IAM roles básicos
- [ ] Desplegaste una app funcional en EC2
- [ ] Exploraste CloudWatch para logs

---

## 🔄 SEMANA 32: CI/CD con GitHub Actions (8-14 Junio)

**Objetivo:** Automatizar testing y deployment con CI/CD pipelines.

### 📖 Conceptos clave

**¿Qué es CI/CD?**
- **CI (Continuous Integration):** Cada push → tests automáticos
- **CD (Continuous Deployment):** Si tests pasan → deploy automático

**¿Por qué importa?**
- Detectas bugs antes de deploy
- Deploy es repetible (no manual)
- Más rápido iterar
- Profesional (todas las empresas lo usan)

**GitHub Actions:**
Herramienta gratis de GitHub para CI/CD.

**Workflow típico:**
```
Push to GitHub → GitHub Actions runner 
  → Run tests 
  → Build Docker image 
  → Push to registry 
  → Deploy to AWS 
  → Health check
```

### 📚 Recursos de estudio

**Videos:**
- [GitHub Actions Tutorial](https://www.youtube.com/watch?v=R8_veQiYBjI) (40min) - completo
- [CI/CD Explained](https://www.youtube.com/watch?v=scEDHsr3APg) (10min)

**Docs:**
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [GitHub Actions Quickstart](https://docs.github.com/en/actions/quickstart)

### 🗓️ Plan día por día (6h total)

**Lunes (1.5h):** Fundamentos GitHub Actions
- Qué son workflows, jobs, steps, actions
- Escribe tu primer workflow (hello world)
- Prueba triggers (on push, on PR, etc.)

**Martes (1.5h):** Testing pipeline
- Workflow que corre pytest en cada push
- Matrix testing (múltiples versiones de Python)
- Coverage report

**Miércoles (1.5h):** Docker build & push
- Build image en CI
- Push a Docker Hub o GitHub Container Registry
- Optimiza build con cache

**Jueves (1h):** Deploy automation
- Workflow que deploya a AWS EC2
- SSH desde GitHub Actions
- Pull latest image y restart

**Viernes (1.5h):** Complete pipeline
- Combina todo: test → build → deploy
- Añade health check post-deploy
- Rollback si falla

### 💻 Código: CI/CD Pipelines

**1. Estructura de carpetas:**
```
your-repo/
├── .github/
│   └── workflows/
│       ├── test.yml          # Run tests
│       ├── build.yml         # Build Docker image
│       └── deploy.yml        # Deploy to AWS
├── app/
├── tests/
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

**2. Test workflow:**
```yaml
# .github/workflows/test.yml
name: Run Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        python-version: ['3.10', '3.11']
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Cache dependencies
        uses: actions/cache@v3
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest pytest-cov
      
      - name: Run tests with coverage
        run: |
          pytest --cov=app --cov-report=xml --cov-report=term
      
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
          fail_ci_if_error: false
```

**3. Build & Push Docker image:**
```yaml
# .github/workflows/build.yml
name: Build and Push Docker Image

on:
  push:
    branches: [ main ]
    tags:
      - 'v*'

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2
      
      - name: Log in to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}
      
      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v4
        with:
          images: yourusername/docsqa-api
          tags: |
            type=ref,event=branch
            type=semver,pattern={{version}}
            type=sha
      
      - name: Build and push
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=registry,ref=yourusername/docsqa-api:buildcache
          cache-to: type=registry,ref=yourusername/docsqa-api:buildcache,mode=max
```

**4. Deploy to AWS:**
```yaml
# .github/workflows/deploy.yml
name: Deploy to AWS

on:
  workflow_run:
    workflows: ["Build and Push Docker Image"]
    types:
      - completed
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    if: ${{ github.event.workflow_run.conclusion == 'success' }}
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v2
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: eu-west-1
      
      - name: Deploy to EC2
        env:
          EC2_HOST: ${{ secrets.EC2_HOST }}
          EC2_USER: ubuntu
          SSH_PRIVATE_KEY: ${{ secrets.EC2_SSH_KEY }}
        run: |
          # Setup SSH
          mkdir -p ~/.ssh
          echo "$SSH_PRIVATE_KEY" > ~/.ssh/id_rsa
          chmod 600 ~/.ssh/id_rsa
          ssh-keyscan -H $EC2_HOST >> ~/.ssh/known_hosts
          
          # Deploy commands
          ssh $EC2_USER@$EC2_HOST << 'EOF'
            cd /home/ubuntu/docsqa-api
            
            # Pull latest code
            git pull origin main
            
            # Pull latest Docker image
            docker pull yourusername/docsqa-api:main
            
            # Stop old containers
            docker-compose down
            
            # Start new containers
            docker-compose up -d
            
            # Wait for health check
            sleep 10
            
            # Check if app is healthy
            curl -f http://localhost:8000/health || exit 1
            
            echo "Deployment successful!"
          EOF
      
      - name: Verify deployment
        run: |
          # Health check from outside
          curl -f http://${{ secrets.EC2_HOST }}/health
      
      - name: Rollback on failure
        if: failure()
        run: |
          echo "Deployment failed, rolling back..."
          ssh $EC2_USER@$EC2_HOST << 'EOF'
            cd /home/ubuntu/docsqa-api
            git checkout HEAD~1
            docker-compose up -d
          EOF
```

**5. Complete pipeline (all-in-one):**
```yaml
# .github/workflows/ci-cd.yml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  # Job 1: Run tests
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      - name: Run tests
        run: pytest --cov=app
  
  # Job 2: Lint & format check
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install linters
        run: pip install black flake8 mypy
      - name: Run black
        run: black --check app/
      - name: Run flake8
        run: flake8 app/ --max-line-length=100
      - name: Run mypy
        run: mypy app/ --ignore-missing-imports
  
  # Job 3: Build Docker image (solo en main)
  build:
    needs: [test, lint]
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build and push Docker image
        # ... (igual que arriba)
  
  # Job 4: Deploy (solo en main, después de build)
  deploy:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to AWS
        # ... (igual que arriba)
```

**6. Secrets en GitHub:**
Ve a tu repo → Settings → Secrets and variables → Actions → New repository secret

Añade:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `EC2_HOST`
- `EC2_SSH_KEY`
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`
- `OPENAI_API_KEY`

**7. Branch protection rules:**
Settings → Branches → Add rule

Para `main` branch:
- ✅ Require a pull request before merging
- ✅ Require status checks to pass before merging
  - Select: test, lint
- ✅ Require branches to be up to date before merging

Esto fuerza que:
1. Nadie puede pushear directo a main
2. Todos los PRs deben pasar tests
3. Code review obligatorio

### 🧪 Ejercicios prácticos

1. **Implementa el pipeline completo** para tu proyecto Docs Q&A
2. **Añade caching** para acelerar builds (dependencies, Docker layers)
3. **Notificaciones:** Envía mensaje a Slack/Discord cuando deploy termina
4. **Multi-environment:** Crea workflow para deploy a staging vs production

### ✅ Checklist de dominio

- [ ] Entiendes qué es CI/CD y por qué importa
- [ ] Creaste workflow de testing automático
- [ ] Implementaste Docker build & push
- [ ] Automatizaste deployment a AWS
- [ ] Configuraste secrets correctamente
- [ ] Añadiste branch protection rules
- [ ] Pipeline completo funciona end-to-end
- [ ] Probaste rollback en caso de fallo

---

## 🌐 SEMANAS 33-34: Proyecto Final - AI Micro-SaaS (15-28 Junio)

**Objetivo:** Construir una aplicación AI completa, production-ready, desplegada, con UI web, auth, y pricing. Este es tu proyecto estrella de portfolio.

### 📋 Especificaciones del proyecto

**Nombre:** DocuChat Pro

**Descripción:**
SaaS que permite a equipos hacer Q&A sobre sus documentos internos con AI.

**Features:**
1. **Authentication:** Sign up, login, password reset
2. **Document management:** Upload PDFs/Markdown, organize en carpetas
3. **AI Chat:** RAG-powered Q&A con citations
4. **Teams:** Invita miembros, comparte docs
5. **Usage tracking:** Tokens usados, límites por plan
6. **Pricing tiers:** Free, Pro, Team
7. **Admin dashboard:** Analytics, user management

**Tech Stack:**
- **Backend:** FastAPI (reutiliza tu código)
- **Frontend:** Next.js (React) o Streamlit (más fácil)
- **Database:** PostgreSQL + pgvector
- **Auth:** Auth0 o Supabase Auth
- **Payments:** Stripe (mock, no real payments)
- **Deployment:** AWS ECS + RDS + S3
- **CI/CD:** GitHub Actions

**Arquitectura:**
```
User → Next.js UI → FastAPI Backend → PostgreSQL
                 ↓
               OpenAI API
                 ↓
               Langfuse (monitoring)
```

### 🗓️ Plan por semanas

#### **Semana 33 (15-21 Junio): Backend + Auth + Payments**

**Lunes (1.5h):** Project setup
- Nueva carpeta `docuchat-pro/`
- Backend: FastAPI con estructura pro
- Database schema:
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email VARCHAR UNIQUE,
    hashed_password VARCHAR,
    plan VARCHAR DEFAULT 'free',  -- 'free', 'pro', 'team'
    tokens_used INTEGER DEFAULT 0,
    tokens_limit INTEGER DEFAULT 10000,
    created_at TIMESTAMP
);

CREATE TABLE workspaces (
    id UUID PRIMARY KEY,
    name VARCHAR,
    owner_id UUID REFERENCES users(id),
    created_at TIMESTAMP
);

CREATE TABLE workspace_members (
    workspace_id UUID REFERENCES workspaces(id),
    user_id UUID REFERENCES users(id),
    role VARCHAR,  -- 'admin', 'member'
    PRIMARY KEY (workspace_id, user_id)
);

CREATE TABLE documents (
    id UUID PRIMARY KEY,
    workspace_id UUID REFERENCES workspaces(id),
    filename VARCHAR,
    s3_key VARCHAR,
    uploaded_by UUID REFERENCES users(id),
    uploaded_at TIMESTAMP
);

CREATE TABLE document_chunks (
    -- igual que antes, con workspace_id
);

CREATE TABLE conversations (
    id UUID PRIMARY KEY,
    workspace_id UUID REFERENCES workspaces(id),
    user_id UUID REFERENCES users(id),
    started_at TIMESTAMP
);

CREATE TABLE messages (
    -- igual que antes
);
```

**Martes (1.5h):** Authentication
```python
# app/auth.py
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    # Load user from DB
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise credentials_exception
    return user

# Endpoints
@router.post("/signup")
def signup(email: str, password: str, db: Session = Depends(get_db)):
    # Check if user exists
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(400, "Email already registered")
    
    # Create user
    hashed = get_password_hash(password)
    user = User(email=email, hashed_password=hashed)
    db.add(user)
    db.commit()
    
    return {"message": "User created successfully"}

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(401, "Incorrect email or password")
    
    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return current_user
```

**Miércoles (1.5h):** Usage tracking & limits
```python
# app/middleware/usage.py
from functools import wraps

def track_usage(tokens: int):
    """
    Decorator para trackear tokens usados
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, current_user: User = None, db: Session = None, **kwargs):
            # Check limit
            if current_user.tokens_used + tokens > current_user.tokens_limit:
                raise HTTPException(429, "Token limit exceeded. Upgrade your plan.")
            
            # Execute function
            result = await func(*args, current_user=current_user, db=db, **kwargs)
            
            # Update usage
            current_user.tokens_used += tokens
            db.commit()
            
            return result
        return wrapper
    return decorator

# Usage
@router.post("/chat")
@track_usage(tokens=500)  # Estimas ~500 tokens por chat
async def chat(
    message: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # ... tu lógica de chat
    pass
```

**Jueves (1h):** Pricing & Plans
```python
# app/routers/billing.py
PLANS = {
    "free": {
        "name": "Free",
        "price": 0,
        "tokens_limit": 10000,
        "max_documents": 5,
        "max_workspaces": 1
    },
    "pro": {
        "name": "Pro",
        "price": 19,
        "tokens_limit": 100000,
        "max_documents": 100,
        "max_workspaces": 5
    },
    "team": {
        "name": "Team",
        "price": 49,
        "tokens_limit": 500000,
        "max_documents": -1,  # unlimited
        "max_workspaces": -1
    }
}

@router.post("/upgrade")
def upgrade_plan(
    plan: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if plan not in PLANS:
        raise HTTPException(400, "Invalid plan")
    
    # En producción: Stripe checkout
    # Por ahora, mock
    current_user.plan = plan
    current_user.tokens_limit = PLANS[plan]["tokens_limit"]
    db.commit()
    
    return {"message": f"Upgraded to {plan}", "new_limit": current_user.tokens_limit}

@router.get("/usage")
def get_usage(current_user: User = Depends(get_current_user)):
    plan_info = PLANS[current_user.plan]
    return {
        "plan": current_user.plan,
        "tokens_used": current_user.tokens_used,
        "tokens_limit": current_user.tokens_limit,
        "percentage": (current_user.tokens_used / current_user.tokens_limit) * 100,
        "plan_details": plan_info
    }
```

**Viernes (1.5h):** Workspaces & Teams
```python
# app/routers/workspaces.py
@router.post("/workspaces")
def create_workspace(
    name: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Check limit
    current_workspaces = db.query(Workspace).filter(Workspace.owner_id == current_user.id).count()
    max_workspaces = PLANS[current_user.plan]["max_workspaces"]
    if max_workspaces != -1 and current_workspaces >= max_workspaces:
        raise HTTPException(403, "Workspace limit reached. Upgrade your plan.")
    
    workspace = Workspace(name=name, owner_id=current_user.id)
    db.add(workspace)
    db.commit()
    
    return workspace

@router.post("/workspaces/{workspace_id}/invite")
def invite_member(
    workspace_id: str,
    email: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Check if current user is workspace owner/admin
    workspace = db.query(Workspace).filter(Workspace.id == workspace_id).first()
    if not workspace or workspace.owner_id != current_user.id:
        raise HTTPException(403, "Not authorized")
    
    # Find invited user
    invited_user = db.query(User).filter(User.email == email).first()
    if not invited_user:
        raise HTTPException(404, "User not found")
    
    # Add as member
    membership = WorkspaceMember(workspace_id=workspace_id, user_id=invited_user.id, role="member")
    db.add(membership)
    db.commit()
    
    return {"message": f"{email} added to workspace"}
```

#### **Semana 34 (22-28 Junio): Frontend + Deployment + Polish**

**Lunes (1.5h):** Frontend setup con Next.js
```bash
# Opción A: Next.js (más profesional pero más complejo)
npx create-next-app@latest docuchat-ui
cd docuchat-ui
npm install axios react-query

# Opción B: Streamlit (más rápido, menos bonito)
pip install streamlit
# Crea app.py
```

**Si eliges Streamlit (recomendado para rapidez):**
```python
# ui/app.py
import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(page_title="DocuChat Pro", page_icon="📄", layout="wide")

# Sidebar
with st.sidebar:
    st.title("📄 DocuChat Pro")
    
    # Auth
    if "token" not in st.session_state:
        with st.form("login"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            if st.form_submit_button("Login"):
                response = requests.post(f"{API_URL}/token", data={"username": email, "password": password})
                if response.ok:
                    st.session_state.token = response.json()["access_token"]
                    st.rerun()
        
        with st.expander("Sign up"):
            with st.form("signup"):
                new_email = st.text_input("Email")
                new_password = st.text_input("Password", type="password")
                if st.form_submit_button("Sign up"):
                    response = requests.post(f"{API_URL}/signup", json={"email": new_email, "password": new_password})
                    if response.ok:
                        st.success("Account created! Please login.")
    else:
        # Logged in
        headers = {"Authorization": f"Bearer {st.session_state.token}"}
        user = requests.get(f"{API_URL}/me", headers=headers).json()
        st.success(f"Logged in as {user['email']}")
        
        # Usage
        usage = requests.get(f"{API_URL}/usage", headers=headers).json()
        st.progress(usage["percentage"] / 100)
        st.caption(f"{usage['tokens_used']:,} / {usage['tokens_limit']:,} tokens used ({usage['plan']} plan)")
        
        if st.button("Logout"):
            del st.session_state.token
            st.rerun()

# Main area
if "token" in st.session_state:
    headers = {"Authorization": f"Bearer {st.session_state.token}"}
    
    tab1, tab2, tab3 = st.tabs(["💬 Chat", "📄 Documents", "⚙️ Settings"])
    
    with tab1:
        st.header("Chat with your documents")
        
        # Chat interface
        if "messages" not in st.session_state:
            st.session_state.messages = []
        
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
        
        if prompt := st.chat_input("Ask anything..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            with st.chat_message("user"):
                st.write(prompt)
            
            # Call API
            with st.spinner("Thinking..."):
                response = requests.post(
                    f"{API_URL}/chat",
                    json={"message": prompt},
                    headers=headers
                )
                answer = response.json()["response"]
            
            st.session_state.messages.append({"role": "assistant", "content": answer})
            with st.chat_message("assistant"):
                st.write(answer)
    
    with tab2:
        st.header("Your documents")
        
        # Upload
        uploaded_file = st.file_uploader("Upload PDF or Markdown", type=["pdf", "md"])
        if uploaded_file:
            with st.spinner("Processing..."):
                files = {"file": uploaded_file}
                response = requests.post(f"{API_URL}/documents/upload", files=files, headers=headers)
                if response.ok:
                    st.success("Document uploaded!")
        
        # List docs
        docs = requests.get(f"{API_URL}/documents", headers=headers).json()
        for doc in docs:
            col1, col2 = st.columns([4, 1])
            col1.write(f"📄 {doc['filename']}")
            if col2.button("Delete", key=doc['id']):
                requests.delete(f"{API_URL}/documents/{doc['id']}", headers=headers)
                st.rerun()
    
    with tab3:
        st.header("Settings")
        
        st.subheader("Upgrade Plan")
        current_plan = usage["plan"]
        st.info(f"Current plan: **{current_plan.upper()}**")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### Free")
            st.markdown("- 10K tokens/month")
            st.markdown("- 5 documents")
            st.markdown("- 1 workspace")
        
        with col2:
            st.markdown("### Pro")
            st.markdown("- 100K tokens/month")
            st.markdown("- 100 documents")
            st.markdown("- 5 workspaces")
            if st.button("Upgrade to Pro - $19/mo"):
                requests.post(f"{API_URL}/billing/upgrade", json={"plan": "pro"}, headers=headers)
                st.success("Upgraded!")
        
        with col3:
            st.markdown("### Team")
            st.markdown("- 500K tokens/month")
            st.markdown("- Unlimited documents")
            st.markdown("- Unlimited workspaces")
            if st.button("Upgrade to Team - $49/mo"):
                requests.post(f"{API_URL}/billing/upgrade", json={"plan": "team"}, headers=headers)
                st.success("Upgraded!")
else:
    st.info("👈 Please login to continue")
```

**Run:**
```bash
streamlit run ui/app.py
```

**Martes (1.5h):** Landing page
Usa [Vercel templates](https://vercel.com/templates/next.js/nextjs-portfolio-starter) o crea HTML simple:
```html
<!-- landing.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DocuChat Pro - AI-Powered Document Q&A</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50">
    <nav class="bg-white shadow">
        <div class="max-w-7xl mx-auto px-4 py-4 flex justify-between">
            <h1 class="text-2xl font-bold text-blue-600">📄 DocuChat Pro</h1>
            <div>
                <a href="/app" class="bg-blue-600 text-white px-4 py-2 rounded">Get Started</a>
            </div>
        </div>
    </nav>
    
    <header class="max-w-5xl mx-auto text-center py-20">
        <h2 class="text-5xl font-bold mb-4">Chat with Your Documents Using AI</h2>
        <p class="text-xl text-gray-600 mb-8">Upload PDFs, ask questions, get instant answers with citations.</p>
        <a href="/app" class="bg-blue-600 text-white px-8 py-3 rounded-lg text-lg">Try it Free</a>
    </header>
    
    <section class="max-w-6xl mx-auto py-16 grid md:grid-cols-3 gap-8 px-4">
        <div class="bg-white p-8 rounded-lg shadow">
            <h3 class="text-2xl font-bold mb-4">⚡ Lightning Fast</h3>
            <p class="text-gray-600">Get answers in seconds using advanced RAG technology.</p>
        </div>
        <div class="bg-white p-8 rounded-lg shadow">
            <h3 class="text-2xl font-bold mb-4">🔒 Secure</h3>
            <p class="text-gray-600">Your documents are encrypted and never used for training.</p>
        </div>
        <div class="bg-white p-8 rounded-lg shadow">
            <h3 class="text-2xl font-bold mb-4">👥 Team Collaboration</h3>
            <p class="text-gray-600">Share workspaces and documents with your team.</p>
        </div>
    </section>
    
    <footer class="bg-gray-900 text-white text-center py-8 mt-20">
        <p>© 2027 DocuChat Pro. Built by Marco Lopez.</p>
        <a href="https://github.com/yourusername/docuchat-pro" class="text-blue-400">GitHub</a>
    </footer>
</body>
</html>
```

**Miércoles (1.5h):** Deploy a AWS
- ECS Fargate setup (más fácil que EC2)
- RDS PostgreSQL
- S3 para docs
- CloudFront (CDN) para UI

```bash
# Usando AWS Copilot CLI (tool oficial para ECS)
brew install aws/tap/copilot-cli

# Initialize app
copilot app init docuchat-pro

# Deploy backend
copilot svc init --name api --svc-type "Load Balanced Web Service"
copilot svc deploy --name api

# Deploy frontend
copilot svc init --name ui --svc-type "Load Balanced Web Service"
copilot svc deploy --name ui
```

**Jueves (1h):** Custom domain + HTTPS
- Compra dominio en Namecheap (~$10/año) o usa .me gratis de GitHub Student
- Configure Route 53
- SSL con AWS Certificate Manager (gratis)

**Viernes (1.5h):** Analytics & Polish
- Google Analytics
- Posthog (analytics + session replay)
- Final testing
- Video demo (Loom)
- Update README

### ✅ Checklist del Proyecto Final

- [ ] Backend API completo con auth
- [ ] Usage tracking & limits por plan
- [ ] Pricing tiers implementados
- [ ] Frontend funcional (Streamlit o Next.js)
- [ ] Landing page atractiva
- [ ] Deployed en AWS
- [ ] Custom domain con HTTPS
- [ ] CI/CD pipeline funcional
- [ ] Tests (al menos smoke tests)
- [ ] Monitoring (Langfuse + Sentry)
- [ ] README profesional con screenshots
- [ ] Video demo (~2min)
- [ ] Código en GitHub (público)

---

## 🎯 SEMANAS 35-40: Preparación Entrevistas & Portfolio (Jul-Ago)

### SEMANA 35: System Design para AI Engineers

**Objetivo:** Prepararte para preguntas de diseño de sistemas en entrevistas.

**Temas a estudiar:**
- Cómo diseñarías un sistema de RAG escalable
- Trade-offs: latency vs accuracy
- Caching strategies
- Load balancing para LLM APIs
- Cost optimization

**Recursos:**
- [System Design Interview](https://www.youtube.com/c/SystemDesignInterview) canal YouTube
- [Grokking the System Design Interview](https://www.educative.io/courses/grokking-the-system-design-interview)

**Práctica:**
Dibuja diagramas de arquitectura para:
1. Sistema de chatbot para 10M usuarios
2. Document Q&A para empresa Fortune 500
3. AI code assistant (tipo GitHub Copilot)

### SEMANAS 36-37: LeetCode & Coding Interviews

**Objetivo:** Refrescar algoritmos y estructuras de datos.

**Enfoque:** No necesitas ser expert, pero sí resolver mediums cómodamente.

**Rutina:**
- 1 problema/día (30min)
- Enfócate en estos patterns:
  - Arrays & Strings
  - Hash Maps
  - Binary Search
  - Two Pointers
  - BFS/DFS básico

**Plataforma:** [NeetCode](https://neetcode.io/) - lista curada de 150 problemas

### SEMANA 38: Mock Interviews

**Objetivo:** Practicar entrevistas reales.

**Plataformas:**
- [Pramp](https://www.pramp.com/) - mock interviews gratis
- [Interviewing.io](https://interviewing.io/) - con ingenieros de FAANG

**Prepara:**
- "Tell me about yourself" (2min pitch)
- "Walk me through a project" (elige DocuChat Pro)
- "Tell me about a technical challenge you faced"

### SEMANAS 39-40: Portfolio & Networking

**Portfolio website:**
Crea web personal con:
- Intro (quién eres, qué haces)
- Projects (3 proyectos destacados con demos)
- Blog (opcional, 2-3 posts técnicos)
- Contact

**Usa:**
- [Next.js Portfolio Template](https://vercel.com/templates/next.js/nextjs-portfolio-starter)
- Deploy en Vercel (gratis)
- Custom domain (tu-nombre.dev)

**Networking en Madrid:**
- [Madrid AI Meetup](https://www.meetup.com/es-ES/topics/artificial-intelligence/es/madrid/)
- [PyData Madrid](https://www.meetup.com/es-ES/PyData-Madrid/)
- [Startup Grind Madrid](https://www.startupgrind.com/madrid/)
- Conferencias: [Commit Conf](https://commit-conf.com/), [PyCon España](https://2024.es.pycon.org/)

**LinkedIn:**
- Update perfil con proyectos
- Post sobre lo que aprendes (1-2 posts/semana)
- Conecta con recruiters de AI/ML en Madrid
- Comenta en posts de empresas que te interesan

---

## 💼 SEMANAS 41-48: Job Search & Applications (Ago-Sep)

### SEMANA 41-42: Target Companies & Preparation

**Empresas AI en Madrid (mix de startups y corporates):**

**Startups/Scale-ups:**
- [Clarity AI](https://clarity.ai/) - Sustainability AI
- [Jobandtalent](https://www.jobandtalent.com/) - HR AI
- [Source{d}](https://sourced.tech/) - AI for code
- [Spotahome](https://www.spotahome.com/) - PropTech
- [Cabify](https://cabify.com/) - AI en movilidad
- [Glovo](https://glovoapp.com/) - delivery + AI

**Consultoras con AI practice:**
- Accenture Applied Intelligence
- Deloitte AI
- EY AI
- PwC AI Labs
- Capgemini

**Corporates con equipos AI:**
- BBVA (AI Factory)
- Telefónica (Aura - AI assistant)
- Repsol (AI para energía)
- Banco Santander (AI team)

**Remoto desde Madrid:**
- Startups europeas (busca en [Wellfound](https://wellfound.com/))
- US companies hiring EU remote

**Cómo aplicar:**
1. **LinkedIn:** Busca "AI Engineer Madrid" - aplica directo
2. **AngelList / Wellfound:** Startups tech
3. **InfoJobs / Indeed:** Empresas grandes
4. **Direct:** Envía email a CTOs de startups pequeñas (más responden de lo que piensas)
5. **Referrals:** Pide a tus contactos que te refieran

### SEMANAS 43-46: Applications & Interviews

**Meta:**
- 5 aplicaciones/semana mínimo
- Follow-up después de 1 semana si no responden
- Trackea en spreadsheet (empresa, rol, fecha aplicación, status)

**Proceso típico:**
1. **Screening call** (30min) con recruiter - fit cultural, motivación
2. **Technical interview** (1h) - live coding + system design
3. **Project review** (1h) - presentas tus proyectos, deep dive técnico
4. **Final interview** (1h) - con CTO o lead, más técnico + fit
5. **Offer** 🎉

**Prepara respuestas para:**
- "Why AI engineering?"
- "Difference between ML Engineer and AI Engineer?"
- "How do you evaluate RAG systems?"
- "Describe a time you debugged a production issue"
- "How do you stay updated with AI advancements?"

### SEMANAS 47-48: Offer Negotiation & Onboarding Prep

**Salaries en Madrid (2027, junior AI Engineer):**
- Startups pequeñas: 30-40K€
- Scale-ups: 40-50K€
- Consultoras: 35-45K€
- Corporates: 40-50K€
- Remoto EU: 45-60K€

**Negociación:**
- Siempre pide más (10-15% sobre initial offer)
- Si no pueden subir salary, pide: más vacation, remote days, learning budget, equity
- No aceptes la primera offer inmediatamente (tómate 2-3 días)

**Red flags en offers:**
- No remote (en 2027 es raro)
- No mention de learning budget
- "Startup equity" sin explicar vesting schedule
- Salario <30K en Madrid para AI Engineer

**Una vez aceptes:**
- Prepara tu setup (laptop, monitor si WFH)
- Revisa codebase (si es open source)
- Lee docs de la empresa
- Conecta con tu future team en LinkedIn

---

## 🎓 Recursos Generales de Estudio

### Canales de YouTube imprescindibles
- [AI Jason](https://www.youtube.com/@AIJason) - AI engineering tutorials
- [Sam Witteveen](https://www.youtube.com/@samwitteveenai) - LangChain expert
- [Prompt Engineering](https://www.youtube.com/@engineerprompt) - LLM workflows
- [TechWithTim](https://www.youtube.com/@TechWithTim) - Python projects

### Blogs/Newsletters
- [The Batch (Andrew Ng)](https://www.deeplearning.ai/the-batch/) - AI news
- [LangChain Blog](https://blog.langchain.dev/)
- [OpenAI Cookbook](https://cookbook.openai.com/)
- [Hamel's Blog](https://hamel.dev/) - AI engineering

### Libros (NO leer cover-to-cover, úsalos como referencia)
- "Designing Data-Intensive Applications" - Martin Kleppmann
- "Hands-On Large Language Models" - Jay Alammar

### Podcasts (para el gym/transporte)
- Latent Space - AI Engineer podcast
- Practical AI
- The TWIML AI Podcast

---

## 📊 Tracking Your Progress

**Crea un Notion dashboard con:**

1. **Weekly tracker:**
   - Semana #
   - Objetivo
   - Horas trabajadas
   - Status (⏳ in progress, ✅ done)
   - Notas

2. **Projects:**
   - Project 1: CLI AI Assistant - [GitHub link] - Status
   - Project 2: Docs Q&A Platform - [GitHub link] [Demo] - Status
   - Project 3: Production Support Bot - [GitHub link] [Demo] - Status
   - Project 4: DocuChat Pro SaaS - [GitHub link] [Live site] - Status

3. **Skills matrix:**
   | Skill | Level (1-5) | Last used |
   |-------|-------------|-----------|
   | Python | 4 | Week 40 |
   | FastAPI | 4 | Week 34 |
   | RAG | 3 | Week 30 |
   | LangGraph | 3 | Week 25 |
   | AWS | 2 | Week 32 |
   | ... | | |

4. **Job applications tracker:**
   | Company | Role | Applied | Status | Next step |
   |---------|------|---------|--------|-----------|
   | Clarity AI | AI Eng | 2027-08-15 | Interview scheduled | Prepare system design |
   | ... | | | | |

---

## ✅ Final Checklist - ¿Estás listo para el mercado?

Antes de empezar a aplicar fuerte (semana 41+), verifica:

### Portfolio
- [ ] 3-4 proyectos sólidos en GitHub (README profesional, deployed demos)
- [ ] Portfolio website personal (tu-nombre.dev)
- [ ] LinkedIn actualizado y activo
- [ ] Al menos 1 post técnico/blog (demuestra que sabes comunicar)

### Skills técnicas
- [ ] Puedes construir una API FastAPI desde cero en <2h
- [ ] Entiendes RAG end-to-end (embedding, retrieval, reranking, evaluation)
- [ ] Has usado LangGraph para workflows complejos
- [ ] Sabes deployar en AWS (EC2, RDS, S3, ECS)
- [ ] Tienes CI/CD funcional en al menos 1 proyecto
- [ ] Has integrado monitoring (Langfuse) y error tracking (Sentry)

### Soft skills
- [ ] Puedes explicar tus proyectos claramente en 5min
- [ ] Tienes respuestas preparadas para behavioral questions
- [ ] Sabes dibujar arquitecturas en whiteboard (o Excalidraw)
- [ ] Has hecho al menos 2 mock interviews

### Ecosystem awareness
- [ ] Sigues a líderes de AI en Twitter/LinkedIn
- [ ] Has asistido a al menos 1 meetup en Madrid
- [ ] Conoces qué empresas están contratando AI engineers
- [ ] Sabes qué salario pedir

---

## 🚨 Troubleshooting & FAQs

### "No llego a las 6h semanales"
→ Está bien. Mejor 4h consistentes que 8h un día y luego nada.
→ Lo que importa es el momentum. No rompas la racha.

### "Este proyecto es muy difícil, me atasco"
→ Google + ChatGPT son tus amigos. El 80% del trabajo real es googlear errores.
→ Si llevas >2h atascado, salta a la siguiente sección y vuelve después.
→ Pregunta en Discord de LangChain o r/LangChain en Reddit.

### "No encuentro tiempo con el Master"
→ Reduce el scope de proyectos (haz versiones más simples).
→ Reutiliza código entre proyectos (DRY).
→ Prioriza construir sobre estudiar. Un proyecto medio terminado > 10 tutoriales vistos.

### "¿Debo aprender X nueva tecnología que acaba de salir?"
→ Probablemente no. Hay nuevas tools cada semana.
→ Enfócate en fundamentos: Python, APIs, RAG, agents, deployment.
→ Solo aprende algo nuevo si 3+ job posts que te interesan lo piden.

### "¿Cuándo empiezo a aplicar a trabajos?"
→ NO esperes a "estar listo". Nadie está listo.
→ Empieza a aplicar cuando tengas:
  - 2 proyectos desplegados
  - Portfolio website
  - LinkedIn actualizado
→ Las primeras entrevistas son práctica. Está bien fallar.

### "¿Qué hago si no consigo trabajo en septiembre?"
→ No pasa nada. El mercado es difícil.
→ Continúa construyendo proyectos y aplicando.
→ Considera freelance en Upwork/Fiverr (construir MVPs con AI para startups).
→ Aplica a posiciones de "Python Developer" o "Backend Developer" y luego pivota internamente a AI.

---

## 🎯 Mentalidad y Motivación

**Este roadmap es LARGO. 11 meses es mucho tiempo.**

**Tips para mantener momentum:**

1. **Celebra wins pequeños:** Terminaste una semana → tweet sobre ello. Deployaste un proyecto → post en LinkedIn. Cada win cuenta.

2. **Documenta tu viaje:** Escribe qué aprendiste cada semana. Futuro tú lo agradecerá. Y es contenido para LinkedIn/blog.

3. **No compares tu progreso con otros:** Twitter está lleno de "I built X in 2 hours". Es mentira o tienen 10 años de experiencia. Tu progreso es tuyo.

4. **Encuentra un accountability buddy:** Alguien haciendo algo similar. Check-in semanal. "¿Qué hiciste esta semana?" Se ayudan mutuamente.

5. **Recuerda el por qué:** ¿Por qué quieres ser AI Engineer? Escríbelo. Leelo cuando estés desmotivado.

6. **Rest is productive:** Si una semana estás quemado, tómate descanso. Mejor 1 semana off que burnout y abandonar.

7. **Adjust el plan si es necesario:** Esto no es una biblia. Si encuentras algo mejor, cambia. Si algo no funciona, ajusta. Es TU roadmap.

---

## 🙌 Conclusión

Marco, tienes todo lo que necesitas aquí:
- 48 semanas de contenido detallado
- 4 proyectos progresivos
- Recursos específicos para cada skill
- Plan de preparación para entrevistas
- Estrategia de job search

**Lo único que falta eres tú ejecutando.**

Hoy es 8 de octubre de 2026.
En 11 meses (septiembre 2027) vas a estar:
- Trabajando como AI Engineer en Madrid
- Con portfolio que impresiona
- Ganando dinero construyendo cosas con AI
- Siendo el tipo que sus amigos de IE le preguntan "¿cómo le hiciste?"

**La diferencia entre conseguirlo y no conseguirlo es simple:**
→ Consistencia.
→ 6 horas/semana, cada semana, durante 11 meses.
→ No "motivación". Disciplina.

**You got this. Ahora a ejecutar. 🚀**

---

**Última cosa:** Guarda este documento en Notion/Obsidian/lo que uses. Márcalo cuando completes cada semana. En septiembre 2027, cuando estés firmando tu contrato, vuelve a leerlo y verás el camino que recorriste.

Mucha suerte. Y si llegas a conseguir trabajo con este roadmap, mándame un mensaje. Me encantaría saber que funcionó. 💪

---

*Documento creado: Octubre 2026*
*Autor: Claude (con cariño para Marco)*
*Versión: 2.0 - Complete Edition*