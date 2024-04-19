from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user
from app.models import Scheduler, db
from app.scheduler.forms.forms import SchedulerForm

scheduler_bp = Blueprint('scheduler', __name__, template_folder='../templates', static_folder='../static',
                         static_url_path='/scheduler/static')


@scheduler_bp.route('/scheduler', methods=['GET', 'POST'])
def scheduler_page():
    form = SchedulerForm()
    scheduler = Scheduler.query.filter(Scheduler.owner_id == current_user.id)
    return render_template('scheduler/scheduler.html', scheduler=scheduler, form=form)


@scheduler_bp.route('/scheduler/add', methods=['GET', 'POST'])
def add_scheduler():
    form = SchedulerForm()
    if form.validate_on_submit():
        service = form.service.data
        employee = form.employee.data
        date = form.date.data
        time = form.time.data
        client_name = form.client_name.data
        phone = form.phone.data
        status = form.status.data
        owner_id = current_user.id
        scheduler = Scheduler(
            service_id=service,
            employee_id=employee,
            date=date,
            time=time,
            client_name=client_name,
            phone=phone,
            status=status,
            owner_id=owner_id
        )
        db.session.add(scheduler)
        db.session.commit()
        return redirect(url_for('scheduler.scheduler_page'))
    return redirect(url_for('scheduler.scheduler_page'))


@scheduler_bp.route('/scheduler/update/<int:id>', methods=['GET', 'POST'])
def edit_scheduler(id):
    scheduler = Scheduler.query.get_or_404(id)
    form = SchedulerForm()
    if form.validate_on_submit():
        scheduler.service_id = form.service.data
        scheduler.employee_id = form.employee.data
        scheduler.date = form.date.data
        scheduler.time = form.time.data
        scheduler.client_name = form.client_name.data
        scheduler.phone = form.phone.data
        scheduler.status = form.status.data
        db.session.commit()
        print(form.errors)
        print(scheduler.time, form.time.data)
        return redirect(url_for('scheduler.scheduler_page'))
    print(form.errors)
    print(scheduler.time, form.time.data)
    return redirect(url_for('scheduler.scheduler_page'))


@scheduler_bp.route('/scheduler/delete/<int:id>', methods=['GET', 'POST'])
def delete_scheduler(id):
    scheduler = Scheduler.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(scheduler)
        db.session.commit()
        return redirect(url_for('scheduler.scheduler_page'))
    return redirect(url_for('scheduler.scheduler_page'))
