from rest_framework import serializers
from api.models import Type

class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'url', 'name')