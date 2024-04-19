from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DateField, TimeField
from wtforms.validators import DataRequired
from app.models import ServiceStatus, Services, Employees


class SchedulerForm(FlaskForm):
    service = SelectField('Услуга:', coerce=int,
                          render_kw={"class": "form-control"})
    employee = SelectField('Мастер:', coerce=int,
                           render_kw={"class": "form-control"})
    date = DateField('Дата:', validators=[DataRequired()],
                     render_kw={"class": "form-control", "placeholder": "Введите дату"})
    time = TimeField('Время:', format='%H:%M', validators=[DataRequired()],
                     render_kw={"class": "form-control", "placeholder": "Введите время"})
    client_name = StringField('Имя клиента:',
                              render_kw={"class": "form-control"})
    phone = StringField('Номер клиента:',
                        render_kw={"class": "form-control", "type": "phone"})
    status = SelectField('Статус:', choices=[(status.name, status.value) for status in ServiceStatus],
                         render_kw={"class": "form-control"})
    submit = SubmitField('Сохранить', render_kw={"class": "btn btn-success"})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service.choices = [(s.id, s.title) for s in Services.query.all()]
        self.employee.choices = [(employee.id, employee.first_name) for employee in Employees.query.all()]
