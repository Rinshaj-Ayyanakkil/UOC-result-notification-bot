import logging
from typing import Union
import requests
from bs4 import BeautifulSoup
from config import LAST_RESULT_ID, exam_result_url

URL = exam_result_url
last_result = {"id": LAST_RESULT_ID}

logger = logging.getLogger("scrapper")

# function to fetch all the CUCBCSS results
def get_all_results():
    try:
        response = requests.post(URL, data={"cour_id": 15})

    except Exception as e:
        logger.error("Couldn't connect to " + URL)
        return []

    try:
        html = response.text

        soup = BeautifulSoup(html, "html.parser")
        results = soup.find_all("a", {"class": "am"})
        return results

    except Exception as e:
        logger.exception(e)

    return []


def is_result_updated(results) -> bool:
    # check if the last result id is changed
    try:
        if last_result["id"] != results[0]["id"]:
            return True

    except IndexError as e:
        logger.error("empty result")

    except Exception as e:
        logger.exception(e)

    return False


# check the results for BSc CS exam results
def search_results() -> Union[list, None]:
    results = get_all_results()

    # return none if result is not updated
    if not is_result_updated(results):
        return None

    new_cs_results = []
    for result_element in results:

        exam_name: str = result_element.text

        # check if result id hit the last result id
        if result_element["id"] == last_result["id"]:
            break

        # if the exam name of the result element contains 'BSC CS', it is added to the list
        if exam_name.find("B.Sc") != -1:
            new_cs_results.append(exam_name)

    # update the last result id with latest result id
    last_result["id"] = results[0]["id"]
    return new_cs_results
