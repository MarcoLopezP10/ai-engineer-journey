"""
- Construir una "Mini CRUD API" completa:
  - GET, POST, PUT, DELETE
  - Con Pydantic models
  - Con manejo de errores
  - Documentado en /docs
  """

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

app=FastAPI(title="Mini CRUD API", description="API para manejar items con operaciones CRUD", version="1.0.0")

class Task(BaseModel):
    id: Optional[str] = None
    title: str
    description: Optional[str] = None
    completed: bool = False

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

@app.put("/tasks/{task_id}")
def update_task(task_id: str,task:Task):
    task.id=task_id
    tasks_db[task_id]=task
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    del tasks_db[task_id]
    return None

    


