from rest_framework import serializers, fields
from .models import *

class HomeworkSerializer(serializers.ModelSerializer):

    deadline = fields.DateTimeField(input_formats=['%d-%m-%Y %H:%M'])

    class Meta:
        model = HomeworkModel
        fields = ['id', 'description', 'deadlineDate', 'deadlineTime', 'isOverdue', 'Class', "deadline"]

class ClassesSerializer(serializers.ModelSerializer):

    homework = HomeworkSerializer(many=True)

    class Meta:
        model = ClassModel
        fields = ['id', 'name', 'instructor_name', 'homework']


