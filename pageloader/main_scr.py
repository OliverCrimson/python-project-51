import html.parser

from progress.bar import Bar

from pageloader.images import replacin, img_links_array, downloading_imgs
from pageloader.mkfolders import folder_create
from pageloader.naming import change_name
from pageloader.request_module import requesting
from urllib.parse import urljoin, urlparse
import pathlib
import logging


CURRENT_DIR = pathlib.Path.cwd()


logging.basicConfig(format='%(levelname)s: %(message)s',
                    level=logging.INFO)
logging.info('fuck of nigga')


def main_func(link, folder=''):
    logging.info(f'requested url: {link}')
    name = change_name(link)
    folder_create(link, folder)
    response = requesting(link)
    imgs = response.find_all('img')
    links = response.find_all('link')
    scripts = response.find_all('script')
    lst, lst_links, script_links = [], [], []
    for tag in imgs:
        valid_link = urljoin(link, tag['src'])
        if urlparse(valid_link).netloc == urlparse(link).netloc:
            lst.append(tag['src'])
            tag['src'] = f"{name}_files/{replacin(tag['src'])}"
    for tag in links:
        valid_link = urljoin(link, tag['href'])
        if urlparse(valid_link).netloc == urlparse(link).netloc:
            lst_links.append(tag['href'])
            tag['href'] = f"{name}_files/{replacin(tag['href'])}"
    for tag in scripts:
        if tag.get('src'):
            valid_link = urljoin(link, tag['src'])
            if urlparse(valid_link).netloc == urlparse(link).netloc:
                script_links.append(tag['src'])
                tag['src'] = f"{name}_files/{replacin(tag['src'])}"
    with open(f"{folder}{name}_files/{name}.html", "w") as file:
        file.write(response.prettify())
        logging.info(f'write html file: {folder}_files/{name}')
    big_list = lst + lst_links + script_links
    result = img_links_array(big_list, link)
    downloading_imgs(link, result, folder)
    logging.info('downloading complete!')

# main_func('https://page-loader.hexlet.repl.co', 'scripts/')
