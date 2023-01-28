# import logging
# import sys

import requests
from bs4 import BeautifulSoup


def requesting(link):
    try:
        respond = requests.get(link)
        respond.raise_for_status()
        soup = BeautifulSoup(respond.content, 'html.parser')
        return soup
    except Exception as error:
        return error
    # if respond.status_code != 200:
    #     logging.warning(f"respond status code: "
    #                     f"{respond.status_code}")
    #     raise Exception
