from django.shortcuts import render
from rest_framework import viewsets
from api.models import Category
from api.serializers import CategorySerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer