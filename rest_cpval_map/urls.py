from django.urls import path
from rest_cpval_map.views import lista_propiedades , detalle_propiedad
from rest_cpval_map.viewslogin import login

urlpatterns = [
    path('lista_propiedades',lista_propiedades,name="lista_propiedades"),
    path('propiedad/<id>',detalle_propiedad,name="detalle_propiedad"),
    path('login',login,name="login")
    
]