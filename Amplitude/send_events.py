import requests
import json
import os

def send_event(additional_data):
    api_key = os.environ["AMPL_API"]
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*'
    }

    data = {"api_key": api_key}
    data["events"] = additional_data

    response = requests.post('https://api2.amplitude.com/2/httpapi',
                             headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("Успех:", response.json())
    else:
        print("Ошибка:", response.text)
