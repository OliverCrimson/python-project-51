import requests
import html.parser
from bs4 import BeautifulSoup
import pathlib
# import urllib.parse
# import urllib.request
from urllib.parse import urljoin, urlparse

from pageloader.loader import namin


def replacin(item):
    res = urlparse(item)
    joined = res.path
    joined = joined.replace('/', '-')[1:]
    if '.' not in joined:
        joined += ".html"
        return joined
    else:
        return joined


def find_img_tags(link):
    """
    finding all img tags in soup object,
    saving content of tags into list object.
    correcting content of img tag in soup and writing corrected html document.
    correctd html doc means src content of img tag lead to local file
    :param link:
    :return: list of img ['src'] content
    """
    cur_dir = pathlib.Path.cwd()
    valid_naming = namin(link)
    desirable_folder = pathlib.Path(f"{cur_dir}/{valid_naming[:-5]}_files")
    desirable_folder.mkdir(exist_ok=True)
    # desirable_link = f"{valid_naming[:-5]}"
    scr = requests.get(link).content
    soup = BeautifulSoup(scr, 'html.parser')
    images_links = soup.find_all('img')
    images_row = []
    link_row = []
    script_row = []
    script_links = soup.find_all('script')
    links_links = soup.find_all('link')
    for item in images_links:
        if urlparse(item['src']).netloc == urlparse(link).netloc:
            images_row.append(item['src'])
            item['src'] = f"{valid_naming[:-5]}_files/{replacin(item['src'])}"
    for item in links_links:
        if urlparse(item['href']).netloc == urlparse(link).netloc:
            link_row.append(item['href'])
            item['href'] = f"{valid_naming[:-5]}_files/{replacin(item['href'])}"
    for item in script_links:
        if item.get('src'):
            if urlparse(item.get('src')).netloc == urlparse(link).netloc:
                script_row.append(item['src'])
                item['src'] = f"{valid_naming[:-5]}_files" \
                              f"/{replacin(namin(item['src']))}"
    with open(f"{desirable_folder}/{valid_naming}", "w") as file:
        file.write(soup.prettify())
    result = link_row + images_row + script_row
    return result

# x = find_img_tags('https://ru.hexlet.io/courses')


def img_links_array(array, link):
    form_array = []
    for i in array:
        form_array.append(urljoin(link, i))
    return form_array


def downloading_imgs(link, array):
    for item in array:
        parsed = urlparse(item)
        with open(f"{namin(link)[:-5]}_files/"
                  f"{replacin(parsed.path)}", 'wb') as file:
            file.write(requests.get(item).content)


# y = img_links_array(x, 'https://ru.hexlet.io/courses')
# downloading_imgs("https://ru.hexlet.io/courses", y)
