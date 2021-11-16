from django.contrib.gis.db.models import fields
from rest_framework import serializers
from core.models import Propiedad



class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad
        fields = '__all__'