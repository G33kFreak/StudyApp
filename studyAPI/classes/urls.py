from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('classes', views.ClassView)
router.register('homework', views.HomeworkView)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls))
]