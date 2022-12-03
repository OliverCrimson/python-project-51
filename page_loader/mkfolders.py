import logging
import pathlib
import sys

from page_loader.naming import change_name

CURRENT_DIR = pathlib.Path.cwd()


def folder_create(link, path=''):
    """
    Function makes folder according to the given link
    :param path:
    :param link:
    :return:
    """
    if not path:
        desirable_folder = pathlib.Path(
            f"{CURRENT_DIR}/{change_name(link)}_files"
        )
        desirable_folder.mkdir(exist_ok=True)
    else:
        desirable_folder = pathlib.Path(
            f"{path}/{change_name(link)}_files"
        )
        desirable_folder.mkdir(exist_ok=True)


def mkfolder(link):
    folder = pathlib.Path(f"{CURRENT_DIR}/{change_name(link)}")
    folder.mkdir(exist_ok=True)


def check_folder(item):
    path = pathlib.Path(item)
    if path.exists():
        logging.info(f'path {path} exists')
        pass
    else:
        logging.info('directory not found')
        sys.exit(1)


def form_folder(link, folder=''):
    if folder:
        path = pathlib.Path(f"{folder}")
        if path.exists():
            return path
        else:
            logging.info(f"{folder} not exists")
            sys.exit(1)
    if not folder:
        string = f"{pathlib.Path.cwd()}/{change_name(link)}_files"
        pathlib.Path(string).mkdir(exist_ok=True)
        return string


def mk_f(path):
    pth = pathlib.Path(path)
    pth.mkdir(exist_ok=True)
