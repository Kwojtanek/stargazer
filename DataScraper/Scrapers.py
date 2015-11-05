# coding=utf-8
from duplicity.backend import retry

__author__ = 'Jakub Wojtanek Kwojtanek@gmail.com'
import urllib
import urllib2
import json
import re
from retrying import retry
from astroquery.simbad import Simbad


with open('/pro/stargazer/DataScraper/sk.txt','r') as f:
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



class SimbadScraper:
    """
    Scraper connects with simbad db and gets data.
     Votable fields defines which data to optain.
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
                f = urllib2.urlopen(req,timeout=2)
                return  json.load(f)
            except:
                count+=1
                return self.send_data_noresp(count)
        else:
            return False