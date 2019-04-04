from rest_framework import viewsets, filters, generics
from core.models import Screening
from datetime import datetime
from .serializers import ScreeningSerializer
from rest_framework.pagination import PageNumberPagination


class ScreeningViewSet(viewsets.ModelViewSet):
    todaysdate = datetime.now().date()
    queryset = Screening.objects.filter(date__gte=todaysdate).order_by('date')
    serializer_class = ScreeningSerializer
    filter_backends = (filters.SearchFilter,)
    # pagination_class = PageNumberPagination
    search_fields = ('name', 'film__name', 'venue__name', 'venue__city', 'season__name',)
