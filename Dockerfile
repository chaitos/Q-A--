FROM python:3.12-slim

WORKDIR /app/QAService

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Копируем проект целиком в /app/QAService
COPY . .

# Собираем статику
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "QAService.wsgi:application", "--bind", "0.0.0.0:8000"]
