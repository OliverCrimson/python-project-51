import requests
# import html.parser
# from bs4 import BeautifulSoup
import pathlib
from urllib.parse import urljoin, urlparse
from progress.bar import PixelBar
from pageloader.loader import namin

import logging


logging.basicConfig(format='%(levelname)s: %(message)s',
                    level=logging.INFO)

CURRENT_DIR = pathlib.Path.cwd()


def replacin(item):
    res = urlparse(item)
    joined = res.path
    joined = joined.replace('/', '-')[1:]
    if '.' not in joined:
        joined += ".html"
        return joined
    else:
        return joined


# def find_img_tags(link):
#     """
#     finding all img tags in soup object,
#     saving content of tags into list object.
#     correcting content of img tag in soup and writing corrected html document.
#     correctd html doc means src content of img tag lead to local file
#     :param link:
#     :return: list of img ['src'] content
#     """
#     logging.info(f'start working on the {link} resources')
#     cur_dir = pathlib.Path.cwd()
#     logging.info(f'discovered current directory as {str(cur_dir)}')
#     valid_naming = namin(link)
#     logging.info(f'making link valid for further actions. result'
#                  f' {valid_naming}')
#     desirable_folder = pathlib.Path(f"{cur_dir}/{valid_naming[:-5]}_files")
#     desirable_folder.mkdir(exist_ok=True)
#     # valid_naming = change_name(link)
#     # folder = folder_create(link)
#     # desirable_folder = f"{folder}_files"
#     logging.info(f'made a new directory for output {str(desirable_folder)}')
#     # desirable_link = f"{valid_naming[:-5]}"
#     scr = requests.get(link).content
#     logging.warning(f"response code is {requests.get(link).status_code}")
#     soup = BeautifulSoup(scr, 'html.parser')
#     images_links = soup.find_all('img')
#     images_row = []
#     link_row = []
#     script_row = []
#     script_links = soup.find_all('script')
#     links_links = soup.find_all('link')
#     for item in images_links:
#         if urlparse(item['src']).netloc == urlparse(link).netloc:
#             images_row.append(item['src'])
#             item['src'] = f"{valid_naming[:-5]}_files/" \
#                           f"{replacin(item['src'])}"
#             logging.info("discovered some available image resorces")
#     for item in links_links:
#         if urlparse(item['href']).netloc == urlparse(link).netloc:
#             link_row.append(item['href'])
#             item['href'] = f"{valid_naming[:-5]}_files/" \
#                            f"{replacin(item['href'])}"
#             logging.info('discovered some links available')
#     for item in script_links:
#         if item.get('src'):
#             if urlparse(item.get('src')).netloc == urlparse(link).netloc:
#                 script_row.append(item['src'])
#                 item['src'] = f"{valid_naming[:-5]}_files"\
#                               f"/{replacin(namin(item['src']))}"
#                 logging.info('discovered some available scripts')
#     with open(f"{desirable_folder}/{valid_naming}", "w") as file:
#         file.write(soup.prettify())
#     result = link_row + images_row + script_row
#     return result


def img_links_array(array, link):
    form_array = []
    for i in array:
        form_array.append(urljoin(link, i))
    return form_array


def downloading_imgs(link, array, path):
    with PixelBar('Downloading', max=len(array)) as bar:
        for item in array:
            parsed = urlparse(item)
            with open(f"{path}/{namin(link)[:-5]}-"
                      f"{replacin(parsed.path)}", 'wb') as file:
                file.write(requests.get(item).content)
            bar.next()


# def download_element(item, link):
#     parsed = urlparse(item)
#     with Bar('Processing..', max=20) as bar:
#         for i in len(item):
#             with open(f"{namin(link)[:-5]}_files/"
#                       f"{replacin(parsed.path)}", 'wb') as file:
#                 file.write(requests.get(item).content)
#             bar.next()
# x = find_img_tags('https://ru.hexlet.io/courses')
# y = img_links_array(x, 'https://ru.hexlet.io/courses')
# downloading_imgs("https://ru.hexlet.io/courses", y)
