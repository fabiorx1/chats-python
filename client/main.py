import requests
import json
import asyncio
import websockets

HUB_URL = "http://localhost:5000"

def ler_hosts():
    response = requests.get(f"{HUB_URL}/hosts")
    addresses = json.loads(response.content)
    return addresses

async def iniciar_cliente(address):
    async with websockets.connect(f"ws://{address}") as websocket:
        while True:
            message = input("Mensagem: ")
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Resposta: {response}")

async def main():
    addresses = ler_hosts()
    address = addresses[0]
    print(address)
    await iniciar_cliente(address)

if __name__ == "__main__":
    asyncio.run(main())