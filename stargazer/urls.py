__author__ = 'kuba'
from django.conf.urls import url, patterns
from .views import MainView, NgcViewAPI, SearchView, SingleView

from .views import ConstellationsViewDetailAPI, ConstellationsViewAPI, SingleConstellationViewAPI
from .views import CataloguesViewAPI, CataloguesDetailViewAPI, SingleCatalogueViewAPI

urlpatterns = patterns('',
    url(r'^$', MainView, name='MainUrl'),
    url(r'^search/$', SearchView, name='SearchUrl'),

# <----------------Endpointy api.-------------------->
    url(r'^ngclistAPI$', NgcViewAPI.as_view(), name='ngclistUrl'),
    url(r'^(?P<pk>[0-9_-]+)$', SingleView.as_view(), name='SingleUrl'),

    url(r'^catalogueAPI/(?P<name>[a-zA-Z0-9_-]+)$', SingleCatalogueViewAPI.as_view(), name='SingleCatalogueUrl'),
    url(r'^cataloguesAPI$', CataloguesViewAPI.as_view(), name='CataloguesUrl'),
    url(r'^cataloguesAPI/(?P<name>[a-zA-Z0-9_-]+)$', CataloguesDetailViewAPI.as_view(),name='CatalougesDetailUrl'),

    url(r'^constellationAPI/(?P<abbreviation>[a-zA-Z_-]+)$', SingleConstellationViewAPI.as_view(), name='SingleConstellationUrl'),
    url(r'^constellationsAPI$', ConstellationsViewAPI.as_view(), name='ConstellationsUrl'),
    url(r'^constellationsAPI/(?P<abbreviation>[a-zA-Z_-]+)$', ConstellationsViewDetailAPI.as_view(), name='ConstellationsDetailUrl'),
)