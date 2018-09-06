from rest_framework import serializers
from api.models import Grow

class GrowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grow
        fields = ('id', 'url', 'name', 'start_date', 'end_date', 'description', 'condition', 'user')