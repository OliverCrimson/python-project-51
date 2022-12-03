import page_loader
import pytest
import pathlib
import requests_mock
from page_loader.mkfolders import folder_create
from page_loader.naming import change_name


def test_change_name():
    assert change_name('https://page-loader.hexlet.repl.co') == 'page-loader-hexlet-repl-co'



