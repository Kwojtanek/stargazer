# -*- coding=utf-8 -*-
__author__ = 'kuba'
from rest_framework import serializers
from .models import Objects_list, StellarObject, Constellations,\
    Catalogues, ObjectPhotos, AstroCharts, BugTracker,\
    ContactApplet, ReletedType, BibCode, Source


class NGCNestedSerializer(serializers.ModelSerializer):
    """
    Backward Stellar object Serializer
    """
    object_catalogue = serializers.StringRelatedField()

    class Meta:
        model = Objects_list
        fields = ('object_catalogue', 'object_number',)

class PhotoPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectPhotos

class ReletedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReletedType


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

class BibcodesSerializer(serializers.ModelSerializer):
    class Meta:
        model= BibCode
        fields = ('name',)

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('name',)


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
    source = SourceSerializer(
        many=True,
        read_only=True
    )
    bibcode = BibcodesSerializer(
        many=True,
        read_only=True
    )
    fov = serializers.ReadOnlyField(
        read_only=True
    )
    first_catalogue = serializers.ReadOnlyField(
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
    stellarobscount = serializers.ReadOnlyField(
        read_only=True,
    )

    class Meta:
        model = Constellations


class CatalogueSerializer(serializers.ModelSerializer):
    stellarobscount = serializers.ReadOnlyField(
        read_only=True,
    )

    class Meta:
        model = Catalogues


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstroCharts
        fields = ('file_name', 'magnitudo')

class BugTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BugTracker

class ContactAppletSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactApplet

class StellarObjectSerializer2(serializers.ModelSerializer):
    class Meta:
        model = StellarObject


class SimpleStellarSerializer(serializers.ModelSerializer):
    bibcode = BibcodesSerializer(
        many=True,
        read_only=True
    )
    catalogues = NGCNestedSerializer(
        many=True,
        read_only=True
    )
    class Meta:
        model = StellarObject
        fields = ('bibcode','catalogues')
