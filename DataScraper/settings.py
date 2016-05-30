__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'

WIKIMEDIA = False
WIKIINFO = False
NED = False
SIMBAD = True
DOCS_OVERVIEW = True
DOCS_PHOTO = True

UPDATED_URL = 'http://127.0.0.1:8000/endpoint/createupdateAPI'


def print_settings():
    print 'WIKIMEDIA %s' % WIKIMEDIA
    print "NED %s" % NED
    print "SIMBAD %s" % SIMBAD
    print "DOCS_OVERVIEW %s" % DOCS_OVERVIEW
    print "DOCS_PHOTO %s" % DOCS_PHOTO
    print "ENDPOINT %s" %UPDATED_URL
    print 'To change settings go to file settings.py'
