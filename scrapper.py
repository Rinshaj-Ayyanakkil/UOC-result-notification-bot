from typing import Union
from bs4.element import ResultSet
from requests_html import HTML, HTMLSession
from config import exam_result_url
from bs4 import BeautifulSoup


URL = exam_result_url
last_result = {"id": "9334"}

session = HTMLSession()

# function to fetch all the CUCBCSS results
def get_all_results() -> ResultSet:
    res = session.post(URL, data={"cour_id": 15})
    html: HTML = res.html

    soup = BeautifulSoup(html.html, "html.parser")
    results = soup.find_all("a", {"class": "am"})
    return results


def is_result_updated(results) -> bool:
    # check if the last result id is changed
    if last_result["id"] != results[0]["id"]:
        return True
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
        if exam_name.find("B.Sc (CUCBCSS UG)") != -1:
            new_cs_results.append(exam_name)

    # update the last result id with latest result id
    last_result["id"] = results[0]["id"]
    return new_cs_results
