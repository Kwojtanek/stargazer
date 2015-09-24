# -*- coding=utf-8 -*-
from django.db import models
from DjangoSettings.DevSettings import MEDIA_URL
from .fields import DeclinationField
from .thumbs import ImageWithThumbsField


class Constellations(models.Model):
    abbreviation = models.CharField(max_length=3, unique=True,blank=False)
    constellation = models.CharField(max_length=128, unique=True, blank=False)
    other_abbreviation = models.CharField(max_length=4, blank=False, unique=True)
    genitive = models.CharField(max_length=128, unique=True, blank=False)
    family = models.CharField(max_length=32, blank=False)
    origin = models.CharField(max_length=64, blank=False)
    meaning = models.CharField(max_length=128, blank=False)
    brightest_star = models.CharField(max_length=32, unique=True, blank=False)

    def __unicode__(self):
        return self.constellation

    def numNGCS(self):
        c = Constellations.objects.get(id=self.pk)
        return c.ngcs.all().count()


class StellarObject(models.Model):
    unique_name = models.CharField(max_length=32, unique=True)
    type = models.CharField(max_length=100, blank=True,null=True)
    type_shortcut = models.CharField(max_length=12,blank=True,null=True)
    classe = models.CharField(max_length=12, blank=True,null=True)
    rightAsc = models.TimeField(blank=True,null=True)
    declination = DeclinationField(blank=True,null=True)
    distance = models.IntegerField(blank=True, null=True)

    constelation = models.ForeignKey(Constellations, related_name='ngcs')

    magnitudo = models.FloatField(max_length=5, blank=True, null=True)
    dimAxb = models.CharField(max_length=32, blank=True,null=True)
    pa = models.SmallIntegerField(blank=True,null=True)
    description = models.CharField(max_length=128, blank=True,null=True)


    id1 = models.CharField(max_length=32, blank=True,null=True)
    id2 = models.CharField(max_length=32, blank=True,null=True)
    id3 = models.CharField(max_length=32, blank=True,null=True)
    notes = models.CharField(max_length=64, blank=True,null=True)
    overview = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return (self.unique_name)


class Catalogues(models.Model):
    name = models.CharField(max_length=64, unique=True, blank=False)
    description = models.CharField(max_length=1024, blank=True)

    def __unicode__(self):
        return self.name

    def numNGCS(self):
        c = Catalogues.objects.get(id=self.pk)
        return c.Catalogue.all().count()


class Objects_list(models.Model):
    single_object = models.ForeignKey(StellarObject, related_name='catalogues')
    object_catalogue = models.ForeignKey(Catalogues, related_name='Catalogue')
    object_number = models.CharField(max_length=16)

    def __unicode__(self):
        return u'%s number %s' % (str(Catalogues.objects.get(pk=self.object_catalogue.pk)), str(StellarObject.objects.get(pk=self.single_object.pk)))
class ObjectPhotos(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    photo = ImageWithThumbsField(upload_to='images', sizes=((410,230),(1280,718)), blank=True, null=True)
    photo_url = models.URLField(blank=True,null=True)
    ngc_object = models.ForeignKey(StellarObject, related_name='photos')

    def __unicode__(self):
        return self.photo.url_410x230

    #Na potrzeby serializera
    def thumb(self):
        if self.photo:
            return self.photo.url_410x230
        else:
            return self.photo_url
    def normal(self):
        if self.photo:
            return self.photo.url_1280x718
        else:
            return self.photo_url
    def orginal(self):
        if self.photo:
            return '%s%s' % (MEDIA_URL,self.photo.name)
        else:
            return self.photo_url

#TODO Wgrać Fixtury do zdjęć

class AstroCharts(models.Model):
    file_name = models.CharField(max_length=16)
    maxAscension = models.TimeField()
    minAscension = models.TimeField()
    maxDeclination = DeclinationField(blank=True,null=True)
    minDeclination = DeclinationField(blank=True,null=True)
    magnitudo = models.DecimalField(max_digits=3, decimal_places=1)
