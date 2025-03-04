from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class Register(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    dateofbirth=models.DateField()
    gender=models.CharField(max_length=50)
    emailid=models.EmailField()
    password=models.CharField(max_length=100)
    mobilenumber=models.CharField(max_length=100)
    role=models.CharField(max_length=50)
    securityquestion=models.CharField(max_length=100)
    securityanswer=models.CharField(max_length=100)
    securityquestion1=models.CharField(max_length=100)
    securityanswer1=models.CharField(max_length=100)
    securityquestion2=models.CharField(max_length=100)
    securityanswer2=models.CharField(max_length=100)


    def __str__(self):
        return self.firstname

class Weatherdetails(models.Model):
    city=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    hour=models.CharField(max_length=100)
    temperature=models.CharField(max_length=100)
    description=models.CharField(max_length=100) 
    icon=models.CharField(max_length=100)
    humidity=models.CharField(max_length=100)
    pressure=models.CharField(max_length=100)
    windspeed=models.CharField(max_length=100)

    def __str__(self):
        return self.city
    
        
