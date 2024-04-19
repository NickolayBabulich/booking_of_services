from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from enum import Enum

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    phone = db.Column(db.String(12), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class EmployeeStatus(Enum):
    ACTIVE = "Работает"
    INACTIVE = "Не работает"
    VACATION = "Отпуск"


class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    phone = db.Column(db.String(20))
    status = db.Column(db.Enum(EmployeeStatus), default=EmployeeStatus.ACTIVE, nullable=False)
    description = db.Column(db.Text)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def get_status(self):
        return self.status.value

    def __repr__(self):
        return '<Employee {}>'.format(self.name)


class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Integer, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Service {}>'.format(self.title)


class ServiceStatus(Enum):
    OPEN = "Открыта"
    BOOKED = "Забронирована"
    CLOSE = "Закрыта"


class Scheduler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)
    service = db.relationship('Services', backref=db.backref('schedulers', lazy=True))
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    employee = db.relationship('Employees', backref=db.backref('schedulers', lazy=True))
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    client_name = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(120), nullable=True)
    status = db.Column(db.Enum(ServiceStatus), default=ServiceStatus.CLOSE, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def get_time_of_day(self):
        hour = self.time.hour
        if 6 <= hour < 12:
            return 'утро'
        elif 12 <= hour < 18:
            return 'день'
        else:
            return 'вечер'

    def get_status(self):
        return self.status.value

    def __repr__(self):
        return '<Scheduler {}>'.format(self.status)


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250), nullable=False)
    timestamp = db.Column(db.String(250), nullable=False)
    if_read = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return '<Notification {}>'.format(self.description)

    def __str__(self):
        return f'{self.description}'
