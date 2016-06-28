from astropy import units as u
from astropy.coordinates import get_constellation, SkyCoord

__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
import unittest
from DataScraper.common_funcs import CataloguesRWD, docs_reader, overview_reader, photo_reader, get_ra, const_reader
from DataScraper.Composer import ComposerInterface, Composer, Mapper
from DataScraper.Senders import LocalSender
null = None


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
testOverviewData = "NGC 1 is a spiral galaxy SbbPa Ring located 190 million light-years away in the constellation Pegasus. At about 90,000 light-years in diameter, it is just a little smaller than our galaxy, the Milky Way. It is the first object listed in the New General Catalogue. In the coordinates used at the time of the catalog's compilation (epoch 1860), this object had the lowest right ascension of all the objects in the catalog, making it the first object to be listed when the objects were arranged by right ascension. Since then, the coordinates have shifted, and this object no longer has the lowest right ascension of all the NGC objects."
testOverviewData2 = "The Ring Nebula (also catalogued as Messier 57, M57 or NGC 6720) is a planetary nebula in the northern constellation of Lyra. Such objects are formed when a shell of ionized gas is expelled into the surrounding interstellar medium by a red giant star, which was passing through the last stage in its evolution before becoming a white dwarf."
testPhotoData = [{"thumb":"/media/images/Pleiades_large.410x230.jpg","normal":"/media/images/Pleiades_large.1280x718.jpg","orginal":"/media/images/Pleiades_large.jpg","name":"","photo":"http://127.0.0.1:8000/media/images/Pleiades_large.jpg","photo_url":null,"photo_thumbnail":null}]


class TestDocs(unittest.TestCase):

    def testReader(self):
        self.assertIsInstance(docs_reader('overview.json'),list)

    def testOverview(self):
        self.assertEqual(overview_reader('NGC',1),testOverviewData)
        self.assertFalse(overview_reader('bla',1))
        self.assertEqual(overview_reader('Messier', 57),testOverviewData2)

    def testPhoto(self):
        self.assertFalse(photo_reader('bla',1))
        self.assertEqual(photo_reader('Messier', 45),testPhotoData)
    def testConst(self):
        self.assertEqual(1,const_reader('peg'))
        self.assertFalse(const_reader('badfa'))
class testComposerInterface(unittest.TestCase):
    #ONly few tests coz' they are overlaping with other unitetests
    testswikidata = u"NGC 1 is a spiral galaxy SbbPa Ring located 190 million light-years away in the constellation Pegasus. It was discovered 30 September 1861 by Heinrich d'Arrest. At about 90,000 light-years in diameter, it is just a little smaller than our galaxy, the Milky Way. It is the first object listed in the New General Catalogue. In the coordinates used at the time of the catalog's compilation (epoch 1860), this object had the lowest right ascension of all the objects in the catalog, making it the first object to be listed when the objects were arranged by right ascension. Since then, the coordinates have shifted, and this object no longer has the lowest right ascension of all the NGC objects."
    def testWiki(self):
        self.maxDiff = None
        self.assertEqual(self.testswikidata,ComposerInterface('WIKIINFO', 'NGC', 1).get_data())
        self.assertFalse(ComposerInterface('WIKIINFO', 'NGC', 999991).get_data())
    def testSimbad(self):
        self.assertFalse(ComposerInterface('SIMBAD', 'NGC', 999991).get_data())
    def testOverview(self):
        self.assertEqual(testOverviewData,ComposerInterface('DOCS_OVERVIEW', 'NGC', 1).get_data())
class TestSender(unittest.TestCase):
    pass
class TestComposer(unittest.TestCase):
    d = {'classe': 'SAbc', 'constelation': 1, 'type_shortcut': 'GinPair', 'otype': u'Galaxy', 'declination': u'+27 42 29', 'rightAsc': u'00:07:15', 'magnitudo': 10.99, 'type': u'Galaxy in Pair of Galaxies'}

    def testMapper(self):
        self.assertEqual(Mapper(ComposerInterface('SIMBAD','NGC', 1).get_data()).map_data(),self.d)

if __name__ == '__main__':
    unittest.main()
