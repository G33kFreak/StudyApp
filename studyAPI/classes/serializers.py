from rest_framework import serializers
from .models import *

class HomeworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = HomeworkModel
        fields = ['id', 'description', 'deadlineDate', 'deadlineTime', 'isOverdue']

class ClassesSerializer(serializers.ModelSerializer):

    homework = HomeworkSerializer(many=True)

    class Meta:
        model = ClassModel
        fields = ['id', 'name', 'instructor_name', 'homework']


