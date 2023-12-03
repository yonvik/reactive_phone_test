import requests

def get_weather_data(city):
    API_KEY = '6a30a7f9e46a41079cf141918230212'
    url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no'
    response = requests.get(url)
    data = response.json()
    temperature = data['current']['temp_c']
    humidity = data['current']['humidity']
    return temperature, humidity
