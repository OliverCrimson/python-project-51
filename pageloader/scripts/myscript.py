# !/usr/bin/env python3
import logging
import sys
from pageloader.cli import parsing
from pageloader.main_scr import main_func


def main():
    try:
        arguments = parsing()
        result = main_func(
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
