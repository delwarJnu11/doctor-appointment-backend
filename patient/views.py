from django.shortcuts import render
from patient.serializers import PatientSerializers
from rest_framework import viewsets
from patient.models import Patient

# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers