import requests

# Din Home Assistant URL
url = "http://192.168.50.11:8123/api/services/notify/mobile_app_maste"

# Din Long-lived access token för autentisering
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhYWFkZWUwY2E4MWQ0OGViOTEyNTIwMDI0MzYwZjZhOCIsImlhdCI6MTcyNjI0NjAxOSwiZXhwIjoyMDQxNjA2MDE5fQ.KfGA5xtbGplbRZo_EgKu5i0MdGpWp5CmU7o6qW0H8Dg",
    "content-type": "application/json",
}

# Data som skickas i notisen
data = {
    "message": "Detta är en notis från min dator!",
    "title": "Notis från Datorn",
    "data": {
        "actions": [
            {
                "action": "yes_action",
                "title": "Ja"
            },
            {
                "action": "no_action",
                "title": "Nej"
            }
        ]
    }
}

# Skicka POST-begäran
response = requests.post(url, headers=headers, json=data)

# Kontrollera resultatet
if response.status_code == 200:
    print("Notisen skickades!")
else:
    print(f"Fel: {response.status_code}")
