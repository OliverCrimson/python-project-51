import logging
import tempfile
from urllib.parse import urljoin, urlparse
import pathlib
import requests
import requests_mock
from progress.bar import PixelBar
from page_loader.mkfolders import make_folder
from page_loader.naming import naming_folders, change_name, flatter_paths
from page_loader.request_module import requesting



logging.basicConfig(format='%(levelname)s: %(message)s',
                    level=logging.INFO)


def finding_tags(soup, link):
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
        if netloc_check(link, one.get(two)):
            url = one.get(two)
            name_for_item = change_name(link)
            asd = urljoin(urlparse(link).netloc, one[two])
            one[two] = f'{name_for_item}_files/'\
                    f'{change_name(urlparse(link).netloc)}-'\
                       f'{flatter_paths(one[two])}'
                       # f'{change_name(urlparse(link).netloc)}-' \
                       
                       
                       
            twin.append((url, one[two]))
    return twin, soup.prettify()



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
    path_to_folder = make_folder(folder_name, folder)
    logging.info(f'created a folder {path_to_folder}')
    html_path = f'{folder}/{flatter_paths(folder_name)}'
    logging.info(f'html file path is {html_path}')
    data, juice = finding_tags(soup, link)
    # with PixelBar('Downloading..', max=len(data)) as bar:
    for netloc, name in data:
        netloc = urljoin(link, netloc)
        file_name = f'{folder}/{name}'
        with open(file_name, 'wb') as file:
            content = requests.get(netloc).content
            file.write(content)
            # bar.next()
        with open(html_path, 'w') as html_file:
            # print(juice)
            html_file.write(juice)
    # pth = pathlib.Path(f'{pathlib.Path.cwd()}/{html_path}')
    # print(pth)
    return html_path


# # with tempfile.TemporaryDirectory() as tempdir:
# #     test = 'https://page-loader.hexlet.repl.co'
# #     print(tempdir)
# #     download(test, tempdir)
# test = 'https://page-loader.hexlet.repl.co'
# # 
# # 
# # test2 = 'https://ru.hexlet.io/u/new?from=https%3A%2F%2Fru.hexlet.io%2Fprojects%2F51%2Fmembers%2F26050%3Fstep%3D4'
# download(test)
# x = requesting(test2)
# finding_tags(x, test2)

# with open('/home/monkeybusiness/new_proj/python-project-51/tests/fixtures/original.html', 'r') as file:
#     x = file.read()
# 
# with requests_mock.Mocker() as m:
#     m.get('https://site.com/blog/about', text=x)
#     finding_tags(requesting())