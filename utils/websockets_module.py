import asyncio
import websockets
import json
from secret import API_KEY
from utils.database import insert_event

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
            print(f"Mottagen händelse: {event}")  # Skriv ut hela event-strukturen för felsökning

            # Hantera olika typer av meddelanden
            if event.get('type') == 'event':
                # Detta är en faktisk händelse, extrahera datan
                event_data = event['event']
                event_type = event_data.get('event_type', 'unknown')
                action = event_data.get('data', {}).get('action', 'unknown')
                user_id = event_data.get('context', {}).get('user_id', 'unknown')
                time_fired = event_data.get('time_fired', 'unknown')

                # Lagra i SQLite-databasen
                insert_event(event_type, action, user_id, time_fired)
            else:
                # Detta är ett system- eller autentiseringsmeddelande, hantera det separat
                print(f"Icke-händelsemeddelande mottaget: {event['type']}")
