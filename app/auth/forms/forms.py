from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField('Логин:', validators=[DataRequired()],
                           render_kw={"class": "form-control", "placeholder": "Введите логин"})
    password = PasswordField('Пароль:', validators=[DataRequired()],
                             render_kw={"class": "form-control", "placeholder": "Введите пароль"})
    submit = SubmitField('Войти', render_kw={'class': "btn btn-primary w-100"})


class RegistrationForm(FlaskForm):
    username = StringField('Имя:', validators=[DataRequired()],
                           render_kw={"class": "form-control", "placeholder": "Введите имя"})
    email = EmailField('Электронная почта:', validators=[Email()],
                       render_kw={"class": "form-control", "placeholder": "Введите электронную почту"})
    phone = StringField('Номер телефона:', validators=[DataRequired()],
                        render_kw={"class": "form-control", "placeholder": "Введите номер телефона"})
    password = PasswordField('Пароль:', validators=[DataRequired()],
                             render_kw={"class": "form-control", "placeholder": "Введите пароль"})
    password2 = PasswordField('Подтверждение пароля:', validators=[DataRequired()],
                              render_kw={"class": "form-control", "placeholder": "Подтвердите пароль"})
    submit = SubmitField('Зарегистрироваться', render_kw={'class': "btn btn-primary w-100"})
