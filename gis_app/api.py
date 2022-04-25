from rest_framework import routers
from .viewsets import ClinicViewSet

router = routers.DefaultRouter()
router.register(r"clinics", ClinicViewSet)

urlpatterns = router.urls

