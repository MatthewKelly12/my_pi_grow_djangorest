from rest_framework import serializers
from api.models import Variety

class VarietySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Variety
        fields = ('id', 'url', 'name', 'category')