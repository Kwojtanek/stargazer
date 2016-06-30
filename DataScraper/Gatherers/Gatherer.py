__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
import json
from DataScraper.Scrapers import SimbadScraper,WikiMediaScraper
from DataScraper.common_funcs import pk_generator,pk_reader,pk_writer
from DataScraper.common_funcs import get_ra, name_func


#To to jest obrzydliwe
def Gatherer(pk):
    print 'Proccessing %s' % pk
    name = name_func(pk)
    if name != False:
        print name
        #LogData(1,**{'pk': pk})
        Wikimedia = WikiMediaScraper(name)
        results = {}
        if Wikimedia.get_finall_data():
            overwiev = Wikimedia.get_finall_data()
            #LogData(2,**{'pk':pk_reader(),'name':name, 'URL':Wikimedia.object_endpoint()}).save()
            results["overview"] = overwiev
            print 'Connected to %s' % Wikimedia.object_endpoint()
        else:
            print 'No wikimedia data'
    else:
        print '%s got no name' % pk


def nooorka(max):
    if pk_reader() <= max:
        try:
            Gatherer(pk_reader())
        except:
            try:
                print 'Retrying connection'
                Gatherer(pk_reader())
            except:
                #LogData(3,**{'pk':pk_reader(), 'status': 'could not connect'}).save()
                print "Couldn't connect to %s" % pk_reader()
        pk_writer(pk_generator().next())
        nooorka(max)


A = WikiMediaScraper('UGC 5692')
print A.get_finall_data()