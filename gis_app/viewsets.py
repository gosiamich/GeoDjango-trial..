from rest_framework import viewsets
from rest_framework_gis import filters

from .models import Clinic
from .serializers import ClinicSerializer


class ClinicViewSet(viewsets.ReadOnlyModelViewSet):
    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

