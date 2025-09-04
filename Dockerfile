FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . .

WORKDIR /app  # рабочая директория совпадает с BASE_DIR

# создаём папку для collectstatic
RUN mkdir -p /app/staticfiles
RUN chmod -R 777 /app/staticfiles

# собираем статику
RUN python manage.py collectstatic --noinput --verbosity 3

EXPOSE 8000

CMD ["gunicorn", "QAService.wsgi:application", "--bind", "0.0.0.0:8000"]
