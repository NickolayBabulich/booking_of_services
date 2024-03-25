# Booking of services (Система бронирования услуг)

Проект по предоставлению возможности бронирования/онлайн-запись на услуги для клиента с одной стороны и для поставщика услуги создавать такую возможность для клиента с другой


## Технологии:

[![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/) [![Flask](https://img.shields.io/badge/-Flask-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/2.1.x/) [![HTML](https://img.shields.io/badge/-HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS](https://img.shields.io/badge/-CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS) [![Bootstrap](https://img.shields.io/badge/-Bootstrap-563D7C?style=flat&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

## Описание:
#### Что реализованно:
- Приветственная страница [http://127.0.0.1:5000]( http://127.0.0.1:5000)
- Форма регистрации пользователя [http://127.0.0.1:5000/registration]( http://127.0.0.1:5000/registration)
- Форма аутентификации [http://127.0.0.1:5000/login]( http://127.0.0.1:5000/login)
- Личный кабинет предпринимателя [http://127.0.0.1:5000/cabinet]( http://127.0.0.1:5000/cabinet)
- Модуль сотрудников [http://127.0.0.1:5000/cabinet/employees]( http://127.0.0.1:5000/cabinet/employees)

## Установка:
#### Для запуска проекта необходимо:
- Клонировать репозиторий `git clone https://github.com/NickolayBabulich/booking_of_services.git`
- Перейти в папку проекта `cd booking_of_services`
- Установить необходимые зависимости `pip install -r requirements.txt`
- Создать базу данных командой `python create_db.py`
- Запустить тестовый веб-сервер командой `flask --app app run --debug`

## Дополнительно:

- На тестовом сервере сервис доступен по ссылке  [http://127.0.0.1:5000]( http://127.0.0.1:5000)