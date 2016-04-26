# coding=utf-8
__author__ = 'root'
import unittest

from DataScraper.Scrapers import Reciver, WikiMediaScraper, SimbadScraper
from DataScraper.Senders import Sender
from DataScraper.Loger import LogData


class TestReciver(unittest.TestCase):
    def testLog(self):
        kwargs = {'a': 'a', 'id' : 100}
        self.assertDictEqual({'a': 'a', 'id' : 100}, LogData(4,**kwargs).print_log())

    def testEndpoint(self):
        S = Reciver(1)
        self.assertEqual(S.name, 1)
        self.assertEqual(S.object_endpoint(), 'http://www.zorya.co/1?format=json')
        resp = S.get_object()
        self.assertEqual(S.get_object().headers['Status'], '200 OK')
        self.assertEqual(S.get_name(), 'NGC 1')
        S3 = Reciver(12101)
        self.assertFalse(Reciver(15999).get_data())
        self.assertEqual(S3.get_name(), 'IC 4089')
        S3 = Reciver(8907)
        self.assertEqual(S3.get_name(), 'IC 895')

    def testWikiAPI(self):
        testtext = "NGC 1 is a spiral galaxy SbbPa Ring located 190 million light-years away in the constellation Pegasus. At about 90,000 light-years in diameter, it is just a little smaller than our galaxy, the Milky Way. It is the first object listed in the New General Catalogue. In the coordinates used at the time of the catalog's compilation (epoch 1860), this object had the lowest right ascension of all the objects in the catalog, making it the first object to be listed when the objects were arranged by right ascension. Since then, the coordinates have shifted, and this object no longer has the lowest right ascension of all the NGC objects."
        name = 'NGC 1'
        S = WikiMediaScraper(name)
        self.assertEqual(S.title, 'NGC 1')
        self.assertEqual(S.object_endpoint(), 'https://en.wikipedia.org/w/api.php?redirects=&format=json&exintro=&prop=extracts&titles=NGC+1&action=query&explaintext=')
        self.assertEqual(S.get_finall_data(),testtext)
        self.assertFalse(WikiMediaScraper('NGC 1111111').get_finall_data())

    def testSimbadAPI(self):
        S = SimbadScraper('NGC 1')
        self.assertEqual(S.name, 'NGC 1')

    def testSender(self):
        data ={"overview": "NGC 3 is a lenticular galaxy in the Pisces constellation.", "classe": "S0:", "type_shortcut": "Gx", "otype": "Galaxy", "declination": "+08 18 05", "rightAsc": "00:07:16", "magnitudo": 14.6, "type": "Galaxy"}
        S = Sender(3,data)
        self.assertEqual(S.send_data(), data)


if __name__ == '__main__':
    unittest.main()
