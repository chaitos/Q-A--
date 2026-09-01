# Q&A Service (Stack Overflow Clone)

Сайт, который работает по принципу вопрос-ответ, аналог Stack Overflow. Пользователи могут задавать вопросы, отвечать на них, а также голосовать за лучшие ответы.

##  Технологии

- **Backend:** Django (Python)
- **Database:** SQLite
- **Frontend:** HTML, CSS, Bootstrap 5
- **Прочее:** Используются статические файлы для подключения бекенда к фронту

## Архитектура

MVC (Model-View-Controller)

##  Как запустить локально

Клонируйте репозиторий:
git clone 
https://github.com/your-username/your-repo-name.git
cd your-repo-name
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate для Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
