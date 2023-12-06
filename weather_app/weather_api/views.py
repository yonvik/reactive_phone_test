from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import City, Weather
from .serializers import WeatherSerializer, SaveWeatherSerializer
from .weather_api import get_weather_data



class WeatherListCreateView(APIView):
    def get(self, request):
        weather = Weather.objects.all()
        serializer = WeatherSerializer(weather, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        city_name = request.data['city']
        city, created = City.objects.get_or_create(name=city_name)
        
        try:
            weather = Weather.objects.get(city=city)
            serializer = WeatherSerializer(weather)
            return Response(serializer.data)
        except Weather.DoesNotExist:
            temperature, humidity = get_weather_data(city)
            weather_data = {'city': city.pk, 'temperature': temperature, 'humidity': humidity}
            serializer = SaveWeatherSerializer(data=weather_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    

class WeatherRetrieveUpdateDestroyView(APIView):
    def get(self, request, pk):
        weather = get_object_or_404(Weather, pk=pk)
        serializer = WeatherSerializer(weather)
        return Response(serializer.data)

    def put(self, request, pk):
        weather = get_object_or_404(Weather, pk=pk)
        city = request.data['city']
        temperature, humidity = get_weather_data(city)
        weather_data = {'city': city, 'temperature': temperature, 'humidity': humidity}
        serializer = WeatherSerializer(weather, data=weather_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        weather = get_object_or_404(Weather, pk=pk)
        weather.delete()
        return Response(status=204)
