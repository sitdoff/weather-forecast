# Приложение для прогноза погоды

## О приложении

### Общая информация

Данное веб-приложение позволяет пользователям быстро и удобно получать прогноз погоды для любого города в мире. Приложение разработано с целью предоставить актуальную информацию о погодных условиях, что позволяет пользователям планировать свои дела, путешествия и ежедневные активности.

### Дополнительно

-   Написаны тесты для ключевых функций
-   Написан Dockerfile для контейнеризации
-   Реализовано сохранение города, для которого был запрошен предыдущий прогноз
-   Реализовано сохранение истории запросов

### Доступные страницы

-   /history/ - статистика запросов в формате json
-   /auth/register/ - регистрация пользователя
-   /auth/login/ - авторизация пользователя

### Использованные технологии

-   Python 3.12
-   Django 5.0 и Django REST Framework 3.15
-   база данных - sqlite
-   библиотека geopy
-   Docker для контейнеризации
-   Данные прогноза погоды предоставлены https://open-meteo.com/

### Основные функции

1. Поиск города:

-   Пользователь вводит название города в поисковую строку.
-   Приложени по введеному названию получает координаты города.

2. Отображение прогноза погоды:

-   После ввода названия города и подтверждения поиска, пользователю отображается текущий прогноз погоды для выбранного города в виде таблицы разделенной по часам.
-   Прогноз включает:
    -   Температуру в градусах Цельсия.
    -   Влажность воздуха.
    -   Скорость ветра.
    -   Количество осадков.

3. Сбор статистики запросов

-   Приложение предоставляет доcтуп к данным в каких городах запрашивался прогноз погоды.

## Как запустить

При первом запуске приложения будет создана база данных и применены миграции. Так же будут загружены данные для демонстрациии.
Будут доступны пользователи:

-   Суперпользователь

```
login: admin_demo
password: admin_demo
```

-   Обычный пользователь

```
login: user
password: user_password
```

### Запуск с использованием Docker

1. Для запуска необходимо склонировать репозиторий.

```bash
git clone https://github.com/sitdoff/weather-forecast.git
```

2. Перейти в папку проекта и запустить процесс сборки контейнера.

```bash
docker build --tag=sitdoff/weather .
```

3. После окончания сборки, зпустить контейнер с пробросом необходимых портов. Приложение будет доступно по адресу http://localhost:8000

```bash
docker run -p 8000:8000 --name=Weather sitdoff/weather
```

### Запуск без контейнера

1. Для запуска необходимо склонировать репозиторий.

```bash
git clone https://github.com/sitdoff/weather-forecast.git
```

2. Перейти в папку проекта и выполнить команды. Приложение будет доступно по адресу http://localhost:8000

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python weather_application/manage.py makemigrations
python weather_application/manage.py migrate
python weather_application/manage.py loaddata weather_application/demo_data.json
python weather_application/manage.py runserver
```
