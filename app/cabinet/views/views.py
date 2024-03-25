from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import current_user

from app.models import Employees, db

from app.cabinet.forms.forms import EmployeeForm

cabinet_bp = Blueprint('cabinet', __name__, template_folder='../templates', static_folder='../static',
                       static_url_path='/cabinet/static')


@cabinet_bp.route('/', methods=['GET', 'POST'])
def cabinet_page():
    return render_template('cabinet/cabinet.html')


@cabinet_bp.route('/employees', methods=['GET', 'POST'])
def employees_page():
    form = EmployeeForm()
    employees = Employees.query.filter(Employees.owner_id == current_user.id)
    return render_template('cabinet/employees/employees.html', employees=employees, form=form)


@cabinet_bp.route('/employees/profile/<int:id>', methods=['GET', 'POST'])
def profile_employee(id):
    employees = Employees.query.filter(Employees.id == id)
    return render_template('cabinet/employees/profile_employee.html', employees=employees)


@cabinet_bp.route('/employees/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone = request.form['phone']
        status = request.form['status']
        description = request.form['description']
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
    return redirect(url_for('cabinet.employees_page'))


@cabinet_bp.route('/employees/update/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    employee = Employees.query.get_or_404(id)
    if request.method == 'POST':
        employee.first_name = request.form['first_name']
        employee.last_name = request.form['last_name']
        employee.phone = request.form['phone']
        employee.status = request.form['status']
        employee.description = request.form['description']
        db.session.commit()
        return redirect(url_for('cabinet.employees_page'))
    return redirect(url_for('cabinet.employees_page'))


@cabinet_bp.route('/employees/delete/<int:id>', methods=['GET', 'POST'])
def delete_employee(id):
    employee = Employees.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(employee)
        db.session.commit()
        return redirect(url_for('cabinet.employees_page'))
    return redirect(url_for('cabinet.employees_page'))
