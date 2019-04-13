from rest_framework import routers
from core.api.views import ScreeningViewSet, ScreeningDateViewSet


router = routers.DefaultRouter()
router.register(r'screening', ScreeningViewSet)
router.register(r'screeningdate', ScreeningDateViewSet)
