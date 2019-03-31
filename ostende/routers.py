from rest_framework import routers
from core.api.views import ScreeningViewSet, ScreeningAPIView


router = routers.DefaultRouter()
router.register(r'screening', ScreeningViewSet)
