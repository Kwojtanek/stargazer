# coding=utf-8
import re

from django.db import models
from django.core.exceptions import ValidationError

__author__ = 'kuba'

# TODO Mój błąd funkcje mnożą i dzielą przez 60 a powinny przez 90


class DeclinationField(models.Field):
    """ Pole deklinacji przechowuje dane jako Integer. Zwraca je pod postacia ciagu znakow w formacie 00°00'00 \
    Deklinacja jest miarą kąta i nie może być większa niż 90stopni"""

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        d = value/3600
        m = (value - d*3600)/ 60
        s = value - d*3600 - m * 60
        #deg_sign = u'\u00b0'
        #return u'%s%s%s\'%s"' % (d, deg_sign, m, s)
        return u'%s %s %s' % (d,  m, s)


    def get_db_prep_value(self, value, connection, prepared=True):
        if value is None:
            return value
        pattern = re.compile('-*\d{1,2}')
        multip = 3600
        s = re.findall(pattern,value)
        suma = 0
        for ob in s:
            ob = int(ob)
            if ob > 90 :
                raise ValidationError('Wrong Format for declination')
            suma = suma + int(ob)*multip
            multip /= 60
        value = suma
        return super(DeclinationField, self).get_db_prep_value(value=value, connection=connection, prepared=prepared)

    def get_db_prep_save(self, value, connection):
        if value is None:
            return value
        pattern = re.compile('-*\d{1,2}')
        multip = 3600
        s = re.findall(pattern,value)
        suma = 0
        for ob in s:
            ob = int(ob)

            if ob > 90 :
                raise ValidationError('Wrong Format for declination')
            suma = suma + int(ob)*multip
            multip /= 60
        value = suma
        return super(DeclinationField, self).get_db_prep_value(value=value, connection=connection)
