
import logging
import sys

import requests
from bs4 import BeautifulSoup


def requesting(link):
    respond = requests.get(link)
    respond.raise_for_status()
    if respond.status_code != 200:
        logging.warning(f"respond status code: "
                        f"{respond.status_code}")
        sys.exit(1)
    soup = BeautifulSoup(respond.content, 'html.parser')
    return soup
