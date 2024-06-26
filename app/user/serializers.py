"""
Serializers for the user API View
"""
from django.contrib.auth import get_user_model

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """ORM Serializer for the user object"""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {
            'password': { 'write_only': True, 'min_length': 7 }
        }


    def create(self, validated_data):
        """Creates a newly registered user"""
        return self.Meta.model.objects.create_user(**validated_data)

