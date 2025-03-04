from django.db import models
from django.forms.widgets import NumberInput

# Create your models here.
class registration(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    emailid=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    dateofbirth=models.CharField(max_length=100)
    mobilenumber=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    gender=models.CharField(max_length=50)
    question=models.CharField(max_length=200)
    answer=models.CharField(max_length=200)
    question1=models.CharField(max_length=200)
    answer1=models.CharField(max_length=200)
    question2=models.CharField(max_length=200)
    answer2=models.CharField(max_length=200)

    def __str__(self):
        return self.firstname

class clubdetails(models.Model):
    clubname=models.CharField(max_length=100)
    assignedrole=models.CharField(max_length=100)
    assignedperson=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    teamname=models.CharField(max_length=100)
    role=models.CharField(max_length=100)

    def __str__(self):
        return self.clubname

