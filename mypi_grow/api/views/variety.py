from django.shortcuts import render
from rest_framework import viewsets
from api.models import Variety
from api.serializers import VarietySerializer

class VarietyView(viewsets.ModelViewSet):
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer
