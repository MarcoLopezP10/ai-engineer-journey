import asyncio
from pydantic import BaseModel, HttpUrl
from typing import List
import random

class Post(BaseModel): #Modelo Pydantic para representar un post
    id: int
    title:str
    body:str
    url: HttpUrl

async def fetch_post(post_id: int) -> Post: #Simula la obtención de un post desde una API
    #Simulando llamada a una API
    await asyncio.sleep(random.uniform(0.5,2.0))
    #Simulando datos de respuesta
    post_data={"id": post_id, "title": f"Post {post_id}", 
                "body": f"Contenido del post {post_id}", 
                "url": f"https://jsonplaceholder.typicode.com/posts/{post_id}"}
    return Post(**post_data)

async def fetch_posts(post_ids: List[int]) -> List[Post]: #Simula la obtención de múltiples posts desde una API de forma asíncrona
    tasks = [fetch_post(post_id)for post_id in post_ids]
    return await asyncio.gather(*tasks)

async def main():
    post_ids=[1,2,3,4,5]
    posts=await fetch_posts(post_ids=post_ids)
    for post in posts:
        print(post)

if __name__ == "__main__":
    asyncio.run(main())

