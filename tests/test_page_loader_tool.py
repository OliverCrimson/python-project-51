import pathlib
import tempfile
import requests_mock

from page_loader.mkfolders import make_folder
from page_loader.page_loader_tool import download

from page_loader.loader import normalize_string
from page_loader.naming import change_name


FIXTURES_PATH = f'{pathlib.Path.cwd()}/tests/fixtures'
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


def test_string():
    expected = 'site-com-blog-about-assets-styles.css'
    actual = normalize_string('https://site.com/blog/about/assets/styles.css')
    assert expected == actual


def test_folder_creation():
    expected_dir_name = 'site-com-blog-about_files'
    with tempfile.TemporaryDirectory() as tempdir:
        make_folder('https://site.com/blog/about', tempdir)
        assert pathlib.Path(f'{tempdir}/{expected_dir_name}').exists()


def test_content():
    original = read_from_file(ORIGINAL, 'r')
    expected = read_from_file(EXPECTED, 'r')
    image = read_from_file(IMAGE, 'rb')
    script = read_from_file(SCRIPT, 'rb')
    style = read_from_file(STYLES, 'r')
    with requests_mock.Mocker() as mock:
        fake_adress = 'https://site.com/blog/about'
        fake_image = 'https://site.com/photos/me.jpg'
        fake_script = 'https://site.com/assets/scripts.js'
        fake_style = 'https://site.com/blog/about/assets/styles.css'
        mock.get(fake_adress, text=original)
        mock.get(fake_image, content=image)
        mock.get(fake_script, content=script)
        mock.get(fake_style, text=style)
        with tempfile.TemporaryDirectory() as tempdir:
            final = download(fake_adress, tempdir)
            result = read_from_file(final, 'r')
            expected_download_result = f'{tempdir}/site-com-blog-about.html'
            assert result == expected
            assert final == expected_download_result