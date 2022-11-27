import sys

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import logging


def requesting(link):
    respond = requests.get(link)
    if respond.status_code != 200:
        sys.exit()
    logging.info(f'status code: {respond.status_code}')
    soup = BeautifulSoup(respond.content, 'html.parser')
    return soup


def soup_extracting_imges(obj):
    imgs = obj.find_all('img')
    list_of_img = []
    for item in imgs:
        list_of_img.append(item['src'])
    return list_of_img


def soup_extracting_links(obj):
    links = obj.find_all('link')
    list_of_links = []
    for item in links:
        list_of_links.append(item['href'])
    return list_of_links


def soup_extracting_scripts(obj):
    scripts = obj.find_all('script')
    list_of_scripts = []
    for item in scripts:
        list_of_scripts.append(item.get('src'))
    return list_of_scripts


def result(link):
    x = requesting(link)
    print(soup_extracting_imges(x))
    print(soup_extracting_links(x))
    print(soup_extracting_scripts(x))


def check_elem(link, item):
    lst = []
    for i in item:
        if urlparse(link).netloc == urlparse(i).netloc:
            lst.append(i)
    return lst
