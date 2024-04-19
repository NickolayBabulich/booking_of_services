import datetime

from flask import Blueprint, render_template, redirect, url_for, request

from app.models import Scheduler, db
from app.notification.views.views import create_notification
from app.reserve.forms.forms import ReserveForm

reserve_bp = Blueprint('reserve', __name__, template_folder='../templates', static_folder='../static',
                       static_url_path='/reserve/static')


def get_scheduler():
    objects = Scheduler.query.all()
    return objects


@reserve_bp.route('/reserve', methods=['GET', 'POST'])
def pick_service():
    form = ReserveForm()
    if form.validate_on_submit():
        service = form.service.data
        if_service = Scheduler.query.filter_by(service_id=service, status='OPEN').order_by(Scheduler.date,
                                                                                           Scheduler.time).all()
        return render_template('reserve/reserve.html', form=form, if_service=if_service)
    return render_template('reserve/reserve.html', form=form)


@reserve_bp.route('/reserve/notification', methods=['GET', 'POST'])
def user_notification():
    return render_template('reserve/notification.html')


@reserve_bp.route('/reserve/add/<int:id>', methods=['GET', 'POST'])
def add_reserve(id):
    scheduler = Scheduler.query.get_or_404(id)
    form = ReserveForm()
    if request.method == 'POST':
        scheduler.client_name = form.client_name.data
        scheduler.phone = form.phone.data
        scheduler.status = 'BOOKED'
        db.session.commit()
        description = (f'Клиент - {scheduler.client_name}, с номером {scheduler.phone}'
                       f' записался на услугу {scheduler.service.title}'
                       f' к мастеру {scheduler.employee.first_name} на {scheduler.date.strftime("%d.%m.%Y")}'
                       f' в {scheduler.time.strftime("%H:%M")}')
        print(create_notification(description))
        return redirect(url_for('reserve.user_notification'))
    print(form.errors)

    return redirect('/')
