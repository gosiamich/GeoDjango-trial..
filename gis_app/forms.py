from django.contrib.gis import forms


class NewEntryForm(forms.Form):
    location_name = forms.CharField(label='Name', max_length=20)
    location = forms.PointField(widget=forms.OSMWidget(
        attrs={
            'map_width': 600,
            'map_height': 400,
            'default_lat': 50.1091,
            'default_lon': 8.6819,
            'default_zoom': 9
        }))
