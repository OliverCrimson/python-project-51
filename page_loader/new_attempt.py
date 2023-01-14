import logging
import pathlib
from urllib.parse import urljoin, urlparse

from page_loader.loader import normalize_link
from page_loader.mkfolders import make_folder
from page_loader.naming import naming_folders, change_name
from page_loader.request_module import requesting


# def download_new(link, folder='.'):
#     response = requesting(link)
#     logging.info(f'requested url is {link}')
#     folder_path = make_folder(link, folder)
#     
    
def finding_tags(soup, link, folder=pathlib.Path.cwd()):
    search_data = [
        ('img', 'src'),
        ('link', 'href'),
        ('script', 'src')
    ]
    
    data_arr = []
    for one, two in search_data:
        required = [
            (one_name, two) for one_name in soup(one) if one_name.get(two) is not None
        ]
        data_arr.extend(required)
    print(data_arr)
    twin = []
    for one, two in data_arr:
        if netloc_check(one.get(two), link):
            url = one.get(two)
            one[two] = 'bla bla'
            twin.append((url, one[two]))
    print(twin)
    print(soup.prettify())
    

def netloc_check(link, item):
    if urlparse(link).netloc != urlparse(item).netloc:
        return item




x = requesting('https://page-loader.hexlet.repl.co')

finding_tags(x, 'https://page-loader.hexlet.repl.co')