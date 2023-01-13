import os

import requests.exceptions
import requests

from page_loader.loader import normalize_string
from page_loader.page_loader_tool import download

import page_loader
import pytest
import tempfile
import pathlib
import requests_mock
from page_loader.naming import change_name


def test_change_name():
    assert change_name('https://page-loader.hexlet.repl.co') == 'page-loader-hexlet-repl-co'



# def read(file, mode="r"):
#     with open (file, "r") as f:
#         f = f.read()
#         return f
# 
# def test_string():
#     expected = 'site-com-blog-about-assets-styles.css'
#     actual = normalize_string('https://site.com/blog/about/assets/styles.css')
#     assert expected == actual