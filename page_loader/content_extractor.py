# import html.parser
# from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import logging
import requests
from progress.bar import PixelBar

from page_loader.loader import namin, normalize_string



def replacin(item):
    res = urlparse(item)
    joined = res.path
    joined = joined.replace('/', '-')[1:]
    if '.' not in joined:
        joined += ".html"
        return joined
    else:
        return joined


def img_links_array(array, link):
    form_array = []
    for i in array:
        form_array.append(urljoin(link, i))
    return form_array


def downloading_imgs(link, array, path):
    # path_for_html = f'{change_name(link)}_files/{}'
    if len(array):
        with PixelBar('Downloading', max=len(array)) as bar:
            for item in array:
                parsed = urlparse(item)
                with open(f"{path}/{namin(link)[:-5]}-"
                          f"{normalize_string(parsed.path)}", 'wb') as file:
                    file.write(requests.get(item).content)
                    logging.info(f"item {path}/{namin(link)[:-5]}-"
                                 f"{replacin(parsed.path)}")
                bar.next()
    else:
        logging.info('Nothing to download')

