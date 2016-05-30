# # coding=utf-8
# import re
#
# from django.db import models
# from django.core.exceptions import ValidationError
#
# __author__ = 'kuba'
# class Cordinate(object):
#     def __init__(self,coordinate):
#         self.coordinate = coordinate
#
#     def __repr__(self):
#
#
# class DeclinationField(models.Field):
#     """
#     Pole deklinacji przechowuje dane jako Integer. Zwraca je pod postacia ciagu znakow w formacie 00°00'00 \
#     """
#     def __init__(self, *args, **kwargs):
#         kwargs['blank'] = True
#         super(DeclinationField, self).__init__(*args, **kwargs)
#
#     def __unicode__(self):
#         return u'Declination Field'
#
#     def __str__(self):
#         return 'Declination Field'
#
#     def deconstruct(self):
#         name, path, args, kwargs = super(DeclinationField, self).deconstruct()
#         del kwargs["max_length"]
#         return name, path, args, kwargs
#
#     def db_type(self, connection):
#         return 'INT'
#     def to_ints(self, value):
#         #Converts to int
#         if value is None:
#             return value
#         pattern = re.compile('-*\d{2}|-*\d{1}')
#         s = re.findall(pattern,value)
#         multip = 3600
#         suma = 0
#         if len(s) > 3:
#             s = s[0:3]
#         for ob in s:
#             ob = int(ob)
#             if ob > 90 or  ob < -90:
#                 return "Wrong Format, %s" % value
#             suma = suma + int(ob)*multip
#             multip /= 60
#         value = suma
#         return value
#     def to_declination(self, value):
#         #converts to dec
#         if value is None:
#             return value
#         value = int(value)
#         d = value/3600
#         m = (value - d*3600)/ 60
#         s = value - d*3600 - m * 60
#         if d< 0:
#             str(d).zfill(3)
#         else:
#             str(d).zfill(2)
#
#         deg_sign = '\u00b0'
#         #return u'%s%s%s\'%s"' % (d, deg_sign, m, s)
#         return '%s %s %s' % (d,str(m).zfill(2), str(s).zfill(2))
#
#     def to_python(self, value):
#         return self.to_declination(value)
#     def get_db_prep_value(self, value,connection,prepared=False):
#         return self.to_ints(value)
import re

from django.db import models
from django.core.exceptions import ValidationError

__author__ = 'kuba'

class DeclinationField(models.Field):
    """ Pole deklinacji przechowuje dane jako Integer. Zwraca je pod postacia ciagu znakow w formacie 00°00'00 \
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
        d = value/3600
        m = (value - d*3600)/ 60
        s = value - d*3600 - m * 60
        deg_sign = u'\u00b0'
        #return u'%s%s%s\'%s"' % (d, deg_sign, m, s)
        return u'%s %s %s' % (str(d).zfill(2), str(m).zfill(2), str(s).zfill(2))


    def get_db_prep_value(self, value, connection, prepared=True):
        if value is None:
            return value
        pattern = re.compile('-*\d{1,2}')
        multip = 3600
        s = re.findall(pattern,value)
        suma = 0
        if len(s) > 3:
            s = s[0:3]
        for ob in s:
            ob = int(ob)
            if ob > 90 :
                raise ValidationError('Wrong Format for declination %s' % value)
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
        if len(s) > 3:
            s = s[0:3]
        for ob in s:
            ob = int(ob)

            if ob > 90 :
                raise ValidationError('Wrong Format for declination %s' % value)
            suma = suma + int(ob)*multip
            multip /= 60
        value = suma
        return super(DeclinationField, self).get_db_prep_value(value=value, connection=connection)
