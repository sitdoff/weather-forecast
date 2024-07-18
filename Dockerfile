FROM python:3.12-slim-bookworm
LABEL creator="Roman Ivanov"
LABEL email="sitdoff@gmail.com"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.6.1
WORKDIR /code
COPY entrypoint.sh .env requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt && chmod +x /code/entrypoint.sh
COPY ./weather_application /code/
ENTRYPOINT [ "./entrypoint.sh"]
