from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Clinic


@admin.register(Clinic)
class ClinicAdmin(OSMGeoAdmin):
    list_display = ("name", "location")


