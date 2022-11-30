import pathlib

from pageloader.request_module import requesting


def download(link, folder=pathlib.Path.cwd()):
    content_ = requesting(link)
    images = content_.find_all('img')
    scripts = content_.find_all('script')
    links = content_.find_all('link')
    script_row, link_row, img_row = [], [], []