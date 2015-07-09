# -*- coding=utf-8 -*-
__author__ = 'kuba'

from rest_framework import serializers
from .models import Objects_list, StellarObject, Constellations, Catalogues

#Backward Ngc Serializer
class NGCNestedSerializer(serializers.ModelSerializer):
    object_catalogue = serializers.StringRelatedField()
    class Meta:
        model = Objects_list
        fields = ('object_catalogue', 'object_number',)

class NGCSerializer(serializers.ModelSerializer):
    catalogues = NGCNestedSerializer(
        many=True,
        read_only=True
    )
    constelation = serializers.SlugRelatedField(
        read_only=True,
        slug_field='abbreviation'
     )
    url = serializers.HyperlinkedIdentityField(
        view_name='SingleUrl',
        lookup_field='pk'
    )
    catalogues_list = serializers.ReadOnlyField(
        read_only=True,
    )

    #TODO dla każdego rozmiaru zdjęcia zwraca hiperlink, Do poprawy, bo błądzi.
    """photos = serializers.HyperlinkedRelatedField(
        read_only=True,
        many = True,
        view_name='Media_url',
        lookup_field='name'
    )
"""
    class Meta:
        model = StellarObject

#Forward Ngc serializer
class ObjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Objects_list
        fields = ('object_number', 'single_object')
        depth = 1

#Serializer dla konstelacji
class ConstellationsSerializer(serializers.ModelSerializer):
    NGCS_number = serializers.ReadOnlyField(
        source='numNGCS',
        read_only=True,
    )
    class Meta:
        model = Constellations


class CatalogueSerializer(serializers.ModelSerializer):
    NGCS_number = serializers.ReadOnlyField(
        source='numNGCS',
        read_only=True,
    )
    class Meta:
        model = Catalogues
