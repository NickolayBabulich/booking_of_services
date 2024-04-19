from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class ServiceForm(FlaskForm):
    title = StringField('Название:', validators=[DataRequired()],
                        render_kw={"class": "form-control", "placeholder": "Введите название"})
    description = TextAreaField('Описание:', render_kw={"class": "form-control", "placeholder": "Введите описание"})
    price = StringField('Цена:', validators=[DataRequired()],
                        render_kw={"class": "form-control", "placeholder": "Введите цену"})
    submit = SubmitField('Сохранить', render_kw={"class": "btn btn-success"})
