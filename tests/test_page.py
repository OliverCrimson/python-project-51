import pageloader
import pytest
import pathlib
import requests_mock
from pageloader.mkfolders import folder_create
from pageloader.naming import change_name


def test_change_name():
    assert change_name('https://page-loader.hexlet.repl.co') == 'page-loader-hexlet-repl-co'



