__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
import json
import urllib2
from Scrapers import SimbadScraper,WikiMediaScraper,Reciver, Sender
from Loger import LogData
from Data_procesors import pk_generator,pk_reader,pk_writer
from Data_procesors import get_description, get_ra, get_otype, name_func


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

        try:
            SimbadResults = SimbadScraper(name).get_data()
            if SimbadResults:
                print 'Connected to Simbad'
                if(SimbadResults['FLUX_B'].compressed()) and (SimbadResults['FLUX_B'].compressed()) != '':
                    results["magnitudo"] = round(SimbadResults['FLUX_B'].compressed()[0],1)
                if(SimbadResults['MORPH_TYPE']).compressed() and (SimbadResults['MORPH_TYPE']).compressed() != '':
                    results["classe"] = SimbadResults['MORPH_TYPE'].compressed()[0]
                if(SimbadResults['OTYPE'].compressed()) and (SimbadResults['OTYPE'].compressed()) != '':
                    results["otype"] = get_description(SimbadResults['OTYPE'].compressed()[0])
                    results["type_shortcut"] = (SimbadResults['OTYPE'].compressed()[0])
                    results["type"] = get_otype(SimbadResults['OTYPE'].compressed()[0])
                if(SimbadResults['RA'].compressed()) and (SimbadResults['RA'].compressed()) != '':
                    results["rightAsc"] = get_ra(SimbadResults['RA'])
                if(SimbadResults['DEC'].compressed()) and (SimbadResults['DEC'].compressed()) != '':
                    results["declination"] = SimbadResults['DEC'].compressed()[0][:-3]
        except:
            print 'No simbad data'
        if results != {}:
            Sender(pk_reader(),results).send_data_noresp()
            print 'Data sended'
            print json.dumps(results)
        else:
            print 'No Data to send'
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
nooorka(20)
