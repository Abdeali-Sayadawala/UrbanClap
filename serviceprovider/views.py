from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import *

# Create your views here.
@api_view(['GET', 'POST'])
def spregister(request):
    if request.method == 'GET':
        listdata = Serviceprovider.objects.all()
        serializer = SPSerializer(listdata)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SPSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
