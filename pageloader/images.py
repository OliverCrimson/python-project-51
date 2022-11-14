import requests
import html.parser
from bs4 import BeautifulSoup
import pathlib
import urllib.parse
import urllib.request
from urllib.parse import urljoin, urlparse
    

from pageloader.loader import namin

x = "/home/monkeybusiness/new_proj/python-project-51/pageloader/page-loader-hexlet-repl-co/page-loader-hexlet-repl-co.html"

# with open(x, 'r') as file:
#     scr = file.read()
# 
# soup = BeautifulSoup(scr, 'html.parser')
# 
# # title = soup.title
# # print(title.string)
# ima = soup.find_all('img')
# for i in ima:
#     print(i['src'])


def find_img_tags(link):
    with open(link, 'r') as file:
        scr = file.read()
        file.close()
    soup = BeautifulSoup(scr, 'html.parser')
    images_links = soup.find_all('img')
    images_row = []
    for item in images_links:
        images_row.append(item['src'])
    return images_row


# bbb = find_img_tags(x)
# # print(find_img_tags(x))
# # def splitting_link(link):
# #     some_link = urllib.parse.urlparse(link)
# #     print(some_link)
# fff = urlparse("https://page-loader.hexlet.repl.co")
# print(fff)
# # rrrr = urljoin('https://page-loader.hexlet.repl.co', bbb[0])
# # 
# req = requests.get(rrrr)
# with open('sample.jpg', 'wb') as file:
#     file.write(req.content)

def download_imges(link):
    valid_name = namin(link)
    print(valid_name)
    valid_link = f'{valid_name[:-5]}/{valid_name}'
    parsed_link = urlparse(link)
    print(parsed_link)
    print(valid_link)
    img_paths_array = find_img_tags(link)
    print(img_paths_array)
    with open(f"{pathlib.Path.cwd()}{valid_link}", "r") as file:
        scrape = file.read()
        soup = BeautifulSoup(scrape, 'html.parser')
        imgs = soup.find_all('img')
        for item in imgs:
            item['src'] = valid_link
            


download_imges(x)


