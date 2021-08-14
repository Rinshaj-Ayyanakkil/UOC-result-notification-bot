import logging
import requests
from config import bot_token, channel_id, telegram_api_url

TOKEN = bot_token
URL = telegram_api_url

logger = logging.getLogger("bot")

# function to send a message to the cs result notification channel
def broadcast_message(message: str):
    try:
        params = {"chat_id": channel_id, "text": message, "parse_mode": "HTML"}
        response = requests.post(URL + "/sendMessage", data=params)

        if response.ok:
            data: dict = response.json()
            chat: dict = data["result"]["chat"]

            chat_type: str = chat["type"]
            if chat_type == "private":
                name = f"{chat['first_name']} {chat['last_name']}"
            else:
                name = f"chat['title']"

            log = f"Message send to {name}({chat_type})"
            logger.info(log)
        else:
            log = f"Message sending failed. error code: {response.status_code}"
            logger.error(log)
    except Exception as e:
        logger.exception(e)
