# !/usr/bin/env python3
from pageloader.loader import downloading
from pageloader.cli import parsing


def main():
    arguments = parsing()
    result = downloading(
        arguments.url,
        arguments.path,
    )
    print(result)


if __name__ == '__main__':
    main()
