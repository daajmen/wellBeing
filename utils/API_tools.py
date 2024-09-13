from secret import API_KEY
import requests


# Din Long-lived access token för autentisering
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "content-type": "application/json",
}


def sendCommandToPhone(phone): 
    url = "http://192.168.50.11:8123/api/services/notify/mobile_app_" + phone
    return url

def sendData(data,phone):
    # Skicka POST-begäran
    response = requests.post(sendCommandToPhone(phone), headers=headers, json=data)  
    if response.status_code == 200:
        print("Notisen skickades!")
    else:
        print(f"Fel: {response.status_code}")


def NotifySleepWell(phone):
    data = {
        "message": "Har du sovit gott?",
        "title": "Sleep well notis",
        "data": {
            "actions": [
                {
                    "action": "sleepWell_yes",
                    "title": "Ja"
                },
                {
                    "action": "sleepWell_no",
                    "title": "Nej"
                }
            ]
        }
    }
    sendData(data,phone)

def NotifyFood(phone):
    data = {
        "message": "Mat",
        "title": "Har du ätit precis, logga klockslag?",
        "data": {
            "actions": [
                {
                    "action": "Food_yes",
                    "title": "Ja",
                    "authenticationRequired": "1234"
                }
            ]
        }
    }
    sendData(data,phone)

def NotifyWorkday(phone):
    data = {
        "title": "Jobb",
        "message": "Hur har jobbet varit idag?",
        "data": {
            "actions": [
                {
                    "action": "work_good",
                    "title": "Bra",
                },
                {
                    "action": "work_bad",
                    "title": "Dåligt",
                    "activationMode": "foreground",
                }               
            ]
        }
    }
    sendData(data,phone)
