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
