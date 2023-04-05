import asyncio
import websockets
import requests

async def protocolo(websocket, path):
    async for message in websocket:
        print(f"Mensagem: {message}.")
        response_message = input("Resposta: ") # Prompt user for response message
        await websocket.send(response_message)

async def iniciar_servidor(port):
    async with websockets.serve(protocolo, "localhost", port):
        print(f"WebSocket rodando na porta {port}")
        await asyncio.Future()  # keep the server running

if __name__ == "__main__":
    # Start the WebSocket server on port 8765
    port = 8765
    try: 
        # registra o IP no servidor
        response = requests.post("http://localhost:5000/registro", data={"port": port})
        print(response.json())
        
        # começa o loop infinito do Chat
        asyncio.get_event_loop().run_until_complete(iniciar_servidor(port))
    except Exception as e:
        print('Exception:', e)
        ...
    finally:
        # remove o endereço da lista do hub
        response = requests.delete("http://localhost:5000/remover", data={"port": port})
        print(response.json())