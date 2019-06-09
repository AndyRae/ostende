from rest_framework import viewsets, filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Screening
from datetime import datetime, timedelta
from .serializers import ScreeningSerializer
from rest_framework.pagination import PageNumberPagination


class ScreeningViewSet(viewsets.ModelViewSet):
    todaysdate = datetime.now().date()
    queryset = Screening.objects.filter(date__gte=todaysdate).order_by('date', 'start_time')
    serializer_class = ScreeningSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('name', 'film__name', 'venue__name', 'venue__city', 'venue__county', 'season__name', 'date',)
    filterset_fields = ('date',)


class ScreeningDateViewSet(viewsets.ModelViewSet):
    d = timedelta(days=30)
    todaysdate = datetime.now().date()
    targetdate = datetime.now().date() + d
    queryset = Screening.objects.filter(date__gte=todaysdate).filter(date__lte=targetdate).order_by('date', 'start_time')
    serializer_class = ScreeningSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('name', 'film__name', 'venue__name', 'venue__city', 'season__name', 'date',)
    filterset_fields = ('date',)
