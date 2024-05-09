from rest_framework import serializers
from .models.users_model import Users

class Users_serializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'