__author__ = 'kuba'
from django.conf.urls import url, patterns
from django.views.generic import TemplateView
from .views import MainView, StellarViewAPI, SearchAPI, SingleView

from .views import ConstellationsViewDetailAPI, ConstellationsViewAPI, SingleConstellationViewAPI
from .views import CataloguesViewAPI, CataloguesDetailViewAPI, SingleCatalogueViewAPI

urlpatterns = patterns('',
    url(r'^browse/$', MainView, name='MainUrl'),
    url(r'^$', TemplateView.as_view(template_name="stargazer/Search.html"), name='SearchUrl'),
    url(r'^searchAPI$', SearchAPI.as_view(), name='SearchApiUrl'),



# <----------------Endpointy api.-------------------->
    url(r'^StellarlistAPI$', StellarViewAPI.as_view(), name='ngclistUrl'),
    url(r'^(?P<pk>[0-9_-]+)$', SingleView.as_view(), name='SingleUrl'),

    url(r'^catalogueAPI/(?P<name>[a-zA-Z0-9_-]+)$', SingleCatalogueViewAPI.as_view(), name='SingleCatalogueUrl'),
    url(r'^cataloguesAPI$', CataloguesViewAPI.as_view(), name='CataloguesUrl'),
    url(r'^cataloguesAPI/(?P<name>[a-zA-Z0-9_-]+)$', CataloguesDetailViewAPI.as_view(),name='CatalougesDetailUrl'),

    url(r'^constellationAPI/(?P<abbreviation>[a-zA-Z_-]+)$', SingleConstellationViewAPI.as_view(), name='SingleConstellationUrl'),
    url(r'^constellationsAPI$', ConstellationsViewAPI.as_view(), name='ConstellationsUrl'),
    url(r'^constellationsAPI/(?P<abbreviation>[a-zA-Z_-]+)$', ConstellationsViewDetailAPI.as_view(), name='ConstellationsDetailUrl'),

)