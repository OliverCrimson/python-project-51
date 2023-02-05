import logging
from urllib.parse import urljoin
from progress.bar import PixelBar
from page_loader.mkfolders import make_folder
from page_loader.urls import change_name, to_file, correcting_links, is_local
from page_loader.request_module import requesting, download_resources


def prepare_html(soup, link):
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
        if is_local(link, actual.get(requested)):
            url = actual.get(requested)
            name_for_item = change_name(link)
            changed_item_string = to_file(correcting_links(actual[requested],
                                                           link))
            actual[requested] = f'{name_for_item}_files/{changed_item_string}'
            items_list.append((url, actual[requested]))
    return items_list, soup.prettify()


def download(link, folder='.'):
    folder_name = change_name(link)
    soup = requesting(link)
    make_folder(folder_name, folder)
    html_path = f'{folder}/{to_file(folder_name)}'
    data, page = prepare_html(soup, link)
    if len(page) != 0:
        logging.info(f'Downloading from {link}')
        with PixelBar('Downloading..', max=len(data)) as bar:
            for netloc, name in data:
                netloc = urljoin(link, netloc)
                file_name = f'{folder}/{name}'
                with open(file_name, 'wb') as file:
                    # content = requests.get(netloc).content
                    content = download_resources(netloc)
                    file.write(content)
                    bar.next()
        with open(html_path, 'w') as html_file:
            html_file.write(page)
    else:
        logging.warning('Current page has nothing available to download.')
    return html_path
