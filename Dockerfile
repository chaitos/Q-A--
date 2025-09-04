FROM python:3.12-slim

# рабочая папка
WORKDIR /app

# зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# код
COPY . .

# рабочая папка проекта
WORKDIR /app/QAService

# собираем статику
RUN python manage.py collectstatic --noinput

# порт
EXPOSE 8000

# запуск через gunicorn
CMD ["gunicorn", "QAService.wsgi:application", "--bind", "0.0.0.0:8000"]
