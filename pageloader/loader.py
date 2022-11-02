import pathlib


def downloading(address, folder=str(pathlib.Path.cwd())):
    string = ''
    result = ''
    if address.startswith('http://'):
        string += str(address[7:])
    if address.startswith('https://'):
        string += address[8:]
    string = string.replace('.', '-')
    string = string.replace('/', '-')
    if folder is not None:
        result = f"{folder}/{string}.html"
    if folder is None:
        folder = str(pathlib.Path.cwd())
        result = f"{folder}/{string}.html"
    return result

# file_path = downloading('https://ru.hexlet.io/courses')
# print(file_path)  # => '/var/tmp/ru-hexlet-io-courses.html'


