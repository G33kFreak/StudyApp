from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminUserOrReadOnly
from .models import *
from .serializers import *

class ClassView(viewsets.ModelViewSet):
    queryset = ClassModel.objects.all()
    serializer_class = ClassesSerializer
    #permission_classes = [IsAuthenticated]

class HomeworkView(viewsets.ModelViewSet):
    queryset = HomeworkModel.objects.all()
    serializer_class = HomeworkSerializer
    #permission_classes = IsAdminUserOrReadOnly

