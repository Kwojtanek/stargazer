# coding=utf-8
from django.db.models import Q
from rest_framework import generics
from zorya.filters import StellarListFilter
from zorya.models import StellarObject, Catalogues
from zorya.serializer import StellarObjectSerializer
from zorya.views import StandardResultsSetPagination

__author__ = 'root'


class SearchAPI(generics.ListAPIView):
    """Endpoint dla wyszukiwarki
    """
    pagination_class = StandardResultsSetPagination
    serializer_class = StellarObjectSerializer
    filter_class = StellarListFilter

    def get_queryset(self):
        stellarquery = StellarObject.objects.all()
        constellation = self.request.query_params.get('const', None)
        type_ = self.request.query_params.get('otype', None)
        catalogue = self.request.query_params.get('cat', None)
        latitude = self.request.query_params.get('lat', None)
        n = self.request.query_params.get('name', None)
        adv = self.request.query_params.get('adv',None)
        orderby =self.request.query_params.get('orderby', None)
        overview =self.request.query_params.get('overview', None)
        catalogue_number = self.request.query_params.get('cat_n',None)

        if constellation:
            constellation = constellation.split(',')
            stellarquery = stellarquery.filter(constelation__abbreviation__in=constellation)
        if overview:
            stellarquery = stellarquery.exclude(overview=None)
        if catalogue_number:
            stellarquery = stellarquery.filter(catalogues__object_number=catalogue_number)
        if type_:
            type_ = type_.split(',')
            if adv == 'true':
                stellarquery = stellarquery.filter(type_shortcut__in=type_)
            else:
                stellarquery = stellarquery.filter(otype__in=type_)
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

        if n:
            stellarquery = stellarquery.filter(bibcode__name__icontains=n).distinct()
        if orderby:
            if orderby == 'constelation':
                return stellarquery.order_by('constelation__abbreviation')
            if orderby == '-constelation':
                return stellarquery.order_by('-constelation__abbreviation')
            else:
                return stellarquery.order_by(orderby)
        else:
            return stellarquery.order_by('magnitudo')
