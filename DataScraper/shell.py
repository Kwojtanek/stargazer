"""DataScraper

Welcome to scraper of data for zorya application.

Usage:
  Only One param available
  shell.py (-h | --help)
  shell.py -v
  shell.py cls
  shell.py -s
  shell.py -run
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
  run   collects data for given catalogue if it exists on server
  settings  To see all connection settings
"""
from __future__ import print_function
import sys, os
from common_funcs import status_code, status_code_raw
from settings import print_settings
from Composer import Composer
from Senders import LocalSender, PKGet,CoorsSender
import requests
import json
__version__ = '0.5.0'
__doc__ += 'VERSION: %s' % __version__

args = sys.argv

cls = lambda : os.system('cls' if os.name=='nt' else 'clear')
h = lambda :print(__doc__)
v = lambda :print(__version__)


#Temporary solution
def run():
    # Function Updates all data for given object in db but object is recognized by it's coordinates
    #  so to update coordinates you have to use update function
    Cat = raw_input('Name of catalogue: ')
    r = requests.get('http://127.0.0.1:8000/endpoint/catalogueInfo',params={'catalogue':Cat,'format':'json'})
    length = int(json.loads(r.text)['size'])
    it = int(json.loads(r.text)['count'])
    print(str(round(float(it)/float(length),4)*100) + ' %')
    while it < length:
        it +=1
        Status = status_code_raw()
        if Status == 200:
            try:
                Data = Composer(Cat, it)
                print(Data.__unicode__())

                LocalSender(Data.get_data()).send()
            except StandardError:
                pass
        else:
            print('Server not reachable')
            break


def update():
    #update function updates only coordinates of objact that is already in db but to do that it has to know id
    # of object to identyfie it so it updates only existing objects.
    Cat = raw_input('Name of catalogue: ')
    r = requests.get('http://127.0.0.1:8000/endpoint/catalogueInfo',params={'catalogue':Cat,'format':'json'})
    length = int(json.loads(r.text)['size'])
    it = int(json.loads(r.text)['count']) - 1
    print(str(round(float(it)/float(length),4)*100) + ' %')
    while it < length:
        it +=1
        Status = status_code_raw()
        if Status == 200:
            try:
                Data = Composer(Cat, it)
                print(Data.__unicode__())
                PK = PKGet(Data.__unicode__()).send()
                coors = Data.get_data()['data']['declination']
                print(PK, ' ', coors)
                C = CoorsSender(coors,PK)
                C.send()
            except StandardError:
                pass
        else:
            print('Server not reachable')
            break
dictFuncs = {
    '-h': h,
    '--help': h,
    'cls': cls,
    '-v':v,
    '-s':status_code,
    'settings': print_settings,
    'run': run,
    'update': update
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
