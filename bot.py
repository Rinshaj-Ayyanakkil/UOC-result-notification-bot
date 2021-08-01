import requests
from config import bot_token, channel_id,telegram_api_url

TOKEN = bot_token
URL = telegram_api_url

# function to send a message to the cs result notification channel
def broadcast_message(messages):
    try:
        params = {'chat_id':channel_id, 'text': str(messages)}
        response = requests.post(URL + '/sendMessage', data=params)
        print(response.status_code)
    except Exception as e:
        print(e)
