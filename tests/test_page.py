import pageloader
import pytest
import pathlib


# @pytest.mark.parametrize(
#     'address, pth, result',
#     [('address_sample.txt', 'path_sample.txt', 'result_sample.txt')]
# )
def test_stuff():
    assert pageloader.downloading(
        'https://page-loader.hexlet.repl.co',
        '/var/tmp'
    ) == '/var/tmp/page-loader-hexlet-repl-co.html'


def test_y():
    assert pageloader.downloading(
        'https://page-loader.hexlet.repl.co'
    ) == f'{pathlib.Path.cwd()}/page-loader-hexlet-repl-co.html'