
__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
'''
File includes all functions that process data and saves them to files, usually in json format
'''
import json
import os
import re
import numpy
from astropy import units as u
from astropy.coordinates import SkyCoord, get_constellation

from Scrapers import Reciver
from Senders import LocalSender

DOCS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),'docs')
LOGS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),'logs')

def pk_writer(pk):
    """
    writes pk
    """
    with open(os.path.join(DOCS_DIR, 'pk.txt'), 'w') as f:
        f.write(str(pk))
        f.close()


def pk_reader():
    """
    reads pk
    """
    with open(os.path.join(DOCS_DIR, 'pk.txt'), 'r') as f:
        pk = int(f.read())
        f.close()
        return pk


def pk_generator():
    """
    Generates next pk
    """
    pk = pk_reader()
    if pk <= 13401:
        yield pk + 1


def get_otype(otype):
    """
    reads type of object and if does not ocures in list waits for input

    """
    with open(os.path.join(DOCS_DIR, 'otypes.json'), 'rb') as f:
        ot = (json.load(f))
        f.close()
    if ot.has_key(otype):
        return ot.get(otype)
    else:
        inputvalue = raw_input('No full name %s ' + otype)
        ot[otype] = inputvalue
        if inputvalue == 'break':
            return False
        else:
            with open(os.path.join(DOCS_DIR,'otypes.json'), 'w') as f:
                json.dump(ot,f)
            return inputvalue


def get_description(otype):

    """
    return matching description of type, if none is matching waits for new
    """
    with open(os.path.join(DOCS_DIR, 'SearchTypes.json'),'r') as f:
        st = (json.load(f))
        f.close()

    for x in range(0,len(st)):
        for y in range(0,len(st[x]['value'])):
            if st[x]['value'][y] == otype:
                return st[x]['label']

    inputvalue = raw_input('No uniform name... for %s ' % otype )

    for z in range(0,len(st)):
        for v in range(0,len(st[z]['value'])):
            if st[z]['value'][v] == inputvalue:
                st[z]['value'].append(otype)
                with open(os.path.join(DOCS_DIR, 'SearchTypes.json'),'w') as f:
                    json.dump(st,f)
                return inputvalue
            else:
                inputlabel = inputvalue
                newrow = {'value': [otype], 'label': inputlabel}
                st.append(newrow)
                with open(os.path.join(DOCS_DIR, 'SearchTypes.json'),'w') as f:
                    json.dump(st,f)
                return inputvalue


def get_ra(ra):
    # Formats right Ascension to datatimelike format
     a = ra
     return a[:2] + ':' + a[3:5] + ':' + a[6:8]


def name_func(pk,count=1):
    # Retries connection if has to
    # TODO Should be more explicit
    print 'Trying'
    name = Reciver(pk).get_name()
    if count < 5:
        if name == False:
            count+=1
            return name_func(pk,count)
        else:
            return name
    else:
        return False


def createsave_json(source,datas):
    """
    Checks if file exists if not creates json file and dumbs json data
    :return:
    """
    path = os.path.join(DOCS_DIR, 'docs/',source)
    print 'banned %s' % datas
    if not os.path.isfile(path):
        with open(path, 'w+') as f:
            json.dump([], f)
            f.close()
    with open(path) as f:
        data = json.load(f)
        f.close()
    with open(path, 'w') as f:
        data.append(datas)
        json.dump(data, f)
        f.close()


def ban_reader(photo):
    """
    Checks if photo is baned
    """
    with open(os.path.join(DOCS_DIR, 'PhotoBanlist.json'), 'r') as f:
        data = json.load(f)
        f.close()
        for x in data:
            if x == photo:
                return True
        return False

def duplicate_reader(photo):
    """
    Checks if photo is duplicated
    """
    with open(os.path.join(DOCS_DIR, 'PhotoDuplicates.json'), 'r') as f:
        data = json.load(f)
        f.close()
        for x in data:
            if x == photo:
                return True
        return False

# Writes json and finds if it already existst if not will append
def list_writer(photo,file):
    path = os.path.join(DOCS_DIR, file)
    with open(path, 'r') as f:
        data = json.load(f)
        f.close()
    for x in data:
        if x == photo:
            return True
    else:
        with open(path,'w') as f:
            data.append(photo)
            json.dump(data,f)
            f.close()
            return False


def duplicate_writer(photo):
    """
    If photo is duplicated it could be banned by user
     so scripte will wait for input decision, else it will simply append to PhotoDuplist
     Returns true if photo is duplicated and baned

    """
    # If photo is baned return True
    if ban_reader(photo):
        print 'PHoto is banned %s ' % photo
        return True
    # Else Look for duplicates files
    else:
        if duplicate_reader(photo):
            # If photo is duplicated wait for decision if it should be baned or passed
            print 'Photo is duplicated %s ' % photo
            decision = raw_input('1 to ban photo or 0 to let it be sended to server name: %s ' % photo)
            # If decisoion is to bann append to ban it end return True
            if int(decision) == 1:
                list_writer(photo,'PhotoBanlist.json')
                return True
            # If decision is to not bann return False
            if int(decision) == 0:
                return False
            # If photo is not banned/in duplicates ->
            # Photo will be pushed to duplicates
        else:
            print 'Photo is not duplicated %s ' % photo
            list_writer(photo,'PhotoDuplicates.json')
            return False



