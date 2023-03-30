import requests
import json

url = 'https://sk-chatgpt-4-5.onrender.com'


def story(prompt):
    payload = {'prompt': prompt}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        bot_response = response.json()['bot']
        return bot_response
    else:
        return 'Error in generating story.'
