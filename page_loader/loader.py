import pathlib

import requests


def namin(address, folder=str(pathlib.Path.cwd())):
    string = ''
    # result = ''
    if address.startswith('http://'):
        string += str(address[7:])
    if address.startswith('https://'):
        string += address[8:]
    string = string.replace('.', '-')
    string = string.replace('/', '-')
    # if folder is not None:
    #     result = f"{folder}/{string}.html"
    # if folder is None:
    #     folder = str(pathlib.Path.cwd())
    #     result = f"{folder}/{string}.html"
    # return result
    return string + ".html"


def save_file(link, path=''):
    extract = requests.get(link).text
    current_dir = pathlib.Path.cwd()
    valid_name = namin(link)
    desi = pathlib.Path(f"{current_dir}/{valid_name[:-5]}")
    desi.mkdir(exist_ok=True)
    with open(f"{desi}/{valid_name}", "w") as file:
        file.write(extract)
        file.close()

# print(downloading('https://page-loader.hexlet.repl.co'))
# save_file('https://page-loader.hexlet.repl.co')
