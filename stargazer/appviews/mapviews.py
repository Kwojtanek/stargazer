# coding=utf-8
import datetime

from rest_framework.decorators import api_view

from rest_framework.response import Response

from stargazer.models import AstroCharts
from DjangoSettings.settings import STATIC_URL

__author__ = 'root'

# Folder w którym znajdują się mapy
CHARTS_DIRS = STATIC_URL + 'astrocharts/'


@api_view()
def mapapi(request):
    """Widok pobiera parametry z GET i dopasowywuje odpowiednią mapę. \
    Każda mapa ma przypisane wartości. Max. i Min. deklinację  i rektescancję"""
    if 'asc' in request.GET and 'dec' in request.GET:
        asc = request.GET['asc']
        dec = request.GET['dec']
    else:
        return Response({'chart': 'Not enough data'})
    try:
        asc = datetime.datetime.strptime(asc, '%H:%M:%S')
        astro = AstroCharts.objects.filter(maxDeclination__gte=dec).filter(minDeclination__lte=dec)
        try:
            astrof = astro.filter(minAscension__gte=asc).order_by('minAscension')
            results = {
                'small': {'file_name': CHARTS_DIRS + astrof.filter(magnitudo=9).first().file_name, 'magnitudo': 9},
                'medium': {'file_name': CHARTS_DIRS + astrof.filter(magnitudo=11).first().file_name, 'magnitudo': 11},
                'big': {
                    'file_name': CHARTS_DIRS + astrof.filter(magnitudo__range=(12.5, 12.7)).first().file_name,
                    'magnitudo': 12.6
                }
            }
            return Response(results)
        except:
            astrof = astro.filter(maxAscension__lte=asc).order_by('-maxAscension')
            results = {
                'small': {'file_name': CHARTS_DIRS + astrof.filter(magnitudo=9).first().file_name, 'magnitudo': 9},
                'medium': {'file_name': CHARTS_DIRS + astrof.filter(magnitudo=11).first().file_name, 'magnitudo': 11},
                'big': {
                    'file_name': CHARTS_DIRS + astrof.filter(magnitudo__range=(12.5, 12.7)).first().file_name,
                    'magnitudo': 12.6}
            }
            return Response(results)

    except:
        return Response({'chart': 'Wrong format'})
