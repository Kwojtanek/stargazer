# -*- coding=utf-8 -*-
import re
import datetime

from django.db import models
from DjangoSettings.DevSettings import MEDIA_URL
from .fields import DeclinationField
from .thumbs import ImageWithThumbsField


class Constellations(models.Model):
    """
    Class for constellation object, Every Stellar Object is related to only one constellation.
    """
    abbreviation = models.CharField(max_length=3, unique=True, blank=False)
    constellation = models.CharField(max_length=128, unique=True, blank=False)
    other_abbreviation = models.CharField(max_length=4, blank=False, unique=True)
    genitive = models.CharField(max_length=128, unique=True, blank=False)
    family = models.CharField(max_length=32, blank=False)
    origin = models.CharField(max_length=64, blank=False)
    meaning = models.CharField(max_length=128, blank=False)
    brightest_star = models.CharField(max_length=32, unique=True, blank=False)

    def __unicode__(self):
        return self.constellation

    def stellarobscount(self):
        """

        :return: count of objects in constellation
        """
        c = Constellations.objects.get(id=self.pk)
        return c.relatedconstellation.all().count()


class StellarObject(models.Model):
    """
    Base class of object that holds all information.
    Forward related to constellation
    Backward related to objects list can have many of them
    Backward related to Photo object

    """
    unique_name = models.CharField(max_length=32, unique=True)
    otype = models.CharField(max_length=24, null=True, blank=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    type_shortcut = models.CharField(max_length=12, blank=True, null=True)
    classe = models.CharField(max_length=12, blank=True, null=True)
    rightAsc = models.TimeField(blank=True, null=True)
    declination = DeclinationField(blank=True, null=True)
    distance = models.IntegerField(blank=True, null=True)

    constelation = models.ForeignKey(Constellations, related_name='relatedconstellation')

    magnitudo = models.FloatField(max_length=5, blank=True, null=True)
    dimAxb = models.CharField(max_length=32, blank=True, null=True)
    pa = models.SmallIntegerField(blank=True, null=True)
    description = models.CharField(max_length=128, blank=True, null=True)

    id1 = models.CharField(max_length=32, blank=True, null=True)
    id2 = models.CharField(max_length=32, blank=True, null=True)
    id3 = models.CharField(max_length=32, blank=True, null=True)
    notes = models.CharField(max_length=64, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.unique_name

    def fov(self):
        """
        Function returns Field of view that will be passed to aladdin map api
        """
        x = 0
        if self.dimAxb:
            pattern = re.compile('\d+.\d+')
            numb = re.findall(pattern, self.dimAxb)
            if len(numb) == 0:
                return 10
            for n in numb:
                if n >= x:
                    x = n
            x = float(x) / 100
            if x > 1:
                return x * 5
            if x <= 1:
                return x * 10
            if x <= 0.1:
                return x * 25
            else:
                return 10

        else:
            return 10


class Catalogues(models.Model):
    """
    Class that holds name and description of catalogue
    It's related to objects_list
    """
    name = models.CharField(max_length=64, unique=True, blank=False)
    description = models.CharField(max_length=1024, blank=True)

    def __unicode__(self):
        return self.name

    def stellarobscount(self):
        c = Catalogues.objects.get(id=self.pk)
        return c.Catalogue.all().count()


class Objects_list(models.Model):
    """
    Mediative class between catalogue and stellar object.
    Every stellar object can be in many catalogues and have unique name or number in it.
    """
    single_object = models.ForeignKey(StellarObject, related_name='catalogues')
    object_catalogue = models.ForeignKey(Catalogues, related_name='Catalogue')
    object_number = models.CharField(max_length=16)

    def __unicode__(self):
        return u'%s number %s' % (str(Catalogues.objects.get(pk=self.object_catalogue.pk)),
                                  str(StellarObject.objects.get(pk=self.single_object.pk)))


class ObjectPhotos(models.Model):
    """
    This Class contains all photos related to StellarObject,
     both uploaded to server and links to photo from different server
     """

    name = models.CharField(max_length=128, blank=True, null=True)
    photo = ImageWithThumbsField(upload_to='images', sizes=((410, 230), (1280, 718)), blank=True, null=True)
    photo_url = models.URLField(blank=True, null=True)
    photo_thumbnail = models.URLField(blank=True,null=True)
    ngc_object = models.ForeignKey(StellarObject, related_name='photos')

    def __unicode__(self):
        if self.photo:
            return self.photo.url_410x230
        else:
            return self.photo_thumbnail

    # Na potrzeby serializera
    def thumb(self):
        if self.photo:
            return self.photo.url_410x230
        else:
            return self.photo_thumbnail

    def normal(self):
        if self.photo:
            return self.photo.url_1280x718
        else:
            return self.photo_url

    def orginal(self):
        if self.photo:
            return '%s%s' % (MEDIA_URL, self.photo.name)
        else:
            return self.photo_url


# TODO Wgrać Fixtury do zdjęć

class AstroCharts(models.Model):
    """
    Class of map. Path is kept in file_name
    """
    file_name = models.CharField(max_length=16)
    maxAscension = models.TimeField()
    minAscension = models.TimeField()
    maxDeclination = DeclinationField(blank=True, null=True)
    minDeclination = DeclinationField(blank=True, null=True)
    magnitudo = models.DecimalField(max_digits=3, decimal_places=1)


class BugTracker(models.Model):
    """
    Saves bugs
    """
    info = models.TextField()
    dateandtime = models.DateTimeField(default=datetime.datetime.now)
    userAgent = models.CharField(max_length=256)
    author = models.EmailField(null=True, blank=True)
    bugUrl = models.CharField(max_length=64)
    addicionalinfo = models.CharField(max_length=32,null=True, blank=True)


class ContactApplet(models.Model):
    author = models.EmailField()
    message = models.TextField()


class ReletedType(models.Model):
    """
    Class represents type of given StellarObject that will be linked by foreign key
    """

    # Type is releted to itself becouse in example blazar is also a galaxy
    maintype = models.ForeignKey('self')
    nametype = models.CharField(max_length=80)
    shortcutnametype = models.CharField(max_length=32)
    phototype = ImageWithThumbsField(upload_to='images', sizes=((410, 230), (1280, 718)), blank=True, null=True)
    descriptiontype = models.TextField()

    # TODO POłączyć StellarObjects z typem
