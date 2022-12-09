import logging
import pathlib
import sys
import requests
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
    folder.mkdir(parents=True, exist_ok=True)


# def check_folder(item):
#     path = pathlib.Path(item)
#     if path.exists():
#         logging.info(f'path {path} exists')
#         pass
#     else:
#         logging.info('directory not found')
#         sys.exit(1)


# def form_folder(link, folder=''):
#     if folder:
#         path = pathlib.Path(f"{folder}")
#         if path.exists():
#             return path
#         else:
#             logging.info(f"{folder} not exists")
#             raise FileNotFoundError
#     if not folder:
#         string = f"{pathlib.Path.cwd()}/{change_name(link)}_files"
#         if requests.get(link).ok:
#             pathlib.Path(string).mkdir(exist_ok=True)
#         logging.warning(string)
#         return pathlib.Path(string)


# def foldres(link, folder=''):
#     if pathlib.Path(folder).exists():
#         path = pathlib.Path(f"{pathlib.Path.cwd()}/{folder}")
#         logging.info(f"path {path} exists")
#         if not path.exists():
#             logging.info(f"Directory {folder} doesn't exist.")
#             raise FileNotFoundError
# 
#     # if pathlib.Path(folder).exists():
#         if path.exists():
#             fol = pathlib.Path(f"{path}"
#                                f"/{change_name(link)}_files")
#             fol.mkdir(exist_ok=True)
#             return fol
#     else:
#         cur = pathlib.Path.cwd()
#         pth = pathlib.Path(f"{cur}/{change_name(link)}_files")
#         pth.mkdir(exist_ok=True)
#         return pth


# foldres('https://page-loader.hexlet.repl.co')

def mk_dir(link, folder=''):
    if pathlib.Path(folder).exists():
        path = pathlib.Path(f"{pathlib.Path.cwd()}/{folder}")
        fol = pathlib.Path(f"{path}/{change_name(link.strip())}_files")
        fol.mkdir(exist_ok=True)
        logging.info(f"created {fol}")
        return fol
        
    else:
        logging.info(f"Directory {folder} doesn't exist")
        raise FileNotFoundError


# print(mk_dir('https://page-loader.hexlet.repl.co', 'scripts'))
# 
# print(pathlib.Path('direc').exists())
