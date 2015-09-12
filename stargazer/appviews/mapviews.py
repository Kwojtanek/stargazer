# coding=utf-8
import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response

from stargazer.models import AstroCharts

from DjangoSettings.settings import STATIC_URL

__author__ = 'Jakub Wojtanek KWojtanek@gmail.com'

# Folder w którym znajdują się mapy
CHARTS_DIRS = 'astrocharts/'
CHARTS_URL = STATIC_URL + CHARTS_DIRS
MAGNITUDO = (9, 11, 12.6)

RESPONSES = {
    1: 'Map Found',
    2: 'Wrong Format',
    3: 'Map Not Found',
    4: 'Not Enough data'
}


@api_view()
def mapapi(request):
    """Widok pobiera parametry z GET i dopasowywuje odpowiednią mapę. \
    Każda mapa ma przypisane wartości. Magnitudo, max. i min. deklinację  i rektescancję \
    Dla deklinacji znajduje w query takie zasięg który,jest: max-dec >= dec < min-dec \
    Dla rektascancji ponieważ może być 23:30:00 -> 1:30:30 znajduje pierwszy większy niż min-rektescencja \
    lub jeśli nie występuje, ostatni mniejszy niż max-rektescencja """
    if 'asc' in request.GET and 'dec' in request.GET:
        asc = request.GET['asc']
        dec = request.GET['dec']
    else:
        k, v = RESPONSES.items()[3]
        return Response({'code': k,
                         'message': v})
    try:
        asc = datetime.datetime.strptime(asc, '%H:%M:%S')
    except ValueError:
        k, v = RESPONSES.items()[1]
        return Response({'code': k,
                         'message': v})

    astroquery = AstroCharts.objects.filter(maxDeclination__gte=dec).filter(minDeclination__lt=dec)
    result = {}
    for mag in MAGNITUDO:
        chartquery = astroquery.filter(magnitudo__range=((float(mag) - 0.1), (float(mag) + 0.1)))
        if chartquery.filter(minAscension__gte=asc).count() != 0:
            chart = chartquery.filter(minAscension__gte=asc).order_by('minAscension').first()
            result['MAG_%s' % mag] = {'url': CHARTS_URL + chart.file_name,
                                      'max_asc': chart.maxAscension,
                                      'min_asc': chart.minAscension,
                                      'max_dec': chart.maxDeclination,
                                      'min_dec': chart.minDeclination,
                                      'max_mag': chart.magnitudo
                                      }
        else:
            chart = chartquery.filter(maxAscension__lte=asc).order_by('-maxAscension').first()
            result['MAG_%s' % mag] = {'url': CHARTS_URL + chart.file_name,
                                      'max_asc': chart.maxAscension,
                                      'min_asc': chart.minAscension,
                                      'max_dec': chart.maxDeclination,
                                      'min_dec': chart.minDeclination,
                                      'max_mag': chart.magnitudo
                                      }
    k, v = RESPONSES.items()[0]
    return Response({'code': k, 'message': v, 'result': result})
