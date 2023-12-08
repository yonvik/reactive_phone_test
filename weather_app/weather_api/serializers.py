from rest_framework import serializers
from .models import Weather

class WeatherSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    class Meta:
        model = Weather
        
        fields = (
                'city', 
                'temperature',
                'humidity',
                'pk')

class SaveWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        
        fields = (
                'city', 
                'temperature',
                'humidity')
