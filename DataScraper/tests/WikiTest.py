# coding=utf-8
__author__ = 'root'
import unittest
import re, json
from DataScraper.Scrapers import WikiMediaScraper, WikiImageScraper, WikiSingleImageScraper
from DataScraper.Data_procesors import ban_reader, createsave_json, duplicate_writer, read_row
filelist = ["File:A Swift Tour of M31.OGG",
            "File:Andromeda Galaxy (with h-alpha).jpg",
            "File:Andromeda active core.jpg",
            "File:Andromeda constellation map.svg",
            "File:Andromeda galaxy.jpg", "File:Andromeda galaxy 2.jpg",
            "File:Andromeda galaxy Ssc2005-20a1.jpg",
            "File:Celestia.png", "File:Commons-logo.svg", "File:Crab Nebula.jpg"]


wikitestimageinfo = {"batchcomplete":"","query":{"pages":{"30895874":{"pageid":30895874,"ns":6,"title":"File:Andromeda Galaxy (with h-alpha).jpg","imagerepository":"shared","imageinfo":[{"timestamp":"2011-01-10T20:31:31Z","user":"File Upload Bot (Magnus Manske)","size":5125758,"width":3000,"height":1971,"thumburl":"https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Andromeda_Galaxy_%28with_h-alpha%29.jpg/609px-Andromeda_Galaxy_%28with_h-alpha%29.jpg","thumbwidth":609,"thumbheight":400,"url":"https://upload.wikimedia.org/wikipedia/commons/9/98/Andromeda_Galaxy_%28with_h-alpha%29.jpg","descriptionurl":"https://commons.wikimedia.org/wiki/File:Andromeda_Galaxy_(with_h-alpha).jpg"}]}}}}
wikitestimageinfo = unicode(wikitestimageinfo)
testrow = {"URL": "https://en.wikipedia.org/w/api.php?redirects=&format=json&exintro=&prop=extracts&titles=NGC+1&action=query&explaintext=", "pk": 1, "name": "NGC 1"}
class TestReciver(unittest.TestCase):
    def testImg(self):
        a = WikiImageScraper('NGC 224')
        self.assertEqual(a.object_endpoint(),'https://en.wikipedia.org/w/api.php?action=query&redirects=&prop=images&titles=NGC+224&format=json')
        self.assertTrue(ban_reader('File:Commons-logo.svg'))
        self.assertFalse(ban_reader('File:Andromeda Galaxy (with h-alpha).jpg'))
        self.assertTrue(duplicate_writer('bla.png'))
        self.assertEqual(testrow,read_row(0))
        self.assertFalse(read_row(123456))

print WikiSingleImageScraper('File:Andromeda Galaxy (with h-alpha).jpg').getimagesdetails()
if __name__ == '__main__':
    unittest.main()
