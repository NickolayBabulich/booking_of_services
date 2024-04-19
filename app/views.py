from flask import render_template, redirect
from flask_login import current_user
from app.reserve.forms.forms import ReserveForm


def home_page():
    form = ReserveForm()
    if current_user.is_authenticated:
        return redirect('cabinet/')
    return render_template('index.html', form=form)


def cabinet_page():
    return render_template('cabinet.html')
