from rest_framework import routers
from core.api.views import ScreeningViewSet


router = routers.DefaultRouter()
router.register(r'screening', ScreeningViewSet)
