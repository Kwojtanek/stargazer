# coding=utf-8
import re

from django.db import models
from django.core.exceptions import ValidationError

__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'

class DeclinationField(models.Field):
    """
    Declination is geographical counterpart of latitude in cartesian system but projected on a sphere.
    Data is represented in sexagesimals including hour not biger than 90 degree, 1/4 of sphere.
    Declinations with magnitudes greater than 90° do not occur, because the poles are the northernmost and southernmost points
    of the celestial sphere.

     Only representation and savings are changed and data is stored in arc seconds.
     Field inherits from simple integer field.
     Becouse of above it allows user to do all standard aritmetics.


     Usage:
     Simply import from filds DeclinationField to your orm model.

     Inputs:
     Class allows to posible inputs:
        -Integer number in arcseconds
        -String representation i.e. ; '01 01 01', '+41° 16′ 9', '-00 03 01', etc.
         Generally it must contain 3 sets of digits to procceed or it will raise ValueError
    """
    def __init__(self, *args, **kwargs):
        kwargs['blank'] = True
        super(DeclinationField, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return u'Declination Field'

    def __str__(self):
        return 'Declination Field'

    def deconstruct(self):
        name, path, args, kwargs = super(DeclinationField, self).deconstruct()
        return name, path, args, kwargs

    def db_type(self, connection):
        return 'INT'

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        if value >= 0:
            negative = False
        if value < 0:
            negative = True
        value = abs(value)
        angle = value/3600
        minute = (value - angle*3600)/60
        sec = value - angle*3600 - minute*60
        if negative:
            angle = '-' + str(angle)
        # return u'%s°%s\'%s"' % (angle,minute, sec)
        return '%s %s %s' % (angle,minute, sec)


    def get_db_prep_value(self, value, connection, prepared=True):
        #if none provided return none
        if value is None:
            return value
        #if negative
        if value[0] == '-':
            value = value[1:]
            negative = True
        else: negative = False
        pattern = re.compile('\d{1,2}')
        dec = re.findall(pattern,value)
        if len(dec) >0:
            angle = dec[0]
        else:
            raise ValidationError('Wrong Format for declination %s' % value)
        if len(dec) >1:
            minute = dec[1]
        else:
            minute = 0
        if len(dec) >2:
            sec = dec[2]
        else:
            sec = 0
        dec_sum = int(angle)*3600 + int(minute)*60 + int(sec)
        if negative:
            dec_sum =dec_sum*-1
        return super(DeclinationField, self).get_db_prep_value(value=dec_sum, connection=connection, prepared=prepared)

    def get_db_prep_save(self, value, connection):
        #if none provided return none
        if value is None:
            return value
        #if negative
        if value[0] == '-':
            value = value[1:]
            negative = True
        else: negative = False
        pattern = re.compile('\d{1,2}')
        dec = re.findall(pattern,value)
        if len(dec) >0:
            angle = dec[0]
        else:
            raise ValidationError('Wrong Format for declination %s' % value)
        if len(dec) >1:
            minute = dec[1]
        else:
            minute = 0
        if len(dec) >2:
            sec = dec[2]
        else:
            sec = 0
        dec_sum = int(angle)*3600 + int(minute)*60 + int(sec)
        if negative:
            dec_sum =dec_sum*-1
        return super(DeclinationField, self).get_db_prep_value(value=dec_sum, connection=connection)