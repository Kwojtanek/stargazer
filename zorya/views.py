# -*- coding=utf-8 -*-
import urlparse
import string

from django.shortcuts import render_to_response
from rest_framework.pagination import PageNumberPagination


from .models import StellarObject, BugTracker, ContactApplet, ObjectPhotos
from .serializer import StellarObjectSerializer, BugTrackerSerializer, ContactAppletSerializer
from .appviews.mapviews import mapapistatic
from django.views.generic import ListView

#TODO napisz stronę 404 Not Found
#TODO Mixins
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
    for bot in BotsUserAgents:
        if request.META['HTTP_USER_AGENT'] == bot:
            urlpath =string.split(urlparse.urlsplit(request.path).path,'/')
            if urlpath[-2] == 'object':
                MainObject = StellarObject.objects.get(pk=urlpath[-1])
                return render_to_response('CrawlersTemplate/SingleView.html',
                                          {'MainObject':MainObject,
                                           'charts':mapapistatic(MainObject.rightAsc,
                                                                 MainObject.declination,
                                                                 MainObject.magnitudo)
                                           }
                                          )

    return render_to_response(
        'Search.html')
class ImgList(ListView):
    model = ObjectPhotos
    queryset = ObjectPhotos.objects.all()
    context_object_name = 'photo'
    paginate_by = 50