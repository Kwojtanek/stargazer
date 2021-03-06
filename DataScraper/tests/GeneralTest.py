__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
import unittest

from DataScraper.Data_procesors import pk_reader, pk_generator, get_otype


class TestGeneral(unittest.TestCase):
    def testPk(self):
        self.assertEqual(pk_reader(),1)
        self.assertEqual(pk_generator().next(),2)
    def testOtype(self):
        self.assertEqual(get_otype('Gx'), 'Gx')
        self.assertEqual(get_otype('Pn'), 'Pl')
        self.assertEqual(get_otype('RfNeb'), 'RfNeb')

if __name__ == '__main__':
    unittest.main()
