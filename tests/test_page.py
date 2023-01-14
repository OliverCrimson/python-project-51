import os
import pathlib
import tempfile

import pytest
import requests
import requests_mock
from page_loader.page_loader_tool import download

from page_loader.loader import normalize_string
# from page_loader.mkfolders import mk_dir
from page_loader.naming import change_name

FIXTURES_PATH = f'{pathlib.Path.cwd()}/fixtures'
LINK = 'https://site.com/blog/about'


def test_change_name():
    assert change_name('https://page-loader.hexlet.repl.co') == 'page-loader-hexlet-repl-co'



def read_from_file(file):
    with open (file, "r") as f:
        f = f.read()
        return f


def test_string():
    expected = 'site-com-blog-about-assets-styles.css'
    actual = normalize_string('https://site.com/blog/about/assets/styles.css')
    assert expected == actual

# def test_folder_creation():
#     expected_dir_name = 'site-com-blog-about_files'
#     # mk_dir('https://site.com/blog/about')
#     assert pathlib.Path(expected_dir_name).exists()
#     os.rmdir(expected_dir_name)


# def test_download():
#     original = read_from_file(f'{FIXTURES_PATH}/original.html')
#     expected = read_from_file(f'{FIXTURES_PATH}/expected.html')
# 
#     with requests_mock.Mocker() as dummy, tempfile.TemporaryDirectory() as dummy_dir:
#         dummy.get('https://site.com/blog/about', text=original)
#         download('https://site.com/blog/about', dummy_dir)
#                 
# 





