import os

import requests.exceptions
import requests
from page_loader.page_loader_tool import download

import page_loader
import pytest
import tempfile
import pathlib
import requests_mock
from page_loader.mkfolders import folder_create
from page_loader.naming import change_name


def test_change_name():
    assert change_name('https://page-loader.hexlet.repl.co') == 'page-loader-hexlet-repl-co'


# def test_connect():
#     bad_url = 'https://badsite.com'
#     requests_mock.get(bad_url, exc=requests.exceptions.ConnectionError)
#     with tempfile.TemporaryDirectory() as tmpdirname:
#         assert not os.listdir(tmpdirname)
# 
#         with pytest.raises(Exception):
#             assert download(bad_url, tmpdirname)
#         assert not os.listdir(tmpdirname)



