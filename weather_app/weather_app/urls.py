from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
]
from weather_api.views import WeatherListCreateView, WeatherRetrieveUpdateDestroyView

urlpatterns = [
    path('weather/', WeatherListCreateView.as_view(), name='weather-list-create'),
    path('weather/<int:pk>/', WeatherRetrieveUpdateDestroyView.as_view(), name='weather-retrieve-update-destroy'),
    path('api-token-auth/', views.obtain_auth_token)
]
