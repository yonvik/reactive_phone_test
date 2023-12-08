from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from adrf.views import APIView
from .models import City, Weather
from .serializers import WeatherSerializer, SaveWeatherSerializer
from .weather_api import get_weather_data
from asgiref.sync import sync_to_async, async_to_sync
import httpx

class WeatherListCreateView(APIView):
    def get_weather(self):
        return Weather.objects.all()
    
    def serialize(self, serializer):
        return serializer.data
    
    def get_city(self, city_name):
        return City.objects.get_or_create(name=city_name)
    
    async def get(self, request):
        weather = await sync_to_async(self.get_weather)()
        serializer = WeatherSerializer(weather, many=True)
        data = await sync_to_async(self.serialize)(serializer=serializer)
        return Response(data)
    
    async def post(self, request):
        city_name = request.data['city']
        city, created = await sync_to_async(self.get_city)(city_name)
        temperature, humidity = await get_weather_data(city)
        
        try:
            weather = await sync_to_async(Weather.objects.get)(city=city)
            serializer = WeatherSerializer(weather)
            data = await sync_to_async(self.serialize)(serializer=serializer)
            return Response(data)
        except Weather.DoesNotExist:
            weather_data = {'city': city.pk, 'temperature': temperature, 'humidity': humidity}
            serializer = SaveWeatherSerializer(data=weather_data)
            await sync_to_async(serializer.is_valid)(raise_exception=True)
            await sync_to_async(serializer.save)()
            data = await sync_to_async(self.serialize)(serializer=serializer)
            return Response(data)

class WeatherRetrieveUpdateDestroyView(APIView):
    def get_city(self, city_name):
        return City.objects.get_or_create(name=city_name)

    def serialize(self, serializer):
        return serializer.data
    
    def get_weather(self, pk):
        return get_object_or_404(Weather, pk=pk)
    
    async def get(self, request, pk):
        weather = await sync_to_async(self.get_weather)(pk)
        serializer = WeatherSerializer(weather)
        data = await sync_to_async(self.serialize)(serializer=serializer)
        return Response(data)
    
    async def put(self, request, pk):
        weather = await sync_to_async(self.get_weather)(pk)
        city = request.data['city']
        temperature, humidity = await get_weather_data(city)
        city, created = await sync_to_async(self.get_city)(city)
        
        weather_data = {
            'city': city.pk,
            'temperature': temperature,
            'humidity': humidity
        }
        serializer = SaveWeatherSerializer(weather, data=weather_data)
        await sync_to_async(serializer.is_valid)(raise_exception=True)
        await sync_to_async(serializer.save)()
        data = await sync_to_async(self.serialize)(serializer=serializer)
        return Response(data)
    
    async def delete(self, request, pk):
        weather = await sync_to_async(self.get_weather)(pk)
        await sync_to_async(weather.delete)()
        return Response(status=204)
