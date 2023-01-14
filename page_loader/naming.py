import os.path
from urllib.parse import urlparse

# import pathlib
#
# from page_loader.loader import namin
#
# from page_loader.content_extractor import replacin


def change_name(link):
    no_scheme = urlparse(link).netloc + urlparse(link).path
    result = no_scheme.replace('/', '-').replace('.', '-')
    return result


def normalize_links(link):
    splitted = os.path.splitext(link)
    first_part = change_name(splitted[0])
    second_part = splitted[1]
    if '.' not in second_part:
        second_part += '.html'
    result = first_part + second_part
    return result
    

def naming_folders(link):
    result = f'{change_name(link)}_files'
    return result

# x = 'https://site.com/blog/about'
# print(naming_folders(x))