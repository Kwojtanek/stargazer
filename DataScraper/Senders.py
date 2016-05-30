# coding=utf-8
import json
import urllib2

from Scrapers import Scraper

__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'


with open('/pro/stargazer/zorya/appviews/supersecret.code','r') as f:
    sk = f.read()
    f.close()
"""
Classes that sends data to db endpoints
"""


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

    def send_data_noresp(self,count=4):
        data = json.dumps(self.data)
        req = urllib2.Request(self.object_endpoint(), data, headers={'Content-Type':'application/json'})
        if count < 5:
            try:
                print 'Trying send data to%s' % self.object_endpoint()
                f = urllib2.urlopen(req,timeout=5)
                return  json.load(f)
            except:
                count+=1
                return self.send_data_noresp(count)
        else:
            return False

class MultipleDataSender(Sender):
    PARAMS = {'sk':sk,'multiple':True}
    pass


class PhotoSender(Scraper):
    def __init__(self, name, data, pk):
        Scraper.__init__(self,name)
        self.name = name
        self.data = data
        #Pk is unique identifier of object that will be updated
        self.pk = pk

    PARAMS = {'format':'json'}
    URL = 'http://www.zorya.co/endpoint/createphotoAPI'

    def conv_data(self):
        #Creates dict
        converted_data = {}
        converted_data['sk'] = sk
        converted_data['name'] = self.name
        converted_data['photo_url'] = self.data['url']
        converted_data['photo_thumbnail'] = self.data['thumburl']
        converted_data['ngc_object'] = self.pk
        return json.dumps(converted_data)

    def send_data(self,count=1):
        data = self.conv_data()
        req = urllib2.Request(self.object_endpoint(), data, headers={'Content-Type':'application/json'})
        if count < 5:
            try:
                print 'Trying send data to%s' % self.object_endpoint()
                f = urllib2.urlopen(req,timeout=5)
                return  json.load(f)
            except:
                count+=1
                return self.send_data(count)
        else:
            return False

class TypeSender(Scraper):
    def __init__(self,name,data):
        Scraper.__init__(self,name)
        self.name = name
        self.data = data
    PARAMS = {'format':'json'}
    URL = 'http://127.0.0.1:8000/endpoint/createtypeAPI'

    def conv_data(self):
        converted_data = {}
        converted_data['sk'] = sk
        converted_data['Maintype'] = self.data['Maintype']
        converted_data['Nametype'] = self.data['Nametype']
        converted_data['Shortcutnametype'] = self.data['Shortcutnametype']
        converted_data['Description'] = self.data['Description']
        print json.dumps(converted_data)

    def send_data(self,count=1):
        data = self.conv_data()
        req = urllib2.Request(self.object_endpoint(), data, headers={'Content-Type':'application/json'})
        if count < 5:
            try:
                print 'Trying send data to%s' % self.object_endpoint()
                f = urllib2.urlopen(req,timeout=5)
                return  json.load(f)
            except:
                count+=1
                return self.send_data(count)
        else:
            return False

# Wbudowane URLLIBS są straszne

# Nadchodzi nowa jakość Requests
import requests

class LocalSender:
    def __init__(self,*args,**kwargs):
        pass
    URL = 'http://127.0.0.1:8000/endpoint/createupdateAPI'
    def check_connection(self):
        req = requests.post(self.URL)
        return req.status_code