from rest_framework import serializers
from .models import *

class ClassesSerializer(serializers.ModelSerializer):

    homework = serializers.StringRelatedField(many=True)

    class Meta:
        model = ClassModel
        fields = ['id', 'name', 'instructor_name', 'homework']

class HomeworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = HomeworkModel
        fields = '__all__'

