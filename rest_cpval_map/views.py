from django.http import response
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Propiedad, Area
from .serializers import AreaSerializer, PropiedadSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_propiedades(request):
    # Lista todas las propiedades

    if request.method == 'GET':
        propiedad = Propiedad.objects.all()
        serializer = PropiedadSerializer(propiedad,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PropiedadSerializer(data = data)
        
        if serializer.is_valid():
            serializer.save()
            return response(serializer,data, status=status.HTTP_201_CREATED)
        else:
            return response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_propiedad(request,id):
	try:
		propiedad = Propiedad.objects.get(id = id)

	except Propiedad.DoesNotExist:

		return Response(status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = PropiedadSerializer(propiedad)
		return Response(serializer.data)

	if request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = PropiedadSerializer(propiedad,data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		propiedad.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)