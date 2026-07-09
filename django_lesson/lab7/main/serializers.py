from rest_framework import serializers
from .models import Good

class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ('name', 'amount', 'price')

