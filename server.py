from fastapi import FastAPI, WebSocket
from typing import List
import uvicorn
import json

app = FastAPI()

# Store WebSocket connections
active_connections: List[WebSocket] = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)

    try:
        while True:
            message = await websocket.receive_text()
            message_data = json.loads(message)
            await broadcast_message(message_data)
    except:
        active_connections.remove(websocket)

async def broadcast_message(message_data: dict):
    message = json.dumps(message_data)
    for connection in active_connections:
        await connection.send_text(message)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
