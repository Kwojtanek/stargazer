# -*- coding=utf-8 -*-
import urlparse
import string
import json

from django.shortcuts import render_to_response
from rest_framework.pagination import PageNumberPagination
from zorya.models import StellarObject, BugTracker, ContactApplet, ObjectPhotos
from zorya.serializer import StellarObjectSerializer, BugTrackerSerializer, ContactAppletSerializer, PhotoPutSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import StellarObject, BugTracker, ContactApplet, ObjectPhotos
from .serializer import StellarObjectSerializer2, BugTrackerSerializer, ContactAppletSerializer
from .appviews.mapviews import mapapistatic
from django.views.generic import ListView
from django.core import serializers
from .appviews.similarviews import SimilarViewStatic


#STRONA 404 jest obsługiwana przez angular routes
#Popular Crawlers userAgents list
BotsUserAgents = [
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Googlebot/2.1 (+http://www.googlebot.com/bot.html)',
    'Googlebot/2.1 (+http://www.google.com/bot.html)',
    'Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html)',
    'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)',
    'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'Mozilla/5.0 (compatible; bingbot/2.0 +http://www.bing.com/bingbot.htm)',
    'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
    'Mediapartners-Google',
    'Baiduspider',
    'Baiduspider+(+http://www.baidu.com/search/spider_jp.html)',
    'Baiduspider+(+http://www.baidu.com/search/spider.htm)',
    'BaiDuSpider',
    'iaskspider/2.0(+http://iask.com/help/help_index.html)',
    'iaskspider']

# Paginatory
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 500

# Strona glowna
def MainView(request):
    """
    Main view function that checks if request is made by bot, if so, it will provide static version of page
    :param request:
    :return:
    """
    for bot in BotsUserAgents:
        if request.META['HTTP_USER_AGENT'] == bot:
            urlpath =string.split(urlparse.urlsplit(request.path).path,'/')
            if urlpath[-2] == 'object':
                MainObject = StellarObject.objects.get(pk=urlpath[-1])
                return render_to_response('CrawlersTemplate/SingleView.html',
                                          {'MainObject':MainObject,
                                           'charts':mapapistatic(MainObject.rightAsc,
                                                                 MainObject.declination,
                                                                 MainObject.magnitudo),

                                           'similar': SimilarViewStatic(**{'type':MainObject.type_shortcut,
                                                                         'constellation': MainObject.constelation,
                                                                        'catalogue': MainObject.catalogues.first().object_catalogue})
                                           },
                                          )

    return render_to_response(
        'Search.html')
class ImgList(ListView):
    model = ObjectPhotos
    queryset = ObjectPhotos.objects.all()
    context_object_name = 'photo'
    paginate_by = 50


