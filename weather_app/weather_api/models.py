from django.db import models

class City(models.Model):
    city = models.CharField(max_length=100)

class Weather(models.Model):
    city = models.OneToOneField(City, on_delete=models.CASCADE, primary_key=False)
    temperature = models.FloatField()
    humidity = models.FloatField()
    