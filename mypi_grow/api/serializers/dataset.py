from rest_framework import serializers
from api.models import Dataset

class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dataset
        fields = ('id', 'url', 'inside_temperature', 'inside_humidity', 'outside_temperature', 'outside_humidity', 'water_temperature', 'water_pH', 'image', 'grow')