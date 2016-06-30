__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
"""
READS row in photolog with photo-index.txt,
Gets list of images from wiki ->{{name}},
Iterates throu list,
Scraps from wiki image info
checks if photo is baned,
checks if photo was used before if so waits for input,
maps corectly name, pk, url,urlthumb
pushes photo to serwer
photo-index++
Loop photo-index if <= len photo.log
"""
import json

from DataScraper.Scrapers import WikiSingleImageScraper,WikiImageScraper
from DataScraper.Senders import PhotoSender
from DataScraper.common_funcs import ban_reader, duplicate_writer, available_photo_reader, save_add_index, read_row


def mainfunc():
    #Reads photo
    singlerow = read_row(available_photo_reader())
    #Subtracks info
    pk = singlerow['pk']
    name = singlerow['name']
    print 'proceeded object %s' % name, singlerow
    #Downloads list of images of object
    filelistexists = WikiImageScraper(name).getimageslist()
    if filelistexists:
        filelist = json.loads(filelistexists)
        #Creates list of not duplicated and not baned photos
        shortlist = []
        for f in filelist:
            duplicate_writer(f)
            if not ban_reader(f):
                shortlist.append(f)
        print 'Images list %s' % shortlist
        for s in shortlist:
            print('Geting details about %s' % s)
            singleimageexists = WikiSingleImageScraper(s,thumbWidth=400,thumbHeight=400).getimagesdetails()
            if singleimageexists:
                singleimage = singleimageexists
                #if photo is big enougth
                if  singleimage['size'] > 80000:
                    print 'Sending... %s' % singleimage
                    PhotoSender('',singleimage, pk).send_data()
                    print 'Data sended'
                else:
                    print "Not enouth details in photo"
            else:
                print 'No info'
    save_add_index(available_photo_reader())
    print '....................................................................................................'
#
# new = []
# for f in json.loads(WikiImageScraper('NGC 224').getimageslist()):
#     if not ban_reader(f):
#         new.append(f)
#
