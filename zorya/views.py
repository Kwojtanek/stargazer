# -*- coding=utf-8 -*-

from django.shortcuts import render_to_response
from rest_framework.pagination import PageNumberPagination

from .models import StellarObject, BugTracker, ContactApplet, ObjectPhotos
from .appviews.mapviews import mapapistatic
from django.views.generic import ListView
from .appviews.similarviews import SimilarViewStatic


#STRONA 404 jest obsługiwana przez angular routes
#Popular Crawlers userAgents list

# Paginatory
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100

# Strona glowna
def MainView(request):
    """
    Main view function that checks if request is made by bot, if so, it will provide static version of page
    changed to middleware!
    :param request:
    :return:
    """
    return render_to_response(
        'Search.html')

class ImgList(ListView):
    model = ObjectPhotos
    queryset = ObjectPhotos.objects.all()
    context_object_name = 'photo'
    paginate_by = 50


