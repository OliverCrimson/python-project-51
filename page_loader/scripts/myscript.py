# !/usr/bin/env python3
import logging
import sys

from page_loader.cli import parsing
from page_loader.page_loader_tool import download


def main():
    try:
        arguments = parsing()
        result = download(
            arguments.url,
            arguments.output
        )
        return result
    except Exception as error:
        logging.error(error)
        logging.info('Page is not available')
        sys.exit(1)


if __name__ == '__main__':
    main()
