#!/bin/bash
# Устанавливаем строгий режим
set -e


# Применение миграций, если это необходимо
python manage.py makemigrations && python manage.py migrate && python manage.py loaddata demo_data.json
python manage.py runserver 0.0.0.0:8000

# Запуск вашего Django приложения
exec "$@"
