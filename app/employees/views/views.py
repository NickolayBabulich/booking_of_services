from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user
from app.models import Employees, db
from app.employees.forms.forms import EmployeeForm

employees_bp = Blueprint('employees', __name__, template_folder='../templates', static_folder='../static',
                         static_url_path='/employees/static')


@employees_bp.route('/employees', methods=['GET', 'POST'])
def employees_page():
    form = EmployeeForm()
    employees = Employees.query.filter(Employees.owner_id == current_user.id)
    return render_template('employees/employees.html', employees=employees, form=form)


@employees_bp.route('/employees/profile/<int:id>', methods=['GET', 'POST'])
def profile_employee(id):
    employees = Employees.query.filter(Employees.id == id)
    return render_template('employees/profile_employee.html', employees=employees)


@employees_bp.route('/employees/add', methods=['GET', 'POST'])
def add_employee():
    form = EmployeeForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone = form.phone.data
        status = form.status.data
        description = form.description.data
        owner_id = current_user.id
        employee = Employees(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            status=status,
            description=description,
            owner_id=owner_id
        )
        db.session.add(employee)
        db.session.commit()

    return redirect(url_for('employees.employees_page'))


@employees_bp.route('/employees/update/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    employee = Employees.query.get_or_404(id)
    form = EmployeeForm()
    if form.validate_on_submit():
        employee.first_name = form.first_name.data
        employee.last_name = form.last_name.data
        employee.phone = form.phone.data
        employee.status = form.status.data
        employee.description = form.description.data
        db.session.commit()
        return redirect(url_for('employees.employees_page'))
    return redirect(url_for('employees.employees_page'))


@employees_bp.route('/employees/delete/<int:id>', methods=['GET', 'POST'])
def delete_employee(id):
    employee = Employees.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(employee)
        db.session.commit()
        return redirect(url_for('employees.employees_page'))
    return redirect(url_for('employees.employees_page'))
