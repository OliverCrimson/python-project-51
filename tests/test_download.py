import pathlib
import tempfile

import pytest
import requests.exceptions
import requests_mock

from page_loader.mkfolders import make_folder
from page_loader.loading import download
from page_loader.request_module import download_resources
from page_loader.urls import change_name, to_file

FIXTURES_PATH = f'{pathlib.Path.cwd()}/tests/fixtures'
BAD_SITE = 'https://badsite.com'
LINK = 'https://site.com/blog/about'
FAKE_IMAGE = 'https://site.com/photos/me.jpg'
FAKE_SCRIPT = 'https://site.com/assets/scripts.js'
FAKE_CSS = 'https://site.com/blog/about/assets/styles.css'
ORIGINAL = f'{FIXTURES_PATH}/original.html'
EXPECTED = f'{FIXTURES_PATH}/expected.html'
IMAGE = f'{FIXTURES_PATH}/site-com-blog-about_files/site-com-photos-me.jpg'
SCRIPT = f'{FIXTURES_PATH}/site-com-blog-about_files/site-com-assets-scripts.js'
STYLES = f'{FIXTURES_PATH}/site-com-blog-about_files/' \
         f'site-com-blog-about-assets-styles.css'


def read_from_file(file, mode):
    with open(file, mode) as f:
        f = f.read()
        return f


def test_change_name():
    assert change_name(LINK) == 'site-com-blog-about'


def test_normalize_string():
    expected = 'site-com-blog-about-assets-styles.css'
    actual = to_file('https://site.com/blog/about/assets/styles.css')
    assert expected == actual


def test_make_folder():
    expected_dir_name = 'site-com-blog-about_files'
    with tempfile.TemporaryDirectory() as tempdir:
        make_folder('https://site.com/blog/about', tempdir)
        assert pathlib.Path(f'{tempdir}/{expected_dir_name}').exists()


def test_download():
    original = read_from_file(ORIGINAL, 'r')
    expected = read_from_file(EXPECTED, 'r')
    image = read_from_file(IMAGE, 'rb')
    script = read_from_file(SCRIPT, 'rb')
    style = read_from_file(STYLES, 'r')
    with requests_mock.Mocker() as mock:
        mock.get(LINK, text=original)
        mock.get(FAKE_IMAGE, content=image)
        mock.get(FAKE_SCRIPT, content=script)
        mock.get(FAKE_CSS, text=style)
        with tempfile.TemporaryDirectory() as tempdir:
            final = download(LINK, tempdir)
            result = read_from_file(final, 'r')
            expected_download_result = f'{tempdir}/site-com-blog-about.html'
            assert result == expected
            assert final == expected_download_result
            assert 'site-com-blog-about_files/' \
                   'site-com-blog-about-assets-styles.css' in result


def test_download_resources():
    image = read_from_file(IMAGE, 'rb')
    with requests_mock.Mocker() as mock:
        mock.get(FAKE_IMAGE, content=image)
        img = download_resources(FAKE_IMAGE)
        assert img == image


def test_errors():
    with pytest.raises(Exception) as error:
        with tempfile.TemporaryDirectory as tmp:
            download('https://badsite.com', tmp)
            assert str(error.value) == requests.RequestException
