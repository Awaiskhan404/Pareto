from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class course(models.Model):
    course_code=models.IntegerField(null=False)
    course_title=models.CharField(max_length=50,null=False,default="")
    course_description=models.CharField(max_length=200,null=False,default="")
    
class students(models.Model):
    course_code=models.ManyToManyField(course)
    review=models.CharField(max_length=700,default="")

class instructor(models.Model):
    pass
