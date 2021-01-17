from django.db import models
from django.contrib.auth.models import UserManager
# Create your models here.


class subject(models.Model):
    course_code=models.IntegerField(null=False,default=0)
    course_title=models.CharField(max_length=50,null=False,default="")
    course_description=models.CharField(max_length=200,null=False,default="")
    
class students(models.Model):
   
    review=models.CharField(max_length=700,default="")
    rating=models.IntegerField(default=0)
    credit_hours=models.IntegerField(default=0)
class instructor(models.Model):
    instructor_name=models.CharField(max_length=30, null=False)
    instructor_bio=models.CharField(max_length=1200, null=False)
    instructor_rate=models.IntegerField()
    review=models.CharField(max_length=700)
    subject=models.CharField(max_length=100)
    


