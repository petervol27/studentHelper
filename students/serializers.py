from rest_framework import serializers
from .models import StudentUser  # Custom User model

# Serializer for Custom User Model (StudentUser)
class StudentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser  # Custom user model
        fields = ['id', 'username', 'email', 'age', 'city']
