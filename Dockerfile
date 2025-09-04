FROM python:3.12-slim

# Рабочая директория указывает туда, где manage.py
WORKDIR /app/QAService

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt gunicorn whitenoise

# Копируем проект целиком в /app
COPY . /app

# Переменные окружения для collectstatic
ENV DJANGO_SECRET_KEY="dummy"
ENV DJANGO_DEBUG="False"
ENV DJANGO_ALLOWED_HOSTS="*"

# Собираем статику
RUN mkdir -p /app/staticfiles
RUN python manage.py collectstatic --noinput --verbosity 3

EXPOSE 8000

# Указываем путь к wsgi из корня проекта
CMD ["gunicorn", "QAService.wsgi:application", "--bind", "0.0.0.0:8000"]
