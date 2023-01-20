import logging
from urllib.parse import urljoin, urlparse
import pathlib
import requests
from bs4 import BeautifulSoup
from progress.bar import PixelBar
from page_loader.mkfolders import make_folder
from page_loader.naming import naming_folders, change_name, flatter_paths
from page_loader.request_module import requesting



logging.basicConfig(format='%(levelname)s: %(message)s',
                    level=logging.INFO)






def finding_tags(soup, link, folder=pathlib.Path.cwd()):
    search_data = [
        ('img', 'src'),
        ('link', 'href'),
        ('script', 'src')
    ]

    data_arr = []
    for one, two in search_data:
        required = [
            (one_name, two) for one_name in soup(one) 
            if one_name.get(two) is not None
        ]
        data_arr.extend(required)
    twin = []
    for one, two in data_arr:
        if netloc_check(one.get(two), link):
            url = one.get(two)
            name_for_item = change_name(link)
            one[two] = f'{name_for_item}_files/' \
                       f'{change_name(link)}-' \
                       f'{flatter_paths(one[two])}'
            twin.append((url, one[two]))
    return twin, soup.prettify()


def netloc_check(link, item):
    if urlparse(link).netloc != urlparse(item).netloc:
        return item


def download(link, folder='.'):
    folder_name = change_name(link)
    
    soup = requesting(link)
    path_to_folder = make_folder(folder_name, folder)
    logging.info(f'created a folder {path_to_folder}')
    
    html_path = f'{folder}/{flatter_paths(folder_name)}'
    logging.info(f'html file path is {html_path}')
    data, juice = finding_tags(soup, link)
    with PixelBar('Downloading..', max=len(data)) as bar:
        for netloc, name in data:
            netloc = urljoin(link, netloc)
            file_name = f'{folder}/{name}'
            with open(file_name, 'wb') as file:
                file.write(requests.get(netloc).content)
            bar.next()
        with open(html_path, 'w') as html_file:
            html_file.write(juice)
            
    # print(html_path)
    return html_path


# test = 'https://page-loader.hexlet.repl.co'
# download(test)