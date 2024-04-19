# Booking of services (Система бронирования услуг)

Проект по предоставлению возможности бронирования/онлайн-запись на услуги для клиента с одной стороны и для поставщика услуги создавать такую возможность для клиента с другой


## Технологии:

[![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/) [![Flask](https://img.shields.io/badge/-Flask-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/2.1.x/) [![HTML](https://img.shields.io/badge/-HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS](https://img.shields.io/badge/-CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS) [![Bootstrap](https://img.shields.io/badge/-Bootstrap-563D7C?style=flat&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

## Описание:
#### Что реализованно:
- Регистрация и аутентификация:
  - Форма регистрации пользователя
  - Форма аутентификации
- Личный кабинет поставщика услуг:
  - Модуль сотрудников
  - Модуль услуг
  - Модуль расписания записей
  - Уведомления
- Бронирование услуг для клиента:
  - Выбор услуги для бронирования
  - Карточки с описанием свободных слотов на услугу
  - Бронирование услуги

## Установка:
#### Для запуска проекта необходимо:
- Клонировать репозиторий `git clone https://github.com/NickolayBabulich/booking_of_services.git`
- Убедиться в наличие python версии не ниже 3.11
- Перейти в папку проекта `cd booking_of_services`
- Установить необходимые зависимости `pip install -r requirements.txt`
- Создать базу данных командой `python create_db.py` (для демонстрации возможно не выполнять данное действие и использовать демо базу данных, необходимо файл data.demo.db переименовать в data.db)
- Запустить тестовый веб-сервер командой `flask --app app run --debug`