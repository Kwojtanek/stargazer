# coding=utf-8
__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
from astroquery.simbad import Simbad
from DataScraper.Scrapers import NEDScraper
from DataScraper.Scrapers import SimbadScraper
from DataScraper.Scrapers import SimbadIdsScraper
from DataScraper.Senders import LocalSender
from DataScraper.common_funcs import get_ra, flux_func, idsconverter
import json
from DataScraper.Composer import Composer
from astroquery.ned import Ned
import re
null = None
'''
Many data in server is incorrect.
This file has to find names of them and update
'''

"Votable FIelds:" \
"right Asc > RA" \
"Declination DEC > " \
"Magnitudo FLUX(V)" \
"dimAxb" 'GALDIM_MAJAXIS x GALDIM_MINAXIS Arc Seconds' \
"PA > GALDIM_ANGLE deg"
"Max id 7840"

catalogue = 'ngc'
iteration = 9
catalogues = {'ngc': 7840,
              'IC': 5386,
              'Messier': 110,
              }
def wildcards_generator(nr):
    #takes number and changes them to wild card '[0-9]','[1-9][0-9]','[1-9][0-9][0-9]' like list
    wildlist = []
    counter = 1
    while counter <= nr:
        pass
wildcards = ['[0-9]','[1-9][0-9]','[1-9][0-9][0-9]',
             '1[0-9][0-9][0-9]','2[0-9][0-9][0-9]','3[0-9][0-9][0-9]',
             '4[0-9][0-9][0-9]','5[0-9][0-9][0-9]','6[0-9][0-9][0-9]',
             '7[0-8][0-9][0-9]']
wildcardsIC = [
             '1[0-9][0-9][0-9]','2[0-9][0-9][0-9]','3[0-9][0-9][0-9]',
             '4[0-9][0-9][0-9]','5[0-3][0-9][0-9]']
wildcardsMessier = ['[0-9]','[1-9][0-9]','1[0-1][0-9]']

Votablefields = ['flux(U)','flux(B)','flux(V)','flux(R)',
                     'flux(I)','flux(J)','flux(H)','flux(K)',
                     'flux(u)', 'flux(g)','flux(r)','flux(i)',
                     'flux(z)',
                     'posa','pm']
def main_func(catalogue='IC',wildcards=wildcardsIC):
    for card in wildcards:
        Data = SimbadScraper(catalogue + ' %s' %(card), *Votablefields,
                             wildcard=True)

        def restdatafunc(res):
            restresults = {}
            if(res['GALDIM_MAJAXIS']) and (res['GALDIM_MAJAXIS']) != '':
                restresults["dimAxb"] = str((res['GALDIM_MAJAXIS'])) + ' x ' + str((res['GALDIM_MINAXIS']))
            if(res['RA']) and (res['RA']) != '':
                restresults["rightAsc"] = get_ra(res['RA'])
            if(res['DEC']) and (res['DEC']) != '':
                 restresults["declination"] = SimbadResults['DEC']
            if(res['GALDIM_ANGLE']) and (res['GALDIM_ANGLE']) != '':
                 restresults["pa"] = int(res['GALDIM_ANGLE'])
            return restresults
        Results =  Data.get_data()

        #Tworzy json do wysłania dla każdego rzędu
        for SimbadResults in Results:
            results = {}
            pattern = re.compile('\d+$')
            try:
                numb = str(int(re.findall(pattern, SimbadResults['MAIN_ID'])[0])+7840)
            except:
                break
            print SimbadResults
            print 'Galadim %s x %s' %(SimbadResults['GALDIM_MAJAXIS'], SimbadResults['GALDIM_MINAXIS'])
            print 'Posa %s x %s' % (SimbadResults['posa_MajAxis'], SimbadResults['posa_MinAxis'])
            print 'Posa up %s x %s' % (SimbadResults['posa_upMajAxis'], SimbadResults['posa_upMinAxis'])
            mag = flux_func(SimbadResults)
            if mag != 0:
                results["magnitudo"] = round(mag,1)
            if results != {}:
                try:
                    LocalSender(numb,results).send_data_noresp()
                except:
                    print "Wrong name"
            print json.dumps(results)
data ={
"data":
{
"rightAsc": "00:07:11",
 "declination": "27 42 21"
},
"catalogue" :
{
            "catalogue": "NGC",
            "number": "12345"
        },
    "photo":[{"thumb":"https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Ngc7840.jpg/400px-Ngc7840.jpg","normal":"https://upload.wikimedia.org/wikipedia/commons/7/78/Ngc7840.jpg","orginal":"https://upload.wikimedia.org/wikipedia/commons/7/78/Ngc7840.jpg","name":"","photo":null,"photo_url":"https://upload.wikimedia.org/wikipedia/commons/7/78/Ngc7840.jpg","photo_thumbnail":"https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Ngc7840.jpg/400px-Ngc7840.jpg"}],
"bibcode" :
["2MAXI J0043+412", "ANDROMEDA Nebula", "AND Nebula", "2C   56", "DA  21", "GIN 801", "IRAS F00400+4059", "IRAS 00400+4059", "IRC +40013", "K79  1C", "LEDA    2557", "M  31", "MCG+07-02-016", "ANDROMEDA", "ANDROMEDA Galaxy", "NGC   224", "RAFGL  104", "UGC   454", "XSS J00425+4102", "Z 535-17", "Z 0040.0+4100", "[DGW65]   4", "2MASX J00424433+4116074", "[M98c] 004000.1+405943", "[VV2000c] J004244.3+411610", "[VV2003c] J004244.3+411610", "[VV2006] J004244.3+411610", "[VV98c] J004245.1+411622", "UZC J004244.3+411608", "[VV2010] J004244.3+411610"]
}
# res = SimbadIdsScraper('NGC 224')
# results = res.get_data()
#
# print json.dumps(idsconverter(results))
# S = SimbadScraper('Messier 16').get_data()
# for x in S:
#     print x
# print round(S['GALDIM_MAJAXIS'].compressed()[0],2)
# print S['GALDIM_MINAXIS'].compressed()[0]
print Composer('IC', 4592).get_data()