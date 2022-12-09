import os

import requests.exceptions
import requests
from page_loader.page_loader_tool import download

import page_loader
import pytest
import tempfile
import pathlib
import requests_mock
from page_loader.naming import change_name


def test_change_name():
    assert change_name('https://page-loader.hexlet.repl.co') == 'page-loader-hexlet-repl-co'



# def test_connect():
#     with requests_mock.Mocker() as mock:
#         mock.get('https://page-loader.hexlet.repl.co', status_code=400)
#         assert download()

