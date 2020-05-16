from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ClassModel
from .serializers import ClassesSerializer

class ClassView(viewsets.ModelViewSet):
    queryset = ClassModel.objects.all()
    serializer_class = ClassesSerializer
    #permission_classes = [IsAuthenticated]
