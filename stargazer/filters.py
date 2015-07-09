__author__ = 'root'
import django_filters
from .models import StellarObject
class StellarListFilter(django_filters.FilterSet):
    min_mag = django_filters.NumberFilter(name='magnitudo', lookup_type='gte')
    max_mag = django_filters.NumberFilter(name='magnitudo', lookup_type='lte')
    class Meta:
        model = StellarObject
        fields = ['max_mag', 'min_mag']