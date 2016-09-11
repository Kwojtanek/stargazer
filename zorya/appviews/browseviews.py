# coding=utf-8
from django.db.models import Count
from rest_framework import generics
from zorya.models import StellarObject, Constellations, Catalogues, Objects_list
from zorya.serializer import StellarObjectSerializer, ConstellationsSerializer, CatalogueSerializer, \
    ObjectsSerializer
from zorya.views import StandardResultsSetPagination

__author__ = 'root'
#TODO Endpointy i  Widoki dla konstelacji, typów i katalogów

class SingleView(generics.RetrieveAPIView):
    serializer_class = StellarObjectSerializer
    queryset = StellarObject


class StellarViewAPI(generics.ListAPIView):
    q = StellarObject.objects.all()
    queryset = q.order_by('-photos')
    pagination_class = StandardResultsSetPagination
    serializer_class = StellarObjectSerializer


# Konstelacje
class ConstellationsListViewAPI(generics.ListAPIView):
    serializer_class = ConstellationsSerializer
    queryset = Constellations.objects.all()


class SingleConstellationViewAPI(generics.RetrieveAPIView):
    lookup_field = 'abbreviation'
    serializer_class = ConstellationsSerializer
    queryset = Constellations


class ConstellationsViewDetailAPI(generics.ListAPIView):
    pagination_class = StandardResultsSetPagination
    serializer_class = StellarObjectSerializer

    def get_queryset(self):
        constellation_name = self.kwargs['abbreviation']
        c = Constellations.objects.get(abbreviation=constellation_name)
        quryset = c.relatedconstellation.all()
        return quryset


# Katalogi
class SingleCatalogueViewAPI(generics.RetrieveAPIView):
    queryset = Catalogues
    lookup_field = 'name'
    serializer_class = CatalogueSerializer


class CataloguesListViewAPI(generics.ListAPIView):
    queryset = Catalogues
    serializer_class = CatalogueSerializer

#Lista obiektów w katalogue
class CataloguesViewAPI(generics.ListAPIView):
    pagination_class = StandardResultsSetPagination
    serializer_class = StellarObjectSerializer

    def get_queryset(self):
        catalogue_name = self.kwargs['cat']
        queryset = StellarObject.objects.annotate(num_p=Count('photos'))\
            .filter(catalogues__object_catalogue__name=catalogue_name).order_by('-num_p')
        return queryset
#Lista obiektów w danym typie.
class TypeViewAPI(generics.ListAPIView):
    pagination_class = StandardResultsSetPagination
    serializer_class = StellarObjectSerializer
    def get_queryset(self):
        typesc = self.kwargs['typesc']
        queryset = StellarObject.objects.annotate(num_p=Count('photos'))\
            .filter(type_shortcut=typesc).order_by('-num_p')
        return queryset
#Lista obiektów w danej konstelacji
class ConstellationsViewAPI(generics.ListAPIView):
    pagination_class = StandardResultsSetPagination
    serializer_class = StellarObjectSerializer

    def get_queryset(self):
        constellation_name = self.kwargs['abbreviation']
        c = Constellations.objects.get(abbreviation=constellation_name)
        quryset = c.relatedconstellation.all()
        return quryset

