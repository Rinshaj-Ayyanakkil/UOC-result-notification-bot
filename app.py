import logging
import time
from config import sleep_interval
from bot import broadcast_message
from scrapper import search_results
import sys

logger = logging.getLogger()

screen_handler = logging.StreamHandler(stream=sys.stdout)
formatter = logging.Formatter(fmt="%(name)s - %(levelname)s: %(message)s")
screen_handler.setFormatter(formatter)

logger.addHandler(screen_handler)
logger.setLevel(logging.DEBUG)


def main():
    while True:
        logger.info("**checking**")
        try:
            new_results = search_results()
            message: str = ""
            if new_results:
                for result in new_results:
                    message += f"<b>{result}</b>\n\n"
                message += """<a href='http://results.uoc.ac.in'>See Results</a>"""
                broadcast_message(message)

            time.sleep(int(sleep_interval))
        except Exception as e:
            logger.exception(e)


if __name__ == "__main__":
    logger.info("starting...")
    main()
