import os.path
from urllib.parse import urlparse


def change_name(link):
    no_scheme = urlparse(link).netloc + urlparse(link).path
    result = no_scheme.replace('/', '-').replace('.', '-')
    return result


def to_dir(link):
    result = f'{change_name(link)}_files'
    return result


def to_file(path_like):
    no_pref = path_like.removeprefix('/')
    divided = os.path.splitext(no_pref)
    stripped = change_name(divided[0])
    if divided[1]:
        return stripped + divided[1]
    else:
        result = change_name(divided[0])
        return result + '.html'


def correcting_links(item_link, original_link):
    x = urlparse(item_link).path
    y = urlparse(original_link).netloc
    result = f'{y}{x}'
    return result


def is_local(link, item):
    splitted = urlparse(item)
    parsed_link = urlparse(link)
    if splitted.netloc == parsed_link.netloc:
        return splitted
    if splitted.netloc == '':
        return splitted
