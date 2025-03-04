from django.db import models

class Weatherdetails(models.Model):
    city=models.CharField(max_length=100)
    temperature=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    humidity=models.CharField(max_length=100)
    pressure=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    sunrise=models.CharField(max_length=100)
    sunset=models.CharField(max_length=100)
    windspeed=models.CharField(max_length=100)

    def __str__(self):
        return self.city

