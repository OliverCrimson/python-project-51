import pageloader
import pytest
import pathlib

from pageloader.mkfolders import folder_create
from pageloader.naming import change_name


def test_change_name():
    res = change_name('https://docs-python.ru/standart-library/modul')
    assert res == 'docs-python-ru-standart-library-modul'


def test_creation_dir():
    folder_create('https://docs-python.ru/standart-library/modul')
    assert pathlib.Path(change_name('https://docs-python.ru/standart-library/modul_files')).exists()
    pathlib.Path(change_name('https://docs-python.ru/standart-library/modul_files')).rmdir()
