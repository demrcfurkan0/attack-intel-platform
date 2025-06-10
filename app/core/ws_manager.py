from fastapi import WebSocket
from typing import Dict, List
import json

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, simulation_id: str):
        await websocket.accept()
        self.active_connections[simulation_id] = websocket
        print(f"WebSocket bağlandı: {simulation_id}")

    def disconnect(self, simulation_id: str):
        if simulation_id in self.active_connections:
            del self.active_connections[simulation_id]
            print(f"WebSocket bağlantısı kesildi: {simulation_id}")

    async def send_json_update(self, simulation_id: str, data: dict):
        if simulation_id in self.active_connections:
            websocket = self.active_connections[simulation_id]
            try:
                await websocket.send_json(data)
            except Exception as e:
                print(f"WebSocket gönderme hatası ({simulation_id}): {e}")
                # Hata durumunda bağlantıyı kesebiliriz
                self.disconnect(simulation_id)

manager = ConnectionManager()