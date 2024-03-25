from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

from app.models import EmployeeStatus


class EmployeeForm(FlaskForm):
    first_name = StringField('Имя:', validators=[DataRequired()],
                             render_kw={"class": "form-control", "placeholder": "Введите имя сотрудника"})
    last_name = StringField('Фамилия:', validators=[DataRequired()],
                            render_kw={"class": "form-control", "placeholder": "Введите имя сотрудника"})
    phone = StringField('Телефон:', validators=[DataRequired()],
                        render_kw={"class": "form-control", "placeholder": "Введите имя сотрудника"})
    status = SelectField('Статус:', choices=[(status.name, status.value) for status in EmployeeStatus],
                         render_kw={"class": "form-control", "placeholder": "Введите имя сотрудника"})
    description = TextAreaField('Описание:', render_kw={"class": "form-control", "placeholder": "Введите описание"})
    submit = SubmitField('Сохранить', render_kw={"class": "btn btn-success"})
