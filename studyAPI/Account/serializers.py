from rest_framework import serializers
from django.contrib.auth.models import User


class userProfileSerializer(serializers.ModelSerializer):
    User = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = User
        fields = '__all__'