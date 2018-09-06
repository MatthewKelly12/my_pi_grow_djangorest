from django.shortcuts import render
from rest_framework import viewsets
from api.models import Condition
from api.serializers import ConditionSerializer

class ConditionView(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer