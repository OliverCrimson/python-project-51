import argparse
import pathlib


CURRENT_DIR = pathlib.Path.cwd()


def parsing():
    parser = argparse.ArgumentParser(
        description='page downloader')
    parser.add_argument('url', help='input page')
    parser.add_argument('-o', '--output',
                        default=pathlib.Path.cwd(),
                        help='chose specific directory')
    return parser.parse_args()
