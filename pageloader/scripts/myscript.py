# !/usr/bin/env python3
from pageloader.loader import namin
from pageloader.cli import parsing
from pageloader.main_scr import main_func

def main():
    arguments = parsing()
    result = main_func(
        arguments.url,
        arguments.path
    )
    return result


if __name__ == '__main__':
    main()
