# coding=utf-8
__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
from django.db.models import Count
from zorya.models import StellarObject
from zorya.serializer import StellarObjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def SimilarViewAPI(request):
    """
    This api searches for simialar objects in StellarObjects query acording to sended params via GET
    :param request: mm
    :return:
    """
    #Checks if any param was send
    if ('type' in request.GET and request.GET['type'] or
        'constellation' in request.GET and request.GET['constellation'] or
        'catalogue' in request.GET and request.GET['catalogue'] ) and \
            'pk' in request.GET and request.GET['pk']:
        #Excludes from query objects with null magnitudo, same pks, includes only object with photo
        #Ordering by releted filds produces duplicates and .distinct() doesn't seams to work so it annotates count of photos
        stellarquery = StellarObject.objects.annotate(num_p=Count('photos')).exclude(magnitudo__isnull=True,pk=request.GET['pk'],num_p=0).order_by('-num_p')
        returnedquery = {}
        #Goes through GET params and maps them corectly to queryset
        for k,v in (request.GET).items():
            if k == 'type':
                serializer = StellarObjectSerializer(stellarquery.filter(type_shortcut=v)[:8],many=True, context={'request': request})
                returnedquery[k] =  serializer.data
            if k == 'constellation':
                serializer = StellarObjectSerializer(stellarquery.filter(constelation__abbreviation=v)[:8],many=True, context={'request': request})
                returnedquery[k] = serializer.data
            if k == 'catalogue':
                serializer = StellarObjectSerializer(stellarquery.filter(catalogues__object_catalogue__name=v)[:8],many=True, context={'request': request})
                returnedquery[k] = serializer.data

        return Response(status=status.HTTP_200_OK,data=returnedquery)
    else:
        return Response(status.HTTP_400_BAD_REQUEST)



def SimilarViewStatic(**kwargs):
    if ('type' in kwargs or 'constellation' in kwargs or 'catalogue' in kwargs) and 'pk' in kwargs:
        stellarquery = StellarObject.objects.annotate(num_p=Count('photos')).exclude(magnitudo__isnull=True,pk=kwargs['pk'],num_p=0).order_by('-num_p')
        returnedquery = {}
        #Goes through GET params and maps them corectly to queryset
        for k,v in (kwargs).items():
            if k == 'type':
                returnedquery[k] =  stellarquery.filter(type_shortcut=v)[:8]
            if k == 'constellation':
                returnedquery[k] =  stellarquery.filter(constelation=v)[:8]
                print returnedquery[k]
            if k == 'catalogue':
                returnedquery[k] =  stellarquery.filter(catalogues__object_catalogue__name=v)[:8]


        return returnedquery
    else:
        return False
