# coding=utf-8
from rest_framework import generics
from zorya.models import StellarObject
from zorya.serializer import StellarObjectSerializer, SimpleStellarSerializer
from zorya.views import StandardResultsSetPagination, HintSetPagination

__author__ = 'root'


class StandartSearchAPI(generics.ListAPIView):
    """Endpoint dla wyszukiwarki
    """

    def get_queryset(self):
        stellarquery = StellarObject.objects.all()
        constellation = self.request.query_params.get('const', None)
        type_ = self.request.query_params.get('otype', None)
        catalogue = self.request.query_params.get('cat', None)
        latitude = self.request.query_params.get('lat', None)
        name = self.request.query_params.get('name', None)
        adv = self.request.query_params.get('adv',None)
        orderby =self.request.query_params.get('orderby', None)
        withmag = self.request.query_params.get('withmag',None)
        max_mag = self.request.query_params.get('max_mag', None)
        min_mag = self.request.query_params.get('min_mag',None)
        hint = self.request.query_params.get('hint', None)


        if max_mag and min_mag:
            stellarquery = stellarquery.filter(magnitudo__lte=max_mag,magnitudo__gte=min_mag)
        if withmag == 'false':
            stellarquery = stellarquery | StellarObject.objects.filter(magnitudo__isnull=True)

        if constellation:
            constellation = constellation.split(',')
            stellarquery = stellarquery.filter(constelation__abbreviation__in=constellation)
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

        if name:
            stellarquery = stellarquery.filter(bibcode__name__iregex=name).order_by('bibcode__name_length').order_by()
            return stellarquery.distinct()

        if orderby:
            if orderby == 'constelation':
                stellarquery =  stellarquery.order_by('constelation__abbreviation')
            if orderby == '-constelation':
                stellarquery = stellarquery.order_by('-constelation__abbreviation')
            else:
                stellarquery =  stellarquery.order_by(orderby)
        else:
            stellarquery = stellarquery.order_by('magnitudo')
        return stellarquery.distinct()



class SearchAPI(StandartSearchAPI):
    pagination_class = StandardResultsSetPagination
    serializer_class = StellarObjectSerializer


class HintAPI(StandartSearchAPI):
    serializer_class = SimpleStellarSerializer
    pagination_class = HintSetPagination
