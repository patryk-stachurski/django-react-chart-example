from rest_framework import viewsets, mixins
from rest_framework import permissions
from django_filters import rest_framework as filters

from . import models
from . import serializers


class ProductFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name='date', lookup_expr='gte', required=True)
    end_date = filters.DateFilter(field_name='date', lookup_expr='lte', required=True)


class DayStatsViewset(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = models.DayStats.objects.select_related('datasource', 'campaign')
    serializer_class = serializers.DayStatsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter
