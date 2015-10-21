# coding=utf-8
__author__ = 'Jakub Wojtanek Kwojtanek@gmail.com'
import urllib
import urllib2
import json
import re
from astroquery.simbad import Simbad


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
        data = urllib2.urlopen(self.object_endpoint())
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
            pattern = re.compile('I\d+')
            if re.findall(pattern, number):
                catalog = 'IC'
                number = number[1:]
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
        a = self.get_data()['query']['pages']
        # noinspection PyBroadException
        try:
            return a[dict(a).keys()[0]]['extract']
        except:
            return False


class SimbadScraper:

    def __init__(self, name,*args):
        self.name = name
        self.votable_fields = ['flux(B)', 'mt','otype', 'ra', 'dec','id(NGC)'].append(args)

    def get_data(self):
        result_table = Simbad()
        result_table.add_votable_fields(self.votable_fields)
        result_table.remove_votable_fields('coordinates')
        result_table = result_table.query_object(self.name)
        return result_table
