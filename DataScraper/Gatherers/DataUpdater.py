# coding=utf-8
__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
from astroquery.simbad import Simbad
from DataScraper.Scrapers import NEDScraper
from DataScraper.Scrapers import SimbadScraper
from DataScraper.Senders import LocalSender
from DataScraper.common_funcs import get_ra
import json
from astroquery.ned import Ned
import re
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
iteration = 0
#Wzory dla Simbad Scrapera
wildcards = ['[0-9]','[1-9][0-9]','[1-9][0-9][0-9]',
             '1[1-9][0-9][0-9]','2[1-9][0-9][0-9]','3[1-9][0-9][0-9]',
             '4[1-9][0-9][0-9]','5[1-9][0-9][0-9]','6[1-9][0-9][0-9]',
             '7[1-8][0-9][0-9]']
# Different wavelengths 
fluxes = ('U', 'B', 'V', 'R', 'I', 'J', 'H', 'K', 'u', 'g', 'r', 'i', 'z')
def fluxfunc(res, FluxCount = 0):
        #Zbiera kilka jasności i uśrednia je
    RoundedFlux = 0
    for f in fluxes:
        if(res['FLUX_' + str(f)]) and (res['FLUX_' + str(f)]) != '':
            RoundedFlux += res['FLUX_' + str(f)]
            FluxCount +=1
    if FluxCount != 0:
        RoundedFlux/= FluxCount
    return RoundedFlux
# ('posa_RA', '<U13'), ('posa_DEC', '<U13'), ('posa_upMajAxis', '<U1'),
#  ('posa_MajAxis', '<f4'), ('posa_upMinAxis', '<U1'), ('posa_MinAxis', '<f4')
#  ('posa_PA', '<f4'), ('posa_equi', '<i4'), ('posa_epoch', '<f4'), ('posa_bibcode', '<U19'),
#  ('PMRA', '<f8'), ('PMDEC', '<f8'), ('PM_ERR_MAJA', '<f4'), ('PM_ERR_MINA', '<f4'),
#  ('PM_ERR_ANGLE', '<i2'), ('PMRA_2', '<f8'), ('PMDEC_2', '<f8'), ('PM_ERR_MAJA_2', '<f4'),
#  ('PM_ERR_MINA_2', '<f4'), ('PM_ERR_ANGLE_2', '<i2')]>

# Data = SimbadScraper(catalogue + ' %s' %(wildcards[iteration]),
#                      'flux(U)','flux(B)','flux(V)','flux(R)',
#                      'flux(I)','flux(J)','flux(H)','flux(K)',
#                      'flux(u)', 'flux(g)','flux(r)','flux(i)',
#                      'flux(z)',
#                      'posa','pm',
#                      wildcard=True)
Data = SimbadScraper('IC 950',
                     'flux(U)','flux(B)','flux(V)','flux(R)',
                     'flux(I)','flux(J)','flux(H)','flux(K)',
                     'flux(u)', 'flux(g)','flux(r)','flux(i)',
                     'flux(z)',
                     'posa','pm')
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
    numb = re.findall(pattern, SimbadResults['MAIN_ID'])
    print SimbadResults
    print 'Galadim %s x %s' %(SimbadResults['GALDIM_MAJAXIS'], SimbadResults['GALDIM_MINAXIS'])
    print 'Posa %s x %s' % (SimbadResults['posa_MajAxis'], SimbadResults['posa_MinAxis'])
    print 'Posa up %s x %s' % (SimbadResults['posa_upMajAxis'], SimbadResults['posa_upMinAxis'])
    # print SimbadResults['Umag']
    # print SimbadResults['Vmag']
    # print SimbadResults['Rmag']
    # print SimbadResults['Imag']
    # print SimbadResults['Jmag']
    mag = fluxfunc(SimbadResults)
    if mag != 0:
        results["magnitudo"] = round(mag,1)
    if results != {}:
        try:
            LocalSender(numb[0],results).send_data_noresp()
        except:
            print "Wrong name"
    print json.dumps(results)
    # # ('GALDIM_MAJAXIS', '<f4'),
# # ('GALDIM_MINAXIS', '<f4'), ('GALDIM_ANGLE', '<i2'),
# # ('GALDIM_INCL', '<i2'), ('GALDIM_QUAL', '<U1'),
# # ('GALDIM_WAVELENGTH', '<U1'), ('GALDIM_BIBCODE', 'O')]>
# V = Simbad.query_objectids("crab nebula")
# print V
# print len(V)
# for x in V:
#     print x
