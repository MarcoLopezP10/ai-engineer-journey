# Ejercicio: Crear 3 modelos Pydantic (User, Product, Order) con validaciones
from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    id: int 
    name:str=Field(...,min_length=2,max_length=50)
    email: EmailStr

class Product(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=100)
    price: float = Field(..., gt=0)

class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int = Field(..., gt=0)

if __name__ == "__main__":
    #Instancias correctas
    user=User(id=1,name="Juan Perez",email="juan.perez@example.com")
    product=Product(id=1,name="Laptop",price=1200.50)
    order=Order(id=1,user_id=user.id,product_id=product.id,quantity=2)
    print("Usuario:", user)
    print("Producto:", product)
    print("Orden:", order)

    #Instancias con fallos
    try:
        user_invalid=User(id=2,name="",email="invalid_email")
    except Exception as e:
        print("Error al crear usuario inválido:", e)
    
