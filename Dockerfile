# Используем базовый образ Python
FROM python:3

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости в контейнер
COPY ./requirements.txt /app/

# Устанавливаем зависимости
RUN pip install -r /app/requirements.txt

# Копируем код приложения в контейнер
COPY . .