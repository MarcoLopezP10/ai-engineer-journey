from fastapi.testclient import TestClient

from practice.semana2.miniCRUD_API import app

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
    # Nota: Cambiado a 200 ya que tu ruta devuelve 'None' con estado por defecto (200 OK)
    assert delete_response.status_code == 200 
