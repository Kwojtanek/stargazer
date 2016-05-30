"""DataScraper

Welcome to scraper of data for zorya application.

Usage:
  Only One param available
  shell.py (-h | --help)
  shell.py -v
  shell.py cls
  shell.py -s
  shell.py cat-info
  shell.py cat-add
  shell.py cat-rm
  shell.py settings

Options:
  exit  Ends sesion
  -h --help     Show this screen.
  -v     Show version.
  -s    server Status Code
  cls    clears shell window
  cat-info  Prints info about Catalogues included in scraper
  cat-add   Allows to add catalogue to scrapping process
  cat-rm    Removes catalogue from scrapping process
  settings  To see all connection settings
"""
from __future__ import print_function
import sys, os
from Senders import LocalSender
from common_funcs import CataloguesRWD, status_code
from settings import print_settings

__version__ = '0.2.0'
__doc__ += 'VERSION: %s' % __version__

args = sys.argv

catinfo = lambda : CataloguesRWD().read()
def catadd():
    C = CataloguesRWD(raw_input('Name of catalogue: '),raw_input('size of catalogue: '),1)
    C.add_cat()
    C.save_file()
def catrm():
    C = CataloguesRWD(catalogue=raw_input('Name of catalogue: '))
    C.delete()
    C.save_file()
cls = lambda : os.system('cls' if os.name=='nt' else 'clear')
h = lambda :print(__doc__)
v = lambda :print(__version__)


dictFuncs = {
    '-h': h,
    '--help': h,
    'cls': cls,
    '-v':v,
    '-s':status_code,
    'cat-info':catinfo,
    'cat-add':catadd,
    'cat-rm': catrm,
    'settings': print_settings
}

def main():
    if len(args) ==1:
        h()
    else:

        for arg in args[1:]:
            if dictFuncs.has_key(arg):
                dictFuncs[arg]()
        args[1] = raw_input('Type exit to quit, -h to see other options >>> ')
        if args[1] != 'exit':
            main()
        else: pass
if __name__ == '__main__':
    main()
