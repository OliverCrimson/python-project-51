from urllib.parse import urlparse


def change_name(link):
    string = f"{urlparse(link).netloc}" \
             f"{urlparse(link).path}"
    string = string.replace('.', '-')
    string = string.replace('/', '-')
    # if string.endswith('-'):
    #     string = string[:-1]
    return string
