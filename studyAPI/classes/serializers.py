from rest_framework import serializers
from .models import ClassModel

class ClassesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassModel
        fields = ['id', 'name', 'instructor', 'toDo']
