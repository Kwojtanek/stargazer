from rest_framework import generics
from zorya.models import StellarObject, Constellations, Catalogues, Objects_list
from zorya.serializer import StellarObjectSerializer, ConstellationsSerializer, CatalogueSerializer, \
    ObjectsSerializer
from zorya.views import StandardResultsSetPagination

__author__ = 'root'


class SingleView(generics.RetrieveAPIView):
    serializer_class = StellarObjectSerializer
    queryset = StellarObject


class StellarViewAPI(generics.ListAPIView):
    queryset = StellarObject.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = StellarObjectSerializer


# Konstelacje
class ConstellationsViewAPI(generics.ListAPIView):
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
        quryset = c.ngcs.all()
        return quryset


# Katalogi
class SingleCatalogueViewAPI(generics.RetrieveAPIView):
    queryset = Catalogues
    lookup_field = 'name'
    serializer_class = CatalogueSerializer


class CataloguesViewAPI(generics.ListAPIView):
    queryset = Catalogues
    serializer_class = CatalogueSerializer


class CataloguesDetailViewAPI(generics.ListAPIView):
    serializer_class = ObjectsSerializer

    def get_queryset(self):
        catalogue_name = self.kwargs['name']
        queryset = Objects_list.objects.filter(object_catalogue__name=catalogue_name)
        return queryset