__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
import json
import pickle
import os
from Scrapers import Reciver

def pk_writer(pk):
    """
    writes pk
    """
    with open('/pro/stargazer/DataScraper/pk.txt', 'w') as f:
        pk_file = f.write(str(pk))
        f.close()


def pk_reader():
    """
    reads pk
    """
    with open('/pro/stargazer/DataScraper/pk.txt', 'r') as f:
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
    with open('/pro/stargazer/DataScraper/otypes.json','rb') as f:
        ot = (json.load(f))
        f.close()
    if ot.has_key(otype):
        return ot.get(otype)
    else:
        inputvalue = raw_input('No full name %s '  + otype)
        ot[otype] = inputvalue
        if inputvalue == 'break':
            return False
        else:
            with open('/pro/stargazer/DataScraper/otypes.json','w') as f:
                json.dump(ot,f)
            return  inputvalue

def get_description(otype):

    """
    return matching description of type, if none is matching waits for new
    """
    with open('/pro/stargazer/DataScraper/SearchTypes.json','r') as f:
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
                with open('/pro/stargazer/DataScraper/SearchTypes.json','w') as f:
                    json.dump(st,f)
                return inputvalue
            else:
                inputlabel = inputvalue
                newrow = {'value': [otype], 'label': inputlabel}
                st.append(newrow)
                with open('/pro/stargazer/DataScraper/SearchTypes.json','w') as f:
                    json.dump(st,f)
                return inputvalue


def get_ra(ra):
    #Formats right Ascension to datatimelike format
     a = ra.compressed()[0]
     return a[:2] + ':' + a[3:5] + ':' + a[6:8]


def name_func(pk,count=1):
    #Retries connection if has to
    #TODO Should be more explicit
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
    path = os.path.join('/pro/stargazer/DataScraper/docs/',source)
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
    with open('/pro/stargazer/DataScraper/docs/PhotoBanlist.json', 'r') as f:
        data = json.load(f)
        f.close()
        for x in data:
            if x == photo:
                return True
        return False

def duplicate_reader(photo):
    """
    Checks if photo is baned
    """
    with open('/pro/stargazer/DataScraper/docs/PhotoDuplicates.json', 'r') as f:
        data = json.load(f)
        f.close()
        for x in data:
            if x == photo:
                return True
        return False

#Writes json and finds if it already existst if not will append
def list_writer(photo,file):
    path = '/pro/stargazer/DataScraper/docs/%s' % file
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
    #If photo is baned return True
    if ban_reader(photo):
        print 'PHoto is banned %s ' % photo
        return True
    #Else Look for duplicates files
    else:
        if duplicate_reader(photo):
            # If photo is duplicated wait for decision if it should be baned or passed
            print 'Photo is duplicated %s ' % photo
            decision = raw_input('1 to ban photo or 0 to let it be sended to server name: %s ' % photo)
            #If decisoion is to bann append to ban it end return True
            if int(decision) == 1:
                list_writer(photo,'PhotoBanlist.json')
                return True
            #If decision is to not bann return False
            if int(decision) == 0:
                return False
            #If photo is not banned/in duplicates ->
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
    with open('/pro/stargazer/DataScraper/docs/photo-index.txt','r') as f:
        i = int(f.read())
        f.close()
        return i

def save_add_index(a):
    """
    Writes index of photo + 1
    :param a:
    :return:
    """
    with open('/pro/stargazer/DataScraper/docs/photo-index.txt','w') as f:
        f.write(str(a+1))
        f.close()

def read_row(index):
    with open('/pro/stargazer/DataScraper/logs/photo.log', 'r') as f:
        data =(json.load(f))
        f.close()
        if index < len(data):
            return data[index]
        else:
            return False
