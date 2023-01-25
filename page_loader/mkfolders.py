import logging
import pathlib
from page_loader.naming import naming_folders


def make_folder(link, folder=''):
    try:
        pathlib.Path(folder).exists()
        path = pathlib.Path(folder)
        directory = pathlib.Path(f"{path}/{naming_folders(link)}")
        directory.mkdir(parents=True, exist_ok=True)
        logging.info(f'Created directory {directory}')
        return directory
    except Exception as ex:
        raise ex
