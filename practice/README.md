# Practice Log

Weekly exercises from my [AI Engineer roadmap](../README.md). Each folder contains the code written during that week.

---

## Week 1: Asynchronous Python and Pydantic

- [`async_data_fetcher.py`](semana1/async_data_fetcher.py): concurrent execution of simulated API calls with `asyncio.gather`, validating each response with Pydantic models.
- [`pr_asyncio.py`](semana1/pr_asyncio.py), [`pr_pydantic.py`](semana1/pr_pydantic.py): exercises on concurrency and data modeling.

## Week 2: REST APIs with FastAPI

- [`miniCRUD_API.py`](semana2/miniCRUD_API.py): full CRUD API (GET, POST, PUT, DELETE) with input validation, HTTP error handling and auto-generated OpenAPI documentation.
- [`helloworldAPI.py`](semana2/helloworldAPI.py), [`endpointsAPI.py`](semana2/endpointsAPI.py): introductory FastAPI endpoints.

## Week 3: Testing and version control

- [`testsCRUD-API.py`](semana3/testsCRUD-API.py): test suite for the Week 2 API using `pytest` and FastAPI's `TestClient`.
- [`simpleTests.py`](semana3/simpleTests.py): Pytest basics.
- Branch-based Git workflow.

## Week 4: LLM fundamentals

- [`chatbot.py`](semana4/chatbot.py): command-line chatbot with conversation memory and Markdown output (`rich`). Falls back to other Gemini models when one is overloaded (503), rate-limited (429) or times out.
- [`asistente_formal.py`](semana4/asistente_formal.py), [`asistente_casual.py`](semana4/asistente_casual.py), [`asistente_tecnico.py`](semana4/asistente_tecnico.py): the same question asked with three different system prompts, to compare how each one changes tone, length and structure.
- [`helloworldOpenAI.py`](semana4/helloworldOpenAI.py): first call to Gemini through the OpenAI SDK, reading the API key from `.env`.

## Week 5: Prompt engineering

In progress.

---

## Running locally

From the repository root:

```bash
python -m venv .venv && source .venv/bin/activate
pip install fastapi uvicorn pydantic pytest httpx

# Week 2 API (docs at http://127.0.0.1:8000/docs)
uvicorn practice.semana2.miniCRUD_API:app --reload

# Week 3 tests
python -m pytest practice/semana3/testsCRUD-API.py
```

Week 4 needs a `GOOGLE_API_KEY` in a `.env` file at the repository root, and the dependencies from `pyproject.toml`:

```bash
uv sync
uv run python practice/semana4/chatbot.py
```
