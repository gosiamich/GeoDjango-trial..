
from django.views.generic.base import TemplateView



class ClinicMapView(TemplateView):
    template_name = "gis_app/map.html"
