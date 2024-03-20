from app import db, create_app

# Создание базы данных
with create_app().app_context():
    db.create_all()
