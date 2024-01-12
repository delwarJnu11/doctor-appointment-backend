from django.shortcuts import render
from service.models import Service
from service.serializers import ServiceSerializer
from rest_framework import viewsets

# Create your views here.
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
