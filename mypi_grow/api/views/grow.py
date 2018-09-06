from django.shortcuts import render
from rest_framework import viewsets
from api.models import Grow
from api.serializers import GrowSerializer

class GrowView(viewsets.ModelViewSet):
    queryset = Grow.objects.all()
    serializer_class = GrowSerializer