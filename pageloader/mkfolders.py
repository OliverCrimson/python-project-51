import pathlib
from pageloader.naming import change_name

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
