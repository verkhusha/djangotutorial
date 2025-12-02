Django Tutorial Project

Опис лабораторної роботи

Цей проєкт створено для лабораторної роботи з Django.  
Мета роботи:
- Інсталяція Python та Django.
- Створення базового Django-проєкту.
- Ознайомлення з роботою серверу Django та структури проєкту.
- Виконання покрокових завдань за офіційним [tutorial Django](https://docs.djangoproject.com/en/5.2/intro/).

Покрокові завдання (коміти)

1. Commit 1 – tutorial01
   - Інсталяція Django.
   - Створення базового проєкту.
   - Перевірка запуску серверу.

2. Commit 2 – tutorial02
   - Створення першої сторінки.
   - Ознайомлення з маршрутизацією.

3. Commit 3 – tutorial03
   - Робота з моделями.
   - Створення бази даних.
   - Міграції.

4. Commit 4 – tutorial04
   - Створення форм та обробка даних користувача.
   - Використання шаблонів.

5. Commit 5 – tutorial05
   - Налаштування адміністративної панелі.
   - Створення користувачів та груп.

6. Commit 6 – tutorial06
   - Робота з шаблонами та розширенням шаблонів.
   - Маршрутизація та додаткові view.

7. Commit 7 – tutorial07
   - Завершення базового функціоналу.
   - Тестування та виправлення помилок.

8. Commit 8 – tutorial08 (опційно)
   - Використання повторно-застосовуваних додатків.
   - Розширення функціоналу проєкту.

Структура проєкту

djangotutorial/
├── manage.py
├── mysite/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
└── db.sqlite3

git clone https://github.com/verkhusha/djangotutorial.git
cd djangotutorial

python3 -m venv .venv
source .venv/bin/activate

pip install django==5.2

python manage.py runserver

http://127.0.0.1:8000/

Виконавець: Владислав Верхуша
