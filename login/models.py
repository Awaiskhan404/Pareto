from django.db import models

# Create your models here.


class endusers(models.Model):
    first_name=models.CharField(max_length=16,null=False)
    last_name=models.CharField(max_length=16,null=False)
    email=models.EmailField(max_length=50,null=False)
    password=models.CharField(max_length=16,null=False)
