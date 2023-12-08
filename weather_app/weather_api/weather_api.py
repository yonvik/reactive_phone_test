import httpx
import os
from dotenv import load_dotenv
load_dotenv()

async def get_weather_data(city):
    API_KEY = os.getenv('API_KEY')
    url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no' 
    async with httpx.AsyncClient() as client: 
        response = await client.get(url) 
        data = response.json()
        temperature = data['current']['temp_c']
        humidity = data['current']['humidity'] 
        return temperature, humidity
