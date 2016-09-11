__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'

from Scrapers import SimbadScraper, SimbadIdsScraper, NEDScraper, WikiMediaScraper
from common_funcs import photo_reader, overview_reader, wiki_photo_all


NED = False
SIMBAD = True
DOCS_OVERVIEW = False
DOCS_PHOTO = False
BIBCODES = False
#Scraping from wiki medias requiers connection for every photo so it slows down scraping process ~4times
WIKIMEDIA = False
WIKIINFO = False

UPDATED_URL = 'http://127.0.0.1:8000/endpoint/createupdateAPI'


#Maps scrapers to correct settings
setts = {'NED': NEDScraper,
         'SIMBAD': SimbadScraper,
         'BIBCODES': SimbadIdsScraper,
         'DOCS_OVERVIEW': overview_reader,
         'DOCS_PHOTO': photo_reader,
         'WIKIINFO': WikiMediaScraper,
         'WIKIMEDIA' : wiki_photo_all}

#Different fields that will be included in data from Nasa Extragalactic db.
Votablefields = ['flux(U)','flux(B)','flux(V)','flux(R)',
                 'flux(I)','flux(J)','flux(H)','flux(K)',
                 'flux(u)', 'flux(g)','flux(r)','flux(i)',
                 'flux(z)',
                 'posa','pm']


def print_settings():
    print 'WIKIMEDIA %s' % WIKIMEDIA
    print "NED %s" % NED
    print "SIMBAD %s" % SIMBAD
    print "DOCS_OVERVIEW %s" % DOCS_OVERVIEW
    print "DOCS_PHOTO %s" % DOCS_PHOTO
    print "ENDPOINT %s" %UPDATED_URL
    print 'To change settings go to file settings.py'