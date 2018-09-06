from rest_framework import serializers
from api.models import Condition

class ConditionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Condition
        fields = ('id', 'url', 'temperature', 'humidity', 'pH', 'variety', 'type')