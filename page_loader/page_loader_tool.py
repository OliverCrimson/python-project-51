
import logging
import pathlib
from urllib.parse import urljoin, urlparse

from page_loader.content_extractor \
    import downloading_imgs, replacin, img_links_array
from page_loader.mkfolders import form_folder
from page_loader.naming import change_name
from page_loader.request_module import requesting

logging.basicConfig(format='%(levelname)s: %(message)s',
                    level=logging.INFO)


def download(link, folder=''):# noqa
    logging.info(f"requested url: {link}")
    name = change_name(link)
    # val_path = pathlib.Path(f"{x}/{name}_files")
    response = requesting(link)
    x = form_folder(link, folder)
    val_path = pathlib.Path(f"{x}/{name}_files")
    val_path.mkdir(exist_ok=True)
    logging.info(f"output path: {pathlib.Path.cwd()}/{folder}")
    images = response.find_all('img')
    links = response.find_all('link')
    scripts = response.find_all('script')
    lst, lst_links, script_links = [], [], []

    for tag in images:
        valid_link = urljoin(link, tag['src'])
        if urlparse(valid_link).netloc == urlparse(link).netloc:
            lst.append(tag['src'])
            tag['src'] = f"{val_path}/{replacin(tag['src'])}"
    for tag in links:
        valid_link = urljoin(link, tag['href'])
        if urlparse(valid_link).netloc == urlparse(link).netloc:
            lst_links.append(tag['href'])
            tag['href'] = f"{val_path}/{replacin(tag['href'])}"
    for tag in scripts:
        if tag.get('src'):
            valid_link = urljoin(link, tag['src'])
            if urlparse(valid_link).netloc == urlparse(link).netloc:
                script_links.append(tag['src'])
                tag['src'] = f"{val_path}/{replacin(tag['src'])}"

    with open(f"{x}/{name}.html", "w") as file:
        file.write(response.prettify())
        logging.info(f'write html file: '
                     f'{x}/{name}.html')
    big_list = lst + lst_links + script_links
    result = img_links_array(big_list, link)
    downloading_imgs(link, result, val_path)
    logging.info(f"Page was downloaded as "
                 f"'{folder}/{name}.html'")