def available_photo_reader():
    """
    READS index of last photo
    :return:
    """
    with open(os.path.join(DOCS_DIR, 'photo-index.txt'),'r') as f:
        i = int(f.read())
        f.close()
        return i

def save_add_index(a):
    """
    Writes index of photo + 1
    :param a:
    :return:
    """
    with open(os.path.join(DOCS_DIR,'photo-index.txt'),'w') as f:
        f.write(str(a+1))
        f.close()


def read_row(index):
    with open(os.path.join(DOCS_DIR,'photo.log'), 'r') as f:
        data =(json.load(f))
        f.close()
        if index < len(data):
            return data[index]
        else:
            return False


# Types reader functions
def otype_reader(pk):
    with open(os.path.join(DOCS_DIR,'otypes.json'),'rb') as f:
        ot = (json.load(f))
        f.close()
    return ot.items()[pk]

def pktype_writer(pk):
    """
    writes pk
    """
    with open(os.path.join(DOCS_DIR,'types/pk.txt'), 'w') as f:
        f.write(str(pk))
        f.close()


def pktype_reader():
    """
    reads pk
    """
    with open(os.path.join(DOCS_DIR, 'types/pk.txt'), 'r') as f:
        pk = int(f.read())
        f.close()
        return pk
fluxes = ('U', 'B', 'V', 'R', 'I', 'u', 'g', 'r', 'i', 'z')

def flux_func(res, fluxcount= 0):
    # Collects different wavelength fluxes and rounds them
    roundedflux = []
    for f in fluxes:
        if(res['FLUX_' + str(f)]) and (res['FLUX_' + str(f)]) != '':
            try:
                roundedflux.append(res['FLUX_' + str(f)].compressed()[0])

            except:
                pass
    return numpy.median(roundedflux)


def idsconverter(table):
    # Takes astroquery table and coverts it to list
    pattern = re.compile('NAME')
    # Many names contains NAME in front)
    l = [re.sub(pattern, '', r[0]).strip() for r in table]
    # return [' '.join(r.split()) for r in l]
    return l
def status_code():
    code = LocalSender().check_connection()
    if code == 200:
        print('Connection Ok')
    elif code == 500:
        print('Server Down')
    else:
        print('Http Status code %s' % code)


class CataloguesRWD:

    def __init__(self, catalogue=None, size=None, last_obj=None,logs='catalogues.log.json'):
        self.catalogue = catalogue
        self.size = size
        self.last_obj = last_obj
        self.logs = logs
        with open(os.path.join(LOGS_DIR,logs),'rw+') as f:
            self.data = json.load(f)
            f.close()

    __len__ = lambda self: len(self.data)

    #Sorry, OPEN/CLOSED principle
    len = lambda self: len(self.data)

    def add_cat(self):
            if not {'catalogue':self.catalogue,'size':self.size,'last_obj':self.last_obj} in self.data and self.last_obj == 1:
                if self.catalogue and self.size and self.last_obj:
                    self.data.append({'catalogue':self.catalogue,'size':self.size,'last_obj':self.last_obj})
            else:
                return False

    def save_file(self):
        with open(os.path.join(LOGS_DIR,self.logs),'w') as f:
            f.write(json.dumps(self.data))
            f.close()

    def purge(self):
        with open(os.path.join(LOGS_DIR,self.logs),'w') as f:
            f.write(json.dumps([]))
            f.close()
            self.data = []

    def add_one(self):
        self.last_obj +=1
        for c in self.data:
            if c['catalogue'] == self.catalogue:
                c['last_obj'] += 1

    def delete(self):
        for i, c in enumerate(self.data):
            if c['catalogue'] == self.catalogue:
                del self.data[i]
                break

    def read(self):
        message = ''
        print "There is %s" %len(self.data)
        if self.data:
            for c in self.data:
                print 'Catalogue name: %s' % c['catalogue']
                print 'Count of objects %s' % c['size']
                print 'Current object %s' % c['last_obj']
                print 'Percentage finished %s ' % (str(format(float(c['last_obj'])/float(c['size']),'.2f')))
        else:
            print 'No data'

    def read_raw(self):
        try:
            return {'catalogue':self.catalogue,'size':self.size,'last':self.last_obj}
        except:
            return 0

def docs_reader(filename):
    with open(os.path.join(DOCS_DIR,filename),'r') as f:
        data = json.load(f)['results']
        f.close()
        return data

def overview_reader(catalogue, number, data= docs_reader('overview.json')):
    ret = [
                row['overview']
                for row in data
                for cat in row['catalogues']
                if cat['object_catalogue'] == catalogue and cat['object_number'] == str(number)
            ]
    if ret:
        return ret[0]
    else:
        return False

def photo_reader(catalogue,number,data =docs_reader('Photo.json')):
    ret = []
    ret = [ row['photos']
            for row in data
            for cat in row['catalogues']
            if cat['object_catalogue'] == catalogue and cat['object_number'] == str(number)
            ]
    if ret:
        return ret[0]
    else:
        return False

def const_reader(abr):
    with open(os.path.join(DOCS_DIR,'constellations.json'),'r') as f:
        data = json.load(f)
        f.close()

    ret = [ row['id']
            for row in data
            if row['abbreviation'].lower() == abr.lower()
            ]
    if ret:
        return ret[0]
    else:
        return False

def get_const(const):
    c = SkyCoord(const,unit=(u.hourangle, u.deg))
    A = get_constellation(c, short_name=True)
    return const_reader(A)