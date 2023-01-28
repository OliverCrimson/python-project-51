import os
import pathlib
import tempfile
import requests_mock

from page_loader.mkfolders import make_folder
from page_loader.page_loader_tool import download, finding_tags

from page_loader.loader import normalize_string
from page_loader.naming import change_name
from page_loader.request_module import requesting

FIXTURES_PATH = f'{pathlib.Path.cwd()}/tests/fixtures'
LINK = 'https://site.com/blog/about'


def test_change_name():
    assert change_name('https://page-loader.hexlet.repl.co') == 'page-loader-hexlet-repl-co'


def read_from_file(file, mode):
    with open (file, mode) as f:
        f = f.read()
        return f


def test_string():
    expected = 'site-com-blog-about-assets-styles.css'
    actual = normalize_string('https://site.com/blog/about/assets/styles.css')
    assert expected == actual


def test_folder_creation():
    expected_dir_name = 'site-com-blog-about_files'
    make_folder('https://site.com/blog/about')
    assert pathlib.Path(expected_dir_name).exists()
    os.rmdir(expected_dir_name)


def test_download():
    with tempfile.TemporaryDirectory() as tempdir:
        expect = f'{tempdir}/page-loader-hexlet-repl-co.html'
        assert expect == download('https://page-loader.hexlet.repl.co', tempdir)


def test_content():
    original = read_from_file(f'{FIXTURES_PATH}/original.html', 'r')
    expected = read_from_file(f'{FIXTURES_PATH}/expected.html', 'r')
    image = read_from_file(f'{FIXTURES_PATH}/site-com-blog-about_files/site-com-photos-me.jpg', 'rb')
    script = read_from_file(f'{FIXTURES_PATH}/site-com-blog-about_files/site-com-assets-scripts.js', 'rb')
    style = read_from_file(f'{FIXTURES_PATH}/site-com-blog-about_files/site-com-blog-about-assets-styles.css', 'r')
    with requests_mock.Mocker() as mock:
        fake_adress = 'https://site.com/blog/about'
        fake_image = 'https://site.com/photos/me.jpg'
        fake_script = 'https://site.com/assets/scripts.js'
        fake_style = 'https://site.com/blog/about/assets/styles.css'
        mock.get(fake_adress, text=original)
        mock.get(fake_image, content=image)
        mock.get(fake_script, content=script)
        mock.get(fake_style, text=style)
        # x = requesting(fake_adress)
        # y = finding_tags(x, fake_adress)
        with tempfile.TemporaryDirectory() as tempdir:
            final = download(fake_adress, tempdir)
            result = read_from_file(final, 'r')
            assert result == expected
