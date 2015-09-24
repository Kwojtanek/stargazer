# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .filters import StellarListFilter
from .models import StellarObject, Catalogues
from .serializer import StellarObjectSerializer


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
        'Browse.html',
        {'Catalogues': Catalogues.objects.all()}, RequestContext(request))
