from rest_framework import viewsets, filters, generics
from core.models import Screening
from datetime import datetime
from .serializers import ScreeningSerializer


class ScreeningViewSet(viewsets.ModelViewSet):
    todaysdate = datetime.now().date()
    queryset = Screening.objects.filter(date__gte=todaysdate).order_by('date')
    serializer_class = ScreeningSerializer


class ScreeningAPIView(generics.ListAPIView):
    serializer_class = ScreeningSerializer

    def get_queryset(self, *args, **kwargs):
        todaysdate = datetime.now().date()
        queryset_list = Screening.objects.filter(date__gte=todaysdate).order_by('date')
        query = self.request.QUERY_PARAMS.get("search", None)
        if query:
            queryset_list = queryset_list.filter(name=query)
        return queryset_list
