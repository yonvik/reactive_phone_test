# Тестовое задание
Асинхронный API сервис который через определенные команды может:
-просматривать данные
-добавлять данные
-изменять данные
-удалять данные о погоде!

>Технологии, используемые на проекте:

>>1. Python ![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python)
>>2. Django ![Django](https://img.shields.io/badge/-Django-0aad48?style=flat-square&logo=Django)
>>3. DjangoRestFramework ![Django Rest Framework](https://img.shields.io/badge/DRF-red?style=flat-square&logo=Django)
>>4. PostgresSQL ![Postgresql](https://img.shields.io/badge/-Postgresql-%232c3e50?style=flat-square&logo=Postgresql)

# Как запустить проект:
Зарегестрироваться на сервисе weatherapi.com и получить API KEY

Клонируйте репозиторий на локальную машину командой:
```
git clone git@github.com:yonvik/reactive_phone_test.git
```

В папку ***weather_app*** расположить .env файл со следующими параметрами:
1. DJANGO_SECRET_KEY=***ВАШ СЕКРЕТНЫЙ КЛЮЧ ПРОЕКТА***
2. API_KEY=***ВАШ СЕКРЕТНЫЙ КЛЮЧ ДЛЯ АПИ ПОГОДЫ***

Установить виртуальное окружение venv
```
python python -m venv env
```

После установки виртуального окружения установить файл с requirements.txt

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:
```
python manage.py migrate
```
Создать суперюзера:
```
python manage.py createsuperuser
```
Запустить проект:
```
python manage.py runserver
```
Далее требуется в Postman ввести данные суперюзера и получить токен.

Без токена будет ошибка авторизации!

## Примеры запросов
POST-запрос .../weather/:
```JSON
{
  "city": "London"
}
```
Ответ (200):
```JSON
{
    "city": "London",
    "temperature": 11.0,
    "humidity": 76.0,
    "pk": 3
}
```

GET-запрос .../weather/:
```JSON
{
  none
}
```
Ответ (200):
```JSON
[
    {
        "city": "New York",
        "temperature": 2.2,
        "humidity": 67.0,
        "pk": 5
    },
    {
        "city": "Moscow",
        "temperature": -14.0,
        "humidity": 85.0,
        "pk": 4
    },
    {
        "city": "London",
        "temperature": 11.0,
        "humidity": 76.0,
        "pk": 3
    }
]
```
