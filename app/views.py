from flask import render_template


def home_page():
    title = 'Booking of services - Сервис бронирования услуг'
    return render_template('index.html', title=title)
