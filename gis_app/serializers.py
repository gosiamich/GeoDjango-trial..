from rest_framework_gis import serializers

from .models import Clinic


class ClinicSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        fields = ("id", "name")
        geo_field = "location"
        model = Clinic
