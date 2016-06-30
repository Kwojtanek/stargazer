__author__ = 'kuba'
from django.conf.urls import url, patterns, include
from .appviews.createaupdateviews import UpdateAPI, BugTrackerViewAPI, ContactAppletViewAPI,\
    PhotoCreate,  CreateUpdateAPI, PhotoList
from .appviews.mapviews import mapapi
from .views import ImgList
from .appviews.searchviews import SearchAPI
from .appviews.generics import TypeViewSet

from .appviews.similarviews import SimilarViewAPI
from .appviews.browseviews import StellarViewAPI, SingleView
from .appviews.browseviews import ConstellationsViewDetailAPI, ConstellationsViewAPI, SingleConstellationViewAPI, ConstellationsListViewAPI
from .appviews.browseviews import CataloguesListViewAPI, SingleCatalogueViewAPI
from .appviews.browseviews import TypeViewAPI, CataloguesViewAPI
# <----------------Endpointy api.-------------------->

endpointspatterns = [
    url(r'^StellarlistAPI$', StellarViewAPI.as_view(), name='StellarlistUrl'),
    url(r'^singleAPI/(?P<pk>[0-9_-]+)$', SingleView.as_view(), name='SingleUrl'),
    url(r'^photoList$', ImgList.as_view(template_name='imglist.html')),

    url(r'^catalogueAPI/(?P<name>[a-zA-Z0-9_-]+)$', SingleCatalogueViewAPI.as_view(),
        name='SingleCatalogueUrl'),
    url(r'^cataloguesAPI$', CataloguesViewAPI.as_view(), name='CataloguesUrl'),

    url(r'^constellationAPI/(?P<abbreviation>[a-zA-Z_-]+)$',
        SingleConstellationViewAPI.as_view(),
        name='SingleConstellationUrl'),
    url(r'^constellationsAPI$', ConstellationsListViewAPI.as_view(), name='ConstellationsUrl'),
    url(r'^constellationsAPI/(?P<abbreviation>[a-zA-Z_-]+)$',
        ConstellationsViewDetailAPI.as_view(),
        name='ConstellationsDetailUrl'),

    url(r'^mapAPI$', mapapi),
    url(r'^searchAPI$', SearchAPI.as_view(), name='SearchApiUrl'),

    url(r'^updateAPI/(?P<pk>[0-9_-]+)$', UpdateAPI, name='UpdateUrl'),
    url(r'^createupdateAPI$',CreateUpdateAPI, name='CreateUpdateUrl'),
    url(r'^createphotoAPI$', PhotoCreate, name='PhotoCreateUrl'),

    url(r'^type/$', TypeViewSet.as_view({'get':'list','post':'create'}), name='TypeCreateUrl' ),
    url(ur'^type/(?P<nametype>.*)/$', TypeViewSet.as_view({'get': 'retrieve','put': 'update','patch': 'partial_update','delete': 'destroy'})),

    url(r'^similarAPI$', SimilarViewAPI, name='SimilarUrl'),
    url(r'^bugtrackerAPI$', BugTrackerViewAPI.as_view(), name='BugTrackerUrl'),
    url(r'^contactappletAPI$', ContactAppletViewAPI.as_view(), name='contactappletUrl'),
    url(r'photoAPI', PhotoList.as_view(), name='PhotoListUrl' )
]
explorepatterns = [
    # All 3 explore endpoints
    url(r'^type/(?P<typesc>[a-zA-Z0-9_-]+)$', TypeViewAPI.as_view(), name='TypeListUrl'),
    url(r'^catalogue/(?P<cat>[a-zA-Z0-9_-]+)$', CataloguesViewAPI.as_view(), name='CatalogueListUrl'),
    url(r'^constellation/(?P<abbreviation>[a-zA-Z0-9_-]+)$', ConstellationsViewAPI.as_view(), name='ConstellationListUrl')
]
urlpatterns = [
    url(r'^exploreAPI/',include(explorepatterns)),
    url(r'^endpoint/', include(endpointspatterns)),
]
