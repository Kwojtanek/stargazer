__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
import unittest

from DataScraper.Data_procesors import otype_reader
from DataScraper.Scrapers import WikiMediaScraper

# firts type
firsttype = (u'AGN', u'Active Galaxy Nucleus')
Nametype = otype_reader(0)[1]
Shortcutnametype = otype_reader(0)[0]
class TestType(unittest.TestCase):
    def testType(self):
        self.assertEqual(u'AGN', Shortcutnametype)
        self.assertEqual(u'Active Galaxy Nucleus',Nametype)

if __name__ == '__main__':
    unittest.main()
print WikiMediaScraper(firsttype[1]).get_finall_data()