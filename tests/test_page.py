import pageloader
import pytest
import pathlib


# @pytest.mark.parametrize(
#     'address, pth, result',
#     [('address_sample.txt', 'path_sample.txt', 'result_sample.txt')]
# )
def test_stuff():
    assert pageloader.downloading(
        'https://ru.hexlet.io/courses',
        '/var/tmp'
    ) == '/var/tmp/ru-hexlet-io-courses.html'


def test_stufff():
    assert pageloader.downloading(
        'https://ru.hexlet.io/courses'
    ) == f'{pathlib.Path.cwd()}/ru-hexlet-io-courses.html'