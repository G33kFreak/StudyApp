from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from Account.models import User
from datetime import datetime
import pytz

def image_folder(instanse, filename):
    filename = instanse.slug + '.' + filename.split('.')[1]
    return '{0}/{1}'.format(instanse.slug, filename)
    

class ClassModel(models.Model):
    name = models.CharField(max_length=50)
    instructor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name

    @property
    def instructor_name(self):
        return self.instructor.first_name + ' ' + self.instructor.last_name
    
class HomeworkModel(models.Model):
    description = models.CharField(max_length=200)
    Class = models.ForeignKey(ClassModel, null=True, on_delete=models.SET_NULL, related_name='homework')
    deadline = models.DateTimeField(auto_now_add=False)

    @property
    def isOverdue(self):
        return pytz.utc.localize(datetime.now()) > self.deadline

    @property
    def deadlineDate(self):
        return str(self.deadline.strftime('%d-%m-%Y %H:%M')).split(' ')[0]

    @property
    def deadlineTime(self):
        return str(self.deadline.strftime('%d-%m-%Y %H:%M')).split(' ')[1]

    def __str__(self):
        return self.description
    
