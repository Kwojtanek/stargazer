# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response, HttpResponse
from django.template import loader, Context, RequestContext
from django.db.models import Q

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .filters import StellarListFilter
from .models import Objects_list, StellarObject, Catalogues, ObjectPhotos, Constellations
from .serializer import NGCSerializer, ConstellationsSerializer, ObjectsSerializer, CatalogueSerializer

#TODO napisz stronę 404 Not Found
#TODO Mixins
# Paginatory
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 200


# Strona glowna
def MainView(request):
    return render_to_response(
        'stargazer/Browse.html',
        {'Catalogues': Catalogues.objects.all()}, RequestContext(request))

# Endpointy API

# Wyszukiwarka
class SearchAPI(generics.ListAPIView):
    pagination_class = StandardResultsSetPagination
    serializer_class = NGCSerializer
    filter_class = StellarListFilter

    def get_queryset(self):
        q = StellarObject.objects.all()
        c = self.request.QUERY_PARAMS.get('const', None)
        t = self.request.QUERY_PARAMS.get('type', None)
        C = self.request.QUERY_PARAMS.get('cat', None)
        l = self.request.QUERY_PARAMS.get('lat', None)
        n = self.request.QUERY_PARAMS.get('name', None)
        if c:
            c = c.split(',')
            q = q.filter(constelation__abbreviation__in=c)
        if t:
            t = t.split(',')
            q = q.filter(type_shortcut__in=t)
        if C:
            C = C.split(',')
            q = q.filter(catalogues__object_catalogue__name__in=C)
        if l:
            l = int(float(l))
            ln = l
            if l > 0:
                ln -= 90
                q = q.filter(declination__gte=str(ln))
            if l < 0:
                ln += 90
                q = q.filter(declination__lte=str(ln))
        qn = StellarObject.objects.none()
        if n:
            print type(n)
            n = n.replace(',', ' ')
            n = n.split()

            #TODO Brzyćkie i niewydajne, do poprawienia!, a może Haystack
            for x in n:
                if x == 'm' or x == 'M':
                    x = 'Messier'
                if Catalogues.objects.filter(name=x).exists():
                    qn = qn|q.filter(catalogues__object_catalogue__name__iexact=x)
                if x.isdigit():
                    qn = qn.filter(catalogues__object_number__exact=x)

                else:
                    qn = qn | (q.filter(Q(unique_name__icontains=x)|Q(id1__icontains=x)|Q(id__icontains=x)|Q(id3__icontains=x)|Q(notes__icontains=x)))
            return qn.order_by('catalogues__object_number')
        else:
            return q.order_by('magnitudo')

class SingleView(generics.RetrieveAPIView):
    serializer_class = NGCSerializer
    queryset = StellarObject


class StellarViewAPI(generics.ListAPIView):
    queryset = StellarObject.objects.all()
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