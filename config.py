import os
from dotenv import load_dotenv

load_dotenv()
bot_token = os.environ.get("BOT_TOKEN")
random_url = "https://random-data-api.com/api/food/random_foo"
channel_id = os.environ.get("RESULT_CHANNEL_ID")
telegram_api_url=f"https://api.telegram.org/bot{bot_token}"
