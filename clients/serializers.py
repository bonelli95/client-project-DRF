from rest_framework import serializers
from clients.models import Client
from clients.validators import *

class ClientSerializer(serializers.ModelSerializer):
    """displaying all customers"""
    class Meta:
        model = Client
        fields = '__all__'

    def validate(self, data):
        if not valid_tin(data['tin']):
            raise serializers.ValidationError({'tin':"Ensure this field has no more than 13 characters"})
        if not valid_name(data['name']):
            raise serializers.ValidationError({'name':"Please use only letters"})
        if not valid_pin(data['pin']):
            raise serializers.ValidationError({'pin':"Ensure this field has no more than 9 characters"})
        if not valid_cell(data['cell']):
            raise serializers.ValidationError({'cell':"Ensure this field has no more than 14 characters"})
        return data
