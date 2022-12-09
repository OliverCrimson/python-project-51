import logging
import pathlib
import sys
import requests
from page_loader.naming import change_name

CURRENT_DIR = pathlib.Path.cwd()



def mk_dir(link, folder=''):
    if pathlib.Path(folder).exists():
        path = pathlib.Path(f"{pathlib.Path.cwd()}/{folder}")
        fol = pathlib.Path(f"{path}/{change_name(link.strip())}_files")
        fol.mkdir(parents=True, exist_ok=True)
        logging.info(f"created {fol}")
        return fol
        
    else:
        logging.info(f"Directory {folder} doesn't exist")
        raise FileNotFoundError


# mk_dir('https://page-loader.hexlet.repl.co')
# 
# print(pathlib.Path('direc').exists())
