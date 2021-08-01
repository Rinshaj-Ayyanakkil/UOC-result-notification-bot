from datetime import datetime
import requests
from config import bot_token, channel_id,telegram_api_url

TOKEN = bot_token
URL = telegram_api_url

def broadcast_message(message:str):
    try:
        params = {'chat_id':channel_id, 'text': message}
        response = requests.post(URL + '/sendMessage', data=params)
        print(response)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    print("starting")
    broadcast_message("hello testing. datetime:"+str(datetime.now()))