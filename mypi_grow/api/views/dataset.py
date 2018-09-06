from django.shortcuts import render
from rest_framework import viewsets
from api.models import Dataset
from api.serializers import DatasetSerializer

class DatasetView(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer