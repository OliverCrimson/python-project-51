import logging
import pathlib

from page_loader.naming import naming_folders



def make_folder(link, folder=''):
    if pathlib.Path(folder).exists():
        path = pathlib.Path(folder)
        directory = pathlib.Path(f"{path}/{naming_folders(link)}")
        directory.mkdir(exist_ok=True)
        logging.info(f'Created directory {directory}')
        return directory
    else:
        raise FileNotFoundError


# make_folder('https://site.com/blog/about')
