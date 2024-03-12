from flask import Blueprint, render_template, request

auth_bp = Blueprint('auth', __name__, template_folder='../templates', static_folder='../static',
                    static_url_path='/auth/static')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login_page():
    title = 'Авторизация'
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == '1':
            print('login success')
        else:
            print('login denied')
    return render_template('auth/login.html', title=title)


@auth_bp.route('/registration', methods=['GET', 'POST'])
def registration_page():
    title = 'Регистрация'
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        password2 = request.form['password2']
        registration_dict = {'name': name, 'email': email, 'phone': phone, 'password': password, 'password2': password2}
        print(registration_dict)
    return render_template('auth/registration.html', title=title)
