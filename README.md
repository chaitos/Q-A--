# QAService — Q&A Service (Stack Overflow Clone) ❓

Сайт вопросов и ответов, аналог Stack Overflow. Пользователи регистрируются, задают вопросы, отвечают на них (в том числе на другие ответы) и ставят лайки.

## Возможности

- Регистрация и авторизация
- Вопросы с автогенерацией slug (в том числе из кириллицы)
- Вложенные ответы на ответы (self-referencing FK)
- Лайки на вопросы и ответы
- Soft delete (`is_active`) вместо физического удаления
- Личный кабинет с историей своих вопросов
- Админ-панель с поиском и фильтрами

## Стек

Python 3, Django 5.2 (Class-Based Views), SQLite, python-slugify, Bootstrap 5, Docker + Gunicorn + WhiteNoise

## Запуск

```bash
git clone https://github.com/chaitos/QAService.git
cd QAService

docker build -t qa-service .
docker run -p 8000:8000 -e DJANGO_SECRET_KEY=any-value-for-local -e DJANGO_DEBUG=True qa-service
```

Сайт откроется на `http://127.0.0.1:8000/`. Миграции применяются автоматически при старте контейнера.

Чтобы зайти в `/admin/`, создайте суперпользователя в отдельном терминале, пока контейнер запущен:

```bash
docker ps                                            # узнать CONTAINER ID
docker exec -it <container_id> python manage.py createsuperuser
```

> Значения `DJANGO_SECRET_KEY`/`DJANGO_DEBUG` выше подходят только для локального просмотра, не для продакшена.

## Возможные улучшения

- [ ] Подсчёт лайков на странице
- [ ] Тесты
- [ ] Поиск и теги для вопросов
- [ ] PostgreSQL вместо SQLite