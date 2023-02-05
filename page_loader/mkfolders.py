import logging
import pathlib
from page_loader.urls import to_dir


def make_folder(link, folder=''):
    if pathlib.Path(folder).exists():
        path = pathlib.Path(folder)
        directory = pathlib.Path(f"{path}/{to_dir(link)}")
        directory.mkdir(parents=True, exist_ok=True)
        logging.info(f'Created directory {directory}')
        return directory
    else:
        raise FileNotFoundError
