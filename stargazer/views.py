# -*- coding=utf-8 -*-
import json, datetime
from django.shortcuts import render_to_response, HttpResponse
from django.template import loader, Context, RequestContext
from django.db.models import Q

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .filters import StellarListFilter
from .models import Objects_list, StellarObject, Catalogues, Constellations, AstroCharts
from .serializer import StellarObjectSerializer, ConstellationsSerializer, ObjectsSerializer, CatalogueSerializer

#TODO napisz stronę 404 Not Found
#TODO Mixins
# Paginatory
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 500


# Strona glowna
def MainView(request):
    return render_to_response(
        'stargazer/Browse.html',
        {'Catalogues': Catalogues.objects.all()}, RequestContext(request))

# Wyszukiwarka
class SearchAPI(generics.ListAPIView):
    pagination_class = StandardResultsSetPagination
    serializer_class = StellarObjectSerializer
    filter_class = StellarListFilter

    def get_queryset(self):
        stellarquery = StellarObject.objects.all()
        constellation = self.request.query_params.get('const', None)
        type_ = self.request.query_params.get('type', None)
        catalogue = self.request.query_params.get('cat', None)
        latitude = self.request.query_params.get('lat', None)
        n = self.request.query_params.get('name', None)
        if constellation:
            constellation = constellation.split(',')
            stellarquery = stellarquery.filter(constelation__abbreviation__in=constellation)
        if type_:
            type_ = type_.split(',')
            stellarquery = stellarquery.filter(type_shortcut__in=type_)
        if catalogue:
            catalogue = catalogue.split(',')
            stellarquery = stellarquery.filter(catalogues__object_catalogue__name__in=catalogue)
        if latitude:
            latitude = int(float(latitude))
            ln = latitude
            if latitude > 0:
                ln -= 90
                stellarquery = stellarquery.filter(declination__gte=str(ln))
            if latitude < 0:
                ln += 90
                stellarquery = stellarquery.filter(declination__lte=str(ln))
        qn = StellarObject.objects.none()
        if n:
            n = n.replace(',', ' ')
            n = n.split()

            #TODO Brzyćkie i niewydajne, do poprawienia!, a może Haystack
            for x in n:
                if x == 'm' or x == 'M':
                    x = 'Messier'
                if Catalogues.objects.filter(name=x).exists():
                    qn = qn|stellarquery.filter(catalogues__object_catalogue__name__iexact=x)
                if x.isdigit():
                    qn = qn.filter(catalogues__object_number__exact=x)

                else:
                    qn = qn | (stellarquery.filter(Q(unique_name__icontains=x)|Q(id1__icontains=x)|Q(id__icontains=x)|Q(id3__icontains=x)|Q(notes__icontains=x)))
            return qn.order_by('magnitudo').distinct()
        else:
            return stellarquery.order_by('magnitudo')