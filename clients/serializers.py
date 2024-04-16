from rest_framework import serializers
from clients.models import Client

class ClientSerializer(serializers.ModelSerializer):
    """displaying all customers"""
    class Meta:
        model = Client
        fields = '__all__'
    