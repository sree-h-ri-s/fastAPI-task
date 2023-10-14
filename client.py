import asyncio
import websockets
import json

async def send_and_receive_messages():
    async with websockets.connect("ws://localhost:8000/ws") as websocket:
        while True:
            message = input("Enter a message (or type 'exit' to quit): ")
            if message.lower() == "exit":
                break
            message_data = {"message": message}
            await websocket.send(json.dumps(message_data))
            response = await websocket.recv()
            response_data = json.loads(response)
            print("Received:", response_data)

asyncio.get_event_loop().run_until_complete(send_and_receive_messages())
