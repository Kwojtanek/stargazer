__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
from rest_framework import viewsets

from zorya.models import ReletedType
from zorya.serializer import ReletedTypeSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = ReletedType.objects.all()
    serializer_class = ReletedTypeSerializer
    lookup_field = 'nametype'