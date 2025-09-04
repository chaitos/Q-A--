FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn whitenoise


COPY . .


ENV DJANGO_SECRET_KEY="dummy"
ENV DJANGO_DEBUG="False"
ENV DJANGO_ALLOWED_HOSTS="*"


RUN mkdir -p /app/staticfiles
RUN python manage.py collectstatic --noinput --verbosity 3

EXPOSE 8000

CMD ["gunicorn", "QAService.wsgi:application", "--bind", "0.0.0.0:8000"]
