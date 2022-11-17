import requests
import html.parser
from bs4 import BeautifulSoup
import pathlib
import urllib.parse
import urllib.request
from urllib.parse import urljoin, urlparse

from pageloader.loader import namin


def find_img_tags(link):
    """
    finding all img tags in soup object, saving content of tags into list object.
    correcting content of img tag in soup and writing corrected html document.
    correctd html doc means src content of img tag lead to local file
    :param link: 
    :return: list of img ['src'] content
    """
    cur_dir = pathlib.Path.cwd()
    valid_naming = namin(link)
    desirable_folder = pathlib.Path(f"{cur_dir}/{valid_naming[:-5]}_files")
    desirable_folder.mkdir(exist_ok=True)
    desirable_link = f"{valid_naming[:-5]}"
    scr = requests.get(link).content
    soup = BeautifulSoup(scr, 'html.parser')
    images_links = soup.find_all('img')
    images_row = []
    for item in images_links:
        images_row.append(item['src'])
        item['src'] = f"{valid_naming[:-5]}_files/{desirable_link}.png"
    with open(f"{desirable_folder}/{valid_naming}", "w") as file:
        file.write(soup.prettify())
    return images_row


find_img_tags('https://page-loader.hexlet.repl.co')
qwe = ['/assets/professions/nodejs.png']


def img_links_array(array, link):
    form_array = []
    for i in array:
        form_array.append(urljoin(link, i))
    return form_array


def downloading_imgs(link, array):
    for item in array:
        with open(f"{namin(link)[:-5]}_files/{namin(link)[:-5]}.png", 'wb') as file:
            file.write(requests.get(item).content)


aaa = img_links_array(qwe, "https://page-loader.hexlet.repl.co")
downloading_imgs("https://page-loader.hexlet.repl.co", aaa)
