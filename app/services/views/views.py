from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user
from app.models import Services, db
from app.services.forms.forms import ServiceForm

services_bp = Blueprint('services', __name__, template_folder='../templates', static_folder='../static',
                        static_url_path='/services/static')


@services_bp.route('/services', methods=['GET', 'POST'])
def services_page():
    form = ServiceForm()
    services = Services.query.filter(Services.owner_id == current_user.id)
    return render_template('services/services.html', services=services, form=form)


@services_bp.route('/services/add', methods=['GET', 'POST'])
def add_service():
    form = ServiceForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        price = form.price.data
        owner_id = current_user.id
        service = Services(
            title=title,
            description=description,
            price=price,
            owner_id=owner_id
        )
        db.session.add(service)
        db.session.commit()
    return redirect(url_for('services.services_page'))


@services_bp.route('/services/update/<int:id>', methods=['GET', 'POST'])
def edit_service(id):
    service = Services.query.get_or_404(id)
    form = ServiceForm()
    if form.validate_on_submit():
        service.title = form.title.data
        service.description = form.description.data
        service.price = form.price.data
        db.session.commit()
        return redirect(url_for('services.services_page'))
    return redirect(url_for('services.services_page'))


@services_bp.route('/services/delete/<int:id>', methods=['GET', 'POST'])
def delete_service(id):
    employee = Services.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(employee)
        db.session.commit()
        return redirect(url_for('services.services_page'))
    return redirect(url_for('services.services_page'))
