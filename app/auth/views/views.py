from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.auth.forms.forms import LoginForm, RegistrationForm
from app.models import db, User
from flask_login import LoginManager, login_user, current_user, logout_user

auth_bp = Blueprint('auth', __name__, template_folder='../templates', static_folder='../static',
                    static_url_path='/auth/static')

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth_bp.route('/login', methods=['GET', 'POST'])
def login_page():
    '''
    Функция отображения страницы логина
    :return: Возвращает шаблон login.html и форму логина
    '''
    if current_user.is_authenticated:
        return redirect('/')
    form = LoginForm()
    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout', methods=['GET', 'POST'])
def logout_page():
    '''
    Функция для проведения выхода с сайта logout
    :return: Возвращает редирект на главную страницу после выхода с сайта
    '''
    logout_user()
    flash('Пользователь вышел с сайта', 'alert-success')
    return redirect('/')


@auth_bp.route('/process-login', methods=['POST'])
def process_login():
    '''
    Функция организует процесс авторизации пользователя и проверку введенных данных
    :return: Возвращает пользователя на главную страницу в случае успешного входа
    '''
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = User.query.filter(User.username == username).first()
            if user and user.check_password(password):
                login_user(user)
                flash('Пользователь вошел', 'alert-success')
                return redirect(url_for('cabinet.cabinet_page'))
        flash('Неверное имя или пароль', 'alert-danger')
        return redirect(url_for('auth.login_page'))


@auth_bp.route('/registration', methods=['GET', 'POST'])
def registration_page():
    '''
    Функция отображения формы и регистрации пользователя на сайте
    :return: Возвращает отображение шаблона и формы для регистрации
    '''
    if current_user.is_authenticated:
        return redirect('/')
    form = RegistrationForm()
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        password2 = request.form['password2']
        if password == password2:
            if User.query.filter(User.username == username).count():
                flash('Пользователь уже существует', 'alert-warning')
            else:
                user = User(username=username, email=email, phone=phone)
                user.set_password(password)
                db.session.add(user)
                db.session.commit()
                flash('Пользователь зарегистрирован', 'alert-success')
        else:
            flash('Пароли не совпадают', 'alert-danger')
    return render_template('auth/registration.html', form=form)
