import time
from bot import broadcast_message
from scrapper import search_results
from datetime import datetime

def main():
    while(True):
        print("checking...")
        broadcast_message("testing"+datetime.now())
        new_results = search_results()
        message:str = ""
        if new_results:
            for result in new_results:
                message += f"<b>{result}</b>\n"
            message += """<a href='http://results.uoc.ac.in'>See Results</a>"""
            broadcast_message(message)
        time.sleep(60)

if __name__=="__main__":
    print("starting...")
    main()