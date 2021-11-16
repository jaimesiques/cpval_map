from django.contrib.gis.db.models import fields
from rest_framework import serializers
from core.models import Area, Propiedad



class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad
        fields = '__all__'
        
        
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'