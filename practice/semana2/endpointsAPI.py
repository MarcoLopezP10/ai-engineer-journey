from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

"""
Ejercicio: Crear API con 3 endpoints:
  - GET /items → devuelve lista de items
  - GET /items/{id} → devuelve item específico
  - POST /items → crea nuevo item
"""

items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
    {"id": 3, "name": "Item 3", "description": "This is item 3"},
]

# Definimos el modelo Pydantic necesario para el método POST
class NewItem(BaseModel):
    name: str
    description: str

@app.get("/items")
def get_items():
    return items

@app.get("/items/{id}")
def get_item(id: int): # <-- Corregido: primero la variable, luego el tipo
    # Buscamos el item cuyo campo "id" coincida exactamente con el recibido en la URL
    for item in items:
        if item["id"] == id:
            return item
            
    # Si recorre toda la lista y no lo encuentra, lanzamos un error 404 limpio
    raise HTTPException(status_code=404, detail="Item no encontrado")

@app.post("/items")
def post_item(item: NewItem): # <-- Añadimos el parámetro con el modelo
    # Calculamos el siguiente ID disponible de forma dinámica
    new_id = len(items) + 1 if items else 1
    
    # Creamos el nuevo diccionario juntando el ID con los datos recibidos
    created_item = {"id": new_id, "name": item.name, "description": item.description}
    
    # Lo agregamos a nuestra lista en memoria
    items.append(created_item)
    
    # Devolvemos el objeto recién creado
    return created_item
