from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class Weather(models.Model):
    city = models.OneToOneField(City, on_delete=models.CASCADE, primary_key=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    