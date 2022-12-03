import sys

import requests
from bs4 import BeautifulSoup
# from urllib.parse import urlparse
import logging


def requesting(link):
    respond = requests.get(link)
    if respond.status_code != 200:
        logging.warning(f"respond status code: "
                        f"{respond.status_code}")
        sys.exit(1)
    soup = BeautifulSoup(respond.content, 'html.parser')
    return soup