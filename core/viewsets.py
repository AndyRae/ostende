from rest_framework import viewsets
from .models import Screening
from datetime import datetime
from .serializers import ScreeningSerializer


class ScreeningViewSet(viewsets.ModelViewSet):
    todaysdate = datetime.now().date()
    queryset = Screening.objects.filter(date__gte=todaysdate).order_by('date')
    serializer_class = ScreeningSerializer
