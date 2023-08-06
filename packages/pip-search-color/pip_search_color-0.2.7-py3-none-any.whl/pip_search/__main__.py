# __main__.py
'''
usage: pypi_search.py [-h] query

positional arguments:
  query       terms to search pypi.org package repository

optional arguments:
  -h, --help  show this help message and exit
'''
import sys
import argparse
from rich import pretty
from pip_search.pip_search import search


def check_positive(pages: int):
    if int(pages) < 1:
        raise argparse.ArgumentTypeError(f'[red]{pages}[/red] is an invalid value for pages')
    return int(pages)


def main():
    pretty.install()
    ap = argparse.ArgumentParser()
    ap.add_argument('-p', '--pages', type=check_positive, required=False, default=2,
                    help='number of page results to display [default=2]')
    ap.add_argument('query', nargs='+', type=str,
                    help='terms to search pypi.org package repository')
    args = ap.parse_args()
    search(query=' '.join(args.query), pages=args.pages)


if __name__ == '__main__':
    sys.exit(main())
