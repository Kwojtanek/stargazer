# coding=utf-8
from duplicity.backend import retry

__author__ = 'Jakub Wojtanek Kwojtanek@gmail.com'
import urllib
import urllib2
import json
import re
from retrying import retry
from astroquery.simbad import Simbad


with open('/pro/stargazer/zorya/appviews/supersecret.code','r') as f:
    sk = f.read()
    f.close()

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
        data = urllib2.urlopen(self.object_endpoint(),timeout=2)
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
                number = re.search(dig,number)
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
        Scraper.__init__(self,name)
        self.title = name
        self.name = ''
        # MAX Count of images returned in list
        self.imgcount =imgcount

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
            imgList = []
            #Pattern matches every photo
            pattern = re.compile("\.(jpg|jpeg|tiff|png)$")

            #Extracts imamges list from data
            try:
                allData = self.get_data()['query']['pages']
                imageListData =  allData[dict(allData).keys()[0]]['images']
                for singleImage in imageListData:
                    if pattern.search(singleImage['title']):
                        imgList.append(singleImage['title'])
                return json.dumps(imgList)
            except:
                return False
        else:
            return False

class WikiSingleImageScraper(Scraper):
    """
    This scraper will download information about one media in wikipedia
    """
    def __init__(self,name,thumbWidth=300,thumbHeight=300):
        Scraper.__init__(self,name)
        self.title = name
        self.name = ''
        # Defines width and height of thumnail
        self.width, self.height = thumbWidth, thumbHeight
    '&'
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
                'iiend':'2007-12-31T23:59:59Z',
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
    """

    def __init__(self, name,*args):
        self.name = name
        self.data = None

    def get_data(self):
        result_table = Simbad()
        result_table.add_votable_fields('flux(B)', 'mt','otype', 'ra', 'dec')
        result_table.remove_votable_fields('coordinates')
        result_table = result_table.query_object(self.name)
        return result_table

class Sender(Scraper):
    def __init__(self, name, data,  **kwargs):
        Scraper.__init__(self,name)
        self.data = data

    PARAMS = {'sk':sk}
    URL = 'http://www.zorya.co/updateAPI/'

    def send_data(self):
        data = json.dumps(self.data)
        req = urllib2.Request(self.object_endpoint(), data, headers={'Content-Type':'application/json'})
        f = urllib2.urlopen(req)
        response = json.load(f)
        return response

    def send_data_noresp(self,count=1):
        data = json.dumps(self.data)
        req = urllib2.Request(self.object_endpoint(), data, headers={'Content-Type':'application/json'})
        if count < 5:
            try:
                print 'Trying send data to%s' % self.object_endpoint()
                f = urllib2.urlopen(req,timeout=5)
                return  json.load(f)
            except:
                count+=1
                return self.send_data_noresp(count)
        else:
            return False

class PhotoSender(Scraper):
    def __init__(self, name, data, pk):
        Scraper.__init__(self,name)
        self.name = name
        self.data = data
        #Pk is unique identifier of object that will be updated
        self.pk = pk

    PARAMS = {'format':'json'}
    URL = 'http://www.zorya.co/endpoint/createphotoAPI'

    def conv_data(self):
        converted_data = {}
        converted_data['sk'] = sk
        converted_data['name'] = self.name
        converted_data['photo_url'] = self.data['url']
        converted_data['photo_thumbnail'] = self.data['thumburl']
        converted_data['ngc_object'] = self.pk
        return json.dumps(converted_data)

    def send_data(self,count=1):
        data = self.conv_data()
        req = urllib2.Request(self.object_endpoint(), data, headers={'Content-Type':'application/json'})
        if count < 5:
            try:
                print 'Trying send data to%s' % self.object_endpoint()
                f = urllib2.urlopen(req,timeout=5)
                return  json.load(f)
            except:
                count+=1
                return self.send_data(count)
        else:
            return False
