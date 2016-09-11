# coding=utf-8
import requests

__author__ = 'Jakub Wojtanek Kwojtanek@gmail.com'
import urllib
import urllib2
import json
import re
from astroquery.ned import Ned
from astroquery.simbad import Simbad

'''
File includes all classes that are connecting to external services and scraps data.
'''

class Scraper:
    """
    Basic class scraper
    """

    def __init__(self, name):
        self.name = name

    def object_endpoint(self):
        """
        :return url to object to be updated
        """
        resp_format = urllib.urlencode(self.PARAMS)
        return '%s%s?%s' % (self.URL, self.name, resp_format)

    def get_object(self):
        """

        :return object page :
        """
        data = urllib2.urlopen(self.object_endpoint(), timeout=2)
        return data

    def get_data(self):
        """
        :rtype json
        """
        # noinspection PyBroadException
        try:
            return json.load(self.get_object())
        except:
            return False


class Reciver(Scraper):
    """
    Recives from server Name for object that will be updated
    """

    def __init__(self, name):
        Scraper.__init__(self, name)

    URL = 'http://www.zorya.co/'
    PARAMS = {'format': 'json'}

    def get_name(self):
        """
        :rtype : txt
        :return most common name of catalogue and number:
        """
        # noinspection PyBroadException
        try:
            u = json.load(self.get_object())
            catalog = u['catalogues'][0]['object_catalogue']
            number = u['catalogues'][0]['object_number']
            pattern = re.compile('I( |\d){4}')
            if re.findall(pattern, number):
                dig = re.compile('\d+')
                catalog = 'IC'
                number = re.search(dig, number)
                number = number.group(0)
                return '%s %s' % (catalog, number)
            else:
                return '%s %s' % (catalog, number)
        except:
            return False


class WikiMediaScraper(Scraper):
    """

    """

    def __init__(self, name):
        Scraper.__init__(self, name)
        self.title = name
        self.name = ''

    URL = 'https://en.wikipedia.org/w/api.php'

    @property
    def PARAMS(self):
        """
        overrides Params variable
        """
        return {'format': 'json',
                'action': 'query',
                'prop': 'extracts',
                'exintro': '',
                'explaintext': '',
                'redirects': '',
                'titles': self.title}

    def get_finall_data(self):
        """
        :rtype : txt
        :return: plain text extracted from json file. Short description of given object
        """
        # noinspection PyBroadException
        try:
            a = self.get_data()['query']['pages']
            return a[dict(a).keys()[0]]['extract']
        except:
            return False


class WikiImageScraper(Scraper):
    """
    This scraper finds images in wikipedia article according to data provided
    """

    def __init__(self, name, imgcount=10):
        Scraper.__init__(self, name)
        self.title = name
        self.name = ''
        # MAX Count of images returned in list
        self.imgcount = imgcount

    URL = "https://en.wikipedia.org/w/api.php"

    @property
    def PARAMS(self):
        """
        overrides Params variable
        """
        return {'format': 'json',
                'action': 'query',
                'prop': 'images',
                'redirects': '',
                'titles': self.title}

    def getimageslist(self):
        """
        :return list of images belonging to article on wikipedia
        """
        if self.get_data():
            imglist = []
            # Pattern matches every photo
            pattern = re.compile("\.(jpg|jpeg|tiff|png)$")

            # Extracts imamges list from data
            try:
                allData = self.get_data()['query']['pages']
                imageListData = allData[dict(allData).keys()[0]]['images']
                for singleImage in imageListData:
                    if pattern.search(singleImage['title']):
                        imglist.append(singleImage['title'])
                return json.dumps(imglist)
            except:
                return False
        else:
            return False


class WikiSingleImageScraper(Scraper):
    """
    This scraper will download information about one media in wikipedia
    """

    def __init__(self, name, thumbWidth=300, thumbHeight=300):
        Scraper.__init__(self, name)
        self.title = name
        self.name = ''
        # Defines width and height of thumnail
        self.width, self.height = thumbWidth, thumbHeight

    URL = 'https://en.wikipedia.org/w/api.php'

    @property
    def PARAMS(self):
        """
        overrides Params variable
        """
        return {'format': 'json',
                'action': 'query',
                'prop': 'imageinfo',
                'redirects': '',
                'titles': self.title,
                'iiurlheight': self.height,
                'iilimit': '50',
                'iiend': '2007-12-31T23:59:59Z',
                'iiprop': 'timestamp|user|url|dimensions'}

    def getimagesdetails(self):
        if self.get_data():
            try:
                allData = self.get_data()['query']['pages']
                singleImage = allData[dict(allData).keys()[0]]['imageinfo']
                return singleImage[0]
            except:
                return False


