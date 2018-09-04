from django.shortcuts import render
from rest_framework import viewsets
from api.models import Type
from api.serializers import TypeSerializer

class TypeView(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

