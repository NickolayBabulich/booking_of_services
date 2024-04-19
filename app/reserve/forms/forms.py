from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from app.models import Services


class ReserveForm(FlaskForm):
    service = SelectField('Услуга:', coerce=int,
                          render_kw={"class": "form-control"})
    client_name = StringField('Имя клиента:',
                              render_kw={"class": "form-control"})
    phone = StringField('Номер клиента:',
                        render_kw={"class": "form-control", "type": "phone"})

    submit = SubmitField('Сохранить', render_kw={"class": "btn btn-success"})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service.choices = [(s.id, s.title) for s in Services.query.all()]
