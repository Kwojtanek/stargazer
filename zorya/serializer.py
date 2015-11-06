# -*- coding=utf-8 -*-
__author__ = 'kuba'

from rest_framework import serializers
from .models import Objects_list, StellarObject, Constellations, Catalogues, ObjectPhotos, AstroCharts


class NGCNestedSerializer(serializers.ModelSerializer):
    """
    Backward Stellar object Serializer
    """
    object_catalogue = serializers.StringRelatedField()

    class Meta:
        model = Objects_list
        fields = ('object_catalogue', 'object_number',)


class PhotoSerializer(serializers.ModelSerializer):
    thumb = serializers.ReadOnlyField(
        read_only=True,
    )
    normal = serializers.ReadOnlyField(
        read_only=True,
    )
    orginal = serializers.ReadOnlyField(
        read_only=True
    )

    class Meta:
        model = ObjectPhotos
        fields = ('thumb', 'normal', 'orginal')


class StellarObjectSerializer(serializers.ModelSerializer):
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

    photos = PhotoSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = StellarObject


class ObjectsSerializer(serializers.ModelSerializer):
    """
    Forward Stellar object serializer
    """

    class Meta:
        model = Objects_list
        fields = ('object_number', 'single_object')
        depth = 1


class ConstellationsSerializer(serializers.ModelSerializer):
    """
     Serializer dla konstelacji
    """
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


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstroCharts
        fields = ('file_name', 'magnitudo')