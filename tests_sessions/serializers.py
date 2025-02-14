from rest_framework import serializers
from .models import TestSession

class TestSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSession
        fields = '__all__'
