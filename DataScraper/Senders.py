# coding=utf-8
import json
import urllib2

from Scrapers import Scraper

__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'


"""
Classes that sends data to db endpoints
"""


class Sender(Scraper):
    def __init__(self, name, data,  **kwargs):
        Scraper.__init__(self,name)
        self.data = data

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

# Wbudowane URLLIBS są straszne

# Nadchodzi nowa jakość Requests
import requests

class LocalSender:
    def __init__(self,data,*args,**kwargs):
        self.json_data = data
    URL = 'http://127.0.0.1:8000/endpoint/createupdateAPI'
    def check_connection(self):
        req = requests.post(self.URL)
        return req.status_code
    def send(self):
        r = requests.post(self.URL, json=self.json_data)

class TypeSender:
    def __init__(self,data,*args,**kwargs):
        self.json_data = data
    URL = 'http://127.0.0.1:8000/endpoint/type/'
    def check_connection(self):
        req = requests.post(self.URL)
        return req.status_code
    def send(self):
        r = requests.post(self.URL, json=self.json_data)

class CoorsSender:
    def __init__(self,coors,pk,*args,**kwargs):
        self.coors = coors
        self.pk = pk
    URL = 'http://127.0.0.1:8000/endpoint/coorsAPI'
    def check_connection(self):
        req = requests.get(self.URL)
        return req.status_code
    def send(self):
        r = requests.get(self.URL,params={'pk':self.pk,'coors':self.coors,'format':'json'})

class PKGet:
    def __init__(self,name,*args,**kwargs):
        self.name = name
    URL = 'http://127.0.0.1:8000/endpoint/searchAPI'
    def check_connection(self):
        req = requests.get(self.URL)
        return req.status_code
    def send(self):
        r = requests.get(self.URL,params={'name':'^' + self.name + '$','format':'json'})
        return int(json.loads(r.text)['results'][0]['id'])