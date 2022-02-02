from django.db import models

# Create your models here.

class prem(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    branch=models.CharField(max_length=20)
    phno=models.IntegerField()
    adhar=models.IntegerField()
    Email=models.EmailField()
    pan=models.IntegerField()
    address=models.CharField(max_length=50)