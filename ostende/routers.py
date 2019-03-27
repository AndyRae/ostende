from rest_framework import routers
from core.viewsets import ScreeningViewSet


router = routers.DefaultRouter()
router.register(r'screening', ScreeningViewSet)
