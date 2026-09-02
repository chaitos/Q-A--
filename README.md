# Q&A Service (Stack Overflow Clone) ❓

Сайт вопросов и ответов, аналог Stack Overflow. Пользователи регистрируются, задают вопросы, отвечают на них (в том числе на другие ответы) и ставят лайки.

## Возможности

- Регистрация и авторизация пользователей
- Создание вопросов с автогенерацией уникального slug (в том числе из кириллицы)
- Ответы на вопросы и вложенные ответы на ответы (self-referencing FK)
- Лайки на вопросы и ответы через отдельные модели (`QuestionLike`, `AnswerLike`) — для большей гибкости, чем стандартный `ManyToManyField`
- Soft delete — вопросы и ответы не удаляются физически, а помечаются `is_active=False`
- Личный кабинет со списком своих вопросов
- Пагинация списка вопросов
- Админ-панель с поиском, фильтрами и inline-редактированием статуса

## Стек

- Python 3 / Django 5.2 (Class-Based Views)
- SQLite (БД для разработки)
- python-slugify (корректные slug из кириллицы)
- Bootstrap 5
- Docker + Gunicorn + WhiteNoise — для продакшен-сборки

## Структура проекта

```
QAService/
├── QAService/          # настройки проекта
├── service/             # основное приложение
│   ├── models.py         # Question, Answer, QuestionLike, AnswerLike
│   ├── views.py          # CBV: ListView, DetailView, CreateView
│   ├── forms.py
│   ├── admin.py
│   └── templates/service/
└── templates/base.html
```

## Установка и запуск локально

```bash
git clone https://github.com/chaitos/Q-A--.git
cd Q-A--/QAService

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt

# создать .env на основе .env.example и указать свой SECRET_KEY

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Запуск через Docker

```bash
docker build -t qa-service .
docker run -p 8000:8000 -e DJANGO_SECRET_KEY=your-secret-key qa-service
```

## Модели данных

- **Question** — вопрос: автор, заголовок, содержание, slug, статус активности
- **Answer** — ответ на вопрос или на другой ответ (`parent`)
- **QuestionLike / AnswerLike** — лайки с ограничением уникальности пары (пользователь, объект)

## Возможные улучшения

- [ ] Подсчёт и отображение количества лайков на странице
- [ ] Тесты (`tests.py` сейчас пустой)
- [ ] Поиск и теги для вопросов
- [ ] Кастомная страница 404