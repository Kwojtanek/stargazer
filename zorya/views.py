# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import StellarObject
from django.db.models import Q
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from .filters import StellarListFilter
from .models import StellarObject, Catalogues
from .serializer import StellarObjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



#TODO napisz stronę 404 Not Found
#TODO Mixins
# Paginatory
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 500

# Strona glowna
def MainView(request):
    return render_to_response(
        'Browse.html',
        {'Catalogues': Catalogues.objects.all()}, RequestContext(request))

@api_view(['POST','GET'])
def UpdateAPI(request, pk):
    if 'sk' in request.GET and request.GET['sk'] == 'tajnykod0123':
        serializer = StellarObjectSerializer(StellarObject.objects.get(pk=pk), data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status.HTTP_401_UNAUTHORIZED)




