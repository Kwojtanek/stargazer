__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
import urlparse
import string
from django.shortcuts import render_to_response
from zorya.models import StellarObject
from zorya.appviews.mapviews import mapapistatic
from zorya.appviews.similarviews import SimilarViewStatic
#crawlers list
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

class CrawlerMiddleware(object):
    def process_request(self,request):
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
        else:
            return None