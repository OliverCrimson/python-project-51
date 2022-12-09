from urllib.parse import urlparse

# import pathlib
#
# from page_loader.loader import namin
#
# from page_loader.content_extractor import replacin


def change_name(link):
    string = f"{urlparse(link).netloc}" \
             f"{urlparse(link).path}"
    string = string.replace('.', '-')
    string = string.replace('/', '-')
    # if string.endswith('-'):
    #     string = string[:-1]
    return string


# x = ' https://site.com/blog/about'
# print(pathlib.Path(f"{pathlib.Path.cwd()}/{change_name(x.strip())}_files"))
