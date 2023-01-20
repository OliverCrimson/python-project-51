import os
import pathlib
import re
import tempfile
import shutil
import requests_mock
from urllib.parse import urlparse, urljoin


def namin(address, folder=str(pathlib.Path.cwd())):
    string = ''
    # result = ''
    if address.startswith('http://'):
        string += str(address[7:])
    if address.startswith('https://'):
        string += address[8:]
    string = string.replace('.', '-')
    string = string.replace('/', '-')
    # if folder is not None:
    #     result = f"{folder}/{string}.html"
    # if folder is None:
    #     folder = str(pathlib.Path.cwd())
    #     result = f"{folder}/{string}.html"
    # return result
    return string + ".html"





def normalize_link(link):
    link_ = urlparse(link).netloc + urlparse(link).path
    return link_


def normalize_string(link):
    norm = normalize_link(link)
    arr = os.path.split(norm)
    first_part = arr[0].replace('/', '-').replace('.', '-')
    second_part = arr[1]
    if '.' not in second_part:
        result = first_part + '-' + second_part + '.html'
        return result
    else:
        return first_part + '-' + second_part

# print(normalize_string('assets/application.css'))
