from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from Pareto import settings
class instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    instructor_name=models.CharField(max_length=50,default="",null=False)
    instructor_bio=models.CharField(max_length=1200, default="",null=False)
    def __str__(self):
        return self.instructor_name
class subject(models.Model):
    COURSES = (
        ('ENGLISH', 'ENGLISH'),
        ('MATH', 'MATH'),
        ('PYTHON', 'PYTHON'),
    )
    instructor_name=models.OneToOneField(instructor,on_delete=models.CASCADE,null=True)
    Course_name = models.CharField(max_length=50,default="SELECT COURSE", choices=COURSES)
    subject_desc=models.CharField(max_length=1200,default="",null=False)  
class instructor_rate(models.Model):
    instructor_id=models.OneToOneField(instructor,on_delete=models.CASCADE,primary_key=True,unique=True)
    rate=models.IntegerField()
class student(models.Model):
    student=models.OneToOneField(User,on_delete=models.CASCADE,null=True) 
    student_name=models.CharField(max_length=50,default="",null=False)
    student_bio=models.CharField(max_length=200,null=True)
    lecture_taken=models.IntegerField()
    def __str__(self):
        return self.student_name
class rating(models.Model):
    user_id=models.OneToOneField(User,on_delete=models.CASCADE)
    review=models.CharField(default="",max_length=100)
    rating=models.IntegerField()