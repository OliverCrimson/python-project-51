import requests
from bs4 import BeautifulSoup


def requesting(link):
    respond = requests.get(link)
    respond.raise_for_status()
    soup = BeautifulSoup(respond.content, 'html.parser')
    return soup
