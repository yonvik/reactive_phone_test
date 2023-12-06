from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from weather_api.models import Weather, City


class WeatherListCreateViewTest(APITestCase):
    def setUp(self):
        self.city = City.objects.create(name='London')
        self.weather = Weather.objects.create(city=self.city, temperature=20, humidity=70)

    def test_get_weather_list(self):
        url = reverse('weather-list-create')
        user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_post_existing_city(self):
        url = reverse('weather-list-create')
        data = {'city': 'London'}
        user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=user)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['temperature'], 20)

    def test_post_new_city(self):
        url = reverse('weather-list-create')
        data = {'city': 'New York'}
        user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=user)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Weather.objects.filter(city__name='New York').exists())


class WeatherRetrieveUpdateDestroyViewTest(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=user)
        self.city = City.objects.create(name='Paris')
        self.weather = Weather.objects.create(city=self.city, temperature=25, humidity=80)

    def test_retrieve_weather(self):
        url = reverse('weather-retrieve-update-destroy', kwargs={'pk': self.weather.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['temperature'], 25)

    def test_delete_weather(self):
        url = reverse('weather-retrieve-update-destroy', kwargs={'pk': self.weather.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Weather.objects.filter(pk=self.weather.pk).exists())
