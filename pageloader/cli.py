import argparse


def parsing():
    parser = argparse.ArgumentParser(
        description='page downloader')
    parser.add_argument('url')
    parser.add_argument('path')
    parser.add_argument('-out', '--output',
                        help='set format of output')
    return parser.parse_args()
