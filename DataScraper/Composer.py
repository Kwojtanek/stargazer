# coding=utf-8
"""
This file connects to different interfaces and created on big data to send as bellow shown.

Data format to send
{"data":
{
    "otype": "Galaxy",
    "type": "Galaxy in Pair of Galaxies",
    "type_shortcut": "GinPair",
    "classe": "Sb",
    "rightAsc": "00:07:11",
    "declination": "27 42 21",
    "magnitudo": 12.5,
    "dimAxb": "0.813 x 0.634",
    "pa": 110,
    "description": "F, S, R, bet *11 and *14",
    "id1": "UGC 5",
    "id2": "MCG 45748",
    "id3": "ZWG 477.54",
    "notes": "ZWG 478.26",
    "constelation": 1
},
"catalogue":{ "catalogue":"NGC",
"number":"12345"
},
"photo":[
    {
        "photo": "http://127.0.0.1:8000/media/images/ngc4494.jpg",
        "photo_url": "",
        "photo_thumbnail": ""
    },
    {
        "photo": "http://127.0.0.1:8000/media/images/ngc4559.jpg",
        "photo_url": "",
        "photo_thumbnail": ""
}],
"source":["www.bla.pca"],
"bibcode":["NGC 225"]
}
"""

__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
import json

from settings import *
from common_funcs import flux_func, get_ra, idsconverter, get_const, get_type, wiki_photo_all

#TODO Implement wikipedia image interface

astrotable = 'astropy.table.table.Table'


class Mapper:
    def __init__(self,data, iType):
        self.data = data
        self.iType = iType

    def map_data(self):
        results = {}
        if(self.data['GALDIM_MAJAXIS']):
            try:
                results["dimAxb"] = '%s x %s' % (self.data['GALDIM_MINAXIS'].compressed()[0], self.data['GALDIM_MINAXIS'].compressed()[0])
            except:
                pass
        if(self.data['FLUX_B'].compressed()) and (self.data['FLUX_B'].compressed()) != '':
            results["magnitudo"] = round(flux_func(self.data),2)
        if(self.data['MORPH_TYPE']).compressed() and (self.data['MORPH_TYPE']).compressed() != '':
            results["classe"] = self.data['MORPH_TYPE'].compressed()[0]
        if(self.data['OTYPE'].compressed()) and (self.data['OTYPE'].compressed()) != '':
            results["otype"] = get_type(self.data['OTYPE'].compressed()[0])['descriptiontype']
            results["type_shortcut"] = get_type(self.data['OTYPE'].compressed()[0])['shortcutnametype']
            results["type"] = get_type(self.data['OTYPE'].compressed()[0])['nametype']
        if(self.data['RA'].compressed()) and (self.data['RA'].compressed()) != '':
            results["rightAsc"] =  get_ra(self.data['RA'].compressed()[0])
        if(self.data['DEC'].compressed()) and (self.data['DEC'].compressed()) != '':
            results["declination"] = self.data['DEC'].compressed()[0][:-3]
        try:
            results['constelation'] = get_const('%s %s' % (results['rightAsc'],results['declination']))
        except:
            pass
        return results


class ComposerInterface:
    """
    Class unifies different scrapers use and return raw data
    """
    def __init__(self,interfaceType, catalogue, number,*args, **kwargs):
        self.iType = interfaceType
        self.catalogue = catalogue
        self.number = number
        self.args = args
        self.kwargs = kwargs

    def representation(self):
        return '%s %s' % (self.catalogue,self.number)


    def get_data(self):
        if setts.has_key(self.iType):
            if self.iType == 'NED':
                return setts[self.iType](self.representation()).get_photometry()
            if self.iType == 'SIMBAD' or self.iType == 'BIBCODES':
                return setts[self.iType](self.representation()).get_data()
            if self.iType == 'DOCS_OVERVIEW' or self.iType == 'DOCS_PHOTO':
                return setts[self.iType](self.catalogue,self.number)
            if self.iType == 'WIKIINFO':
                return setts[self.iType](self.representation()).get_finall_data()
            if self.iType =='WIKIMEDIA':
                return setts[self.iType](self.representation())


        else:
            return 0


class Composer(object):
    """
    Class  takes data from different interfaces, combine them and returns dictionary
    """
    def __init__(self, catalogue, number,
                 joint = ' ',
                 BIBCODES=BIBCODES,
                 NED=NED,
                 SIMBAD=SIMBAD,
                 WIKIMEDIA = WIKIMEDIA,
                 WIKIINFO = WIKIINFO,
                 DOCS_OVERVIEW = DOCS_OVERVIEW,
                 DOCS_PHOTO = DOCS_PHOTO):

        self.NED=NED
        self.SIMBAD=SIMBAD
        self.WIKIMEDIA = WIKIMEDIA
        self.WIKIINFO = WIKIINFO
        self.DOCS_OVERVIEW = DOCS_OVERVIEW
        self.DOCS_PHOTO = DOCS_PHOTO
        self.BIBCODES = BIBCODES
        # User can explicitly change settings

        self.catalogue = catalogue
        self.number = number
        self.joint = joint
        if WIKIMEDIA and DOCS_PHOTO or DOCS_OVERVIEW and WIKIINFO:
            raise StandardError('Warrnig, if data is collected from local files and wikipedia, it may cause errors.')

    def __unicode__(self):
        return '%s%s%s' % (self.catalogue, self.joint, self.number)

    print_settings = lambda: print_settings()

    def get_data(self):
        data = {}
        data['source'] = []
        if SIMBAD:
            SMCI = Mapper(ComposerInterface('SIMBAD', self.catalogue, self.number).get_data(),'SIMBAD').map_data()
            data['data'] = SMCI
            data['source'].append('http://simbad.u-strasbg.fr/simbad/sim-id?output.format=ASCII&Ident=%s_%s' %(self.catalogue,self.number))
        if NED:
            NMCI = Mapper(ComposerInterface('NED', self.catalogue, self.number).get_data(),'NED').map_data()
            data['data'] = NMCI
        if BIBCODES:
            BCI = ComposerInterface('BIBCODES',self.catalogue, self.number).get_data()
            data['bibcode'] = idsconverter(BCI)
        if DOCS_OVERVIEW:
            DCI = ComposerInterface('DOCS_OVERVIEW',self.catalogue, self.number).get_data()
            if DCI:
                data['data']['overview'] =  DCI
                data['source'].append(WikiMediaScraper(self.__unicode__()).object_endpoint())

        if DOCS_PHOTO:
            #BUG send multiple times same picture
            PCI = ComposerInterface('DOCS_PHOTO',self.catalogue, self.number).get_data()
            if PCI:
                data['photo'] = PCI
        if WIKIINFO:
            WPI = ComposerInterface('WIKIINFO',self.catalogue,self.number).get_data()
            if WPI:
                data['data']['overview'] = WPI
        if WIKIMEDIA:
            WMPI = ComposerInterface('WIKIMEDIA',self.catalogue,self.number).get_data()
            if WMPI:
                data['photo'] = WMPI
        data['catalogue'] ={ 'catalogue':self.catalogue, 'number':self.number}
        return data

