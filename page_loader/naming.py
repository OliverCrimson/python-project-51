import os.path
from urllib.parse import urlparse


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


def flatter_paths(path_like):
    no_pref = path_like.removeprefix('/')
    devided = os.path.splitext(no_pref)
    stripped = change_name(devided[0])
    if devided[1]:
        return stripped + devided[1]
    else:
        result = change_name(devided[0])
        return result + '.html'


def correcting_links(item_link, original_link):
    x = urlparse(item_link).path
    y = urlparse(original_link).netloc
    result = f'{y}{x}'
    return result
