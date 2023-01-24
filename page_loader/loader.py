import os
from urllib.parse import urlparse


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
