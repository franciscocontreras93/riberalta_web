from unicodedata import name
from django.urls import path, re_path

from components. views import (
MapView,
MapViewInspect,
Form,
FormTest,
forms_wizard_view,
saveDatosTerreno,
) 


app_name = 'components'

urlpatterns = [
    
    # path(r"forms/",view = Form,name="forms.terreno"),
    path(r"forms/save/titular",view = saveDatosTerreno,name="forms.save.titular"),
    path("forms/wizard",view = FormTest,name="forms.wizard"),
    path("maps/",view = MapView,name="maps.leaflet"),
    path(r"maps/<str:cod>", view=MapViewInspect,name='maps.leaflet')
]
