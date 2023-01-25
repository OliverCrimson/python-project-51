# !/usr/bin/env python3
import logging
import sys

from page_loader.cli import parsing
from page_loader.page_loader_tool import download


logging.basicConfig(format='%(levelname)s: %(message)s',
                    level=logging.INFO)


def main():
    arguments = parsing()
    try:
        result = download(
            arguments.url,
            arguments.output
        )
        logging.info('Downloading complete')
        return result
    except Exception as error:
        logging.error(error)
        logging.info(f'Page is not available')
        sys.exit(1)


if __name__ == '__main__':
    main()
