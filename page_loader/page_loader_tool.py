import logging
from urllib.parse import urljoin, urlparse
import requests
from progress.bar import PixelBar
from page_loader.mkfolders import make_folder
from page_loader.naming import change_name, flatter_paths, correcting_links
from page_loader.request_module import requesting


def finding_tags(soup, link):
    search_data = [
        ('img', 'src'),
        ('link', 'href'),
        ('script', 'src')
    ]
    data_list = []
    for first, second in search_data:
        required = [
            (one_name, second) for one_name in soup(first)
            if one_name.get(second) is not None
        ]
        data_list.extend(required)
    items_list = []
    for actual, requested in data_list:
        if netloc_check(link, actual.get(requested)):
            url = actual.get(requested)
            name_for_item = change_name(link)
            changed_item_string = flatter_paths(correcting_links
                                                (actual[requested], link)
                                                )
            actual[requested] = f'{name_for_item}_files/{changed_item_string}'
            items_list.append((url, actual[requested]))
    return items_list, soup.prettify()


def netloc_check(link, item):
    splitted = urlparse(item)
    parsed_link = urlparse(link)
    if splitted.netloc == parsed_link.netloc:
        return splitted
    if splitted.netloc == '':
        return splitted


def download(link, folder='.'):
    folder_name = change_name(link)
    soup = requesting(link)
    make_folder(folder_name, folder)
    html_path = f'{folder}/{flatter_paths(folder_name)}'
    data, page = finding_tags(soup, link)
    if len(page) != 0:
        logging.info(f'Downloading from {link}')
        with PixelBar('Downloading..', max=len(data)) as bar:
            for netloc, name in data:
                netloc = urljoin(link, netloc)
                file_name = f'{folder}/{name}'
                with open(file_name, 'wb') as file:
                    content = requests.get(netloc).content
                    file.write(content)
                    bar.next()
        with open(html_path, 'w') as html_file:
            html_file.write(page)
    else:
        logging.warning('Current page has nothing available to download.')
    return html_path
