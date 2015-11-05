__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
import json
import pickle
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
     a = ra.compressed()[0]
     return a[:2] + ':' + a[3:5] + ':' + a[6:8]


def name_func(pk,count=1):
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