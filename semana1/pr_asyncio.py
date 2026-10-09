import asyncio 

async def cocinar():
    print("Cocinando...")
    await asyncio.sleep(2)
    print("Comida lista!")

async def servir():
    print("Llevando a la mesa...")
    await asyncio.sleep(1)
    print("Comida Servida!")

async def comer():
    print("Comiendo...")
    await asyncio.sleep(3)
    print("Comida terminada!")

async def main():
    print("Empezando servicio de comida")

    await asyncio.gather(
        cocinar(),
        servir(),
        comer()
    )

    print("Acabamos servicio de comida")

if __name__ == "__main__":
    asyncio.run(main())
    