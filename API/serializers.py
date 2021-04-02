from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Hospital, DocumentRegistration

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'], first_name= validated_data['first_name'], last_name= validated_data['last_name'])
        return user

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class DocumentRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentRegistration
        fields = '__all__'