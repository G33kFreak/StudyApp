from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

def image_folder(instanse, filename):
    filename = instanse.slug + '.' + filename.split('.')[1]
    return '{0}/{1}'.format(instanse.slug, filename)


class ClassModel(models.Model):
    name = models.CharField(max_length=50)
    instructor = models.CharField(max_length=50)
    toDo = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
    
