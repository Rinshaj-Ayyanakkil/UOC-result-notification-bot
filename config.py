import os
from dotenv import load_dotenv

load_dotenv()
bot_token = os.environ.get("BOT_TOKEN")
channel_id = os.environ.get("RESULT_CHANNEL_ID")
telegram_api_url=f"https://api.telegram.org/bot{bot_token}"
exam_result_url="http://results.uoc.ac.in/getlist.php"
sleep_interval=os.environ.get("SLEEP_INTERVAL")