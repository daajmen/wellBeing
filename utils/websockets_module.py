import asyncio
import websockets
import json
from secret import API_KEY

async def listen_to_events():
    uri = "ws://192.168.50.11:8123/api/websocket"
    async with websockets.connect(uri) as websocket:
        # Autentisera med token
        await websocket.send(json.dumps({
            "type": "auth",
            "access_token": API_KEY
        }))
        
        # Prenumerera på alla event som har att göra med notifikationer från mobile_app
        await websocket.send(json.dumps({
            "id": 1,
            "type": "subscribe_events",
            "event_type": "mobile_app_notification_action"
        }))

        while True:
            response = await websocket.recv()
            event = json.loads(response)
            print(f"Mottagen händelse: {event}")
