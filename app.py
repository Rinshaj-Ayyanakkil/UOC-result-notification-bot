import time
from bot import broadcast_message
from scrapper import search_results

def main():
    while(True):
        print("checking...")
        new_results = search_results()
        if new_results:
            broadcast_message(new_results)
        time.sleep(900)

if __name__=="__main__":
    print("starting...")
    main()