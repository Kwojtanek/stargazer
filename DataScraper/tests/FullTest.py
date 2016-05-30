__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
import unittest
from DataScraper.common_funcs import CataloguesRWD
class TestCatalogue(unittest.TestCase):
    filled = CataloguesRWD(catalogue='NGC',size=7402,last_obj=1,logs='ctest.log.json')
    def testReadWrite(self):
        self.assertEquals(0,CataloguesRWD(logs='ctest.log.json').len())
        self.assertFalse(CataloguesRWD(logs='ctest.log.json').add_cat())
        self.filled.add_cat()
        self.assertEqual(1,self.filled.len())
        self.filled.save_file()
        self.assertEquals(1,CataloguesRWD(logs='ctest.log.json').len())
        self.filled.add_cat()
        self.filled.save_file()
        self.assertEquals(1,CataloguesRWD(logs='ctest.log.json').len())
        self.filled.add_one()
        self.filled.save_file()
        self.assertFalse(CataloguesRWD(logs='ctest.log.json').add_cat())
        self.assertEqual(CataloguesRWD(logs='ctest.log.json').data[0]['last_obj'],2)

        CataloguesRWD(logs='ctest.log.json').purge()
class TestSender(unittest.TestCase):
    pass
class TestComposer(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