class SimbadScraper:
    """
    Scraper connects with simbad db and gets data.
     Votable fields defines which data to obtain.
     All key arguments are passed throu this class
     Data that will be passed as args
     See more on => astroquery.simbad.Simbad() class.
    """

    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.data = None
        self.args = args
        self.kwargs = kwargs

    def get_data(self):
        result_table = Simbad()
        # Extended timeout to search for 1000 rows
        result_table.TIMEOUT = 120
        result_table.ROW_LIMIT = 1000
        result_table.add_votable_fields('flux(V)', 'mt', 'otype', 'ra', 'dec', 'dim','flux(U)','flux(B)','flux(R)',
                     'flux(I)','flux(J)','flux(H)','flux(K)',
                     'flux(u)', 'flux(g)','flux(r)','flux(i)',
                     'flux(z)', *self.args)
        result_table = result_table.query_object(self.name, **self.kwargs)
        return result_table

class SimbadIdsScraper:
    """
    Returns ids of given objects
    """
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.data = None
    def get_data(self):
        Simbad.ROW_LIMIT = 18
        result_table = Simbad.query_objectids(self.name)
        return result_table

class NEDScraper:
    """
    This class connetcts to NASA/IPAC EXTRAGALACTIC DATABASE
    """
    def __init__(self, name):
        self.name = name

    def get_photometry(self):
        """

        :return:  Returns photometry data as astropy.table.Table` object.:
        Available dict.keys() are:
        ['No.', 'Object Name', 'RA(deg)', 'DEC(deg)', 'Type', 'Velocity', 'Redshift',
        'Redshift Flag', 'Magnitude and Filter', 'Distance (arcmin)', 'References', 'Notes',
        'Photometry Points', 'Positions', 'Redshift Points', 'Diameter Points', 'Associations']

        """

        return Ned.get_table(self.name)

    def get_diameters(self):
        """
        :return ` Returns data as astropy.table.Table` object.:
        Available dict.keys() are:

        ['No.', 'Frequency targeted', 'Refcode', 'Major Axis', 'Major Axis Flag',
        'Major Axis Unit', 'Minor Axis', 'Minor Axis Flag', 'Minor Axis Unit', 'Axis Ratio',
        'Axis Ratio Flag', 'Major Axis Uncertainty', 'Ellipticity', 'Eccentricity',
        'Position Angle', 'Equinox', 'Reference Level', 'NED Frequency', 'NED Major Axis',
        'NED Major Axis Uncertainty', 'NED Axis Ratio', 'NED Ellipticity', 'NED Eccentricity',
        'NED cos-1_axis_ratio', 'NED Position Angle', 'NED Minor Axis', 'Minor Axis Uncertainty',
        'NED Minor Axis Uncertainty', 'Axis Ratio Uncertainty', 'NED Axis Ratio Uncertainty',
        'Ellipticity Uncertainty', 'NED Ellipticity Uncertainty', 'Eccentricity Uncertainty',
        'NED Eccentricity Uncertainty', 'Position Angle Uncertainty',
        'NED Position Angle Uncertainty', 'Significance', 'Frequency', 'Frequency Unit',
        'Frequency Mode', 'Detector Type', 'Fitting Technique', 'Features', 'Measured Quantity',
        'Measurement Qualifiers', 'Targeted RA', 'Targeted DEC', 'Targeted Equinox',
        'NED Qualifiers', 'NED Comment']

        """
        return Ned.get_table(self.name, table='diameters')

class TypeScraper:

    def __init__(self,name,*args,**kwargs):
        self.name = name.replace('?','%3F')

    @property
    def URL(self):
        return 'http://127.0.0.1:8000/endpoint/type/%s/' %self.name

    def get(self):
        params = {'format':'json'}
        r = requests.get(self.URL,params=params)
        if json.loads(r.text).has_key('datail'):
            return False
        else:
            return r.text