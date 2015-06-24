# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response, HttpResponse
from django.template import loader, Context, RequestContext

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view

from .models import Objects_list, Ngc_list, Catalogues, NgcPhotos, Constellations
from .serializer import NGCSerializer, ConstellationsSerializer, ObjectsSerializer, CatalogueSerializer

#TODO napisz stronę 404 Not Found
#TODO Mixins
# Paginatory
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


# Strona glowna
def MainView(request):
    return render_to_response(
        'stargazer/ngc_list.html',
        {'Catalogues': Catalogues.objects.all()}, RequestContext(request))


# Wyszukiwarka
def SearchView(request):
    return render_to_response('stargazer/search.html')

# Endpointy API
def SearchAPI(request):
    if request.is_ajax():
        pass
    #TODO otrzymuje dane i zwraca filtrowaną listę obiektów

    #TODO Filtry napisać

class SingleView(generics.RetrieveAPIView):
    serializer_class = NGCSerializer
    queryset = Ngc_list


class NgcViewAPI(generics.ListAPIView):
    queryset = Ngc_list.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = NGCSerializer


#Konstelacje
class ConstellationsViewAPI(generics.ListAPIView):
    serializer_class = ConstellationsSerializer
    queryset = Constellations.objects.all()

class SingleConstellationViewAPI(generics.RetrieveAPIView):
    lookup_field = 'abbreviation'
    serializer_class = ConstellationsSerializer
    queryset = Constellations

class ConstellationsViewDetailAPI(generics.ListAPIView):
    pagination_class = StandardResultsSetPagination
    serializer_class = NGCSerializer

    def get_queryset(self):
        constellation_name = self.kwargs['abbreviation']
        c = Constellations.objects.get(abbreviation=constellation_name)
        quryset = c.ngcs.all()
        return quryset


#Katalogi
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