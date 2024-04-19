from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for
from app.models import db, Notification

notification_bp = Blueprint('notification', __name__, template_folder='../templates', static_folder='../static')


def create_notification(description):
    timestamp = datetime.utcnow()
    notification = Notification(description=description, timestamp=timestamp)
    db.session.add(notification)
    db.session.commit()


@notification_bp.route('/notifications', methods=['GET', 'POST'])
def notification_page():
    notifications = db.session.query(Notification).all()
    return render_template('notification/notifications.html', notifications=notifications)


@notification_bp.route('/notifications/delete/<int:id>', methods=['GET', 'POST'])
def if_read(id):
    notification = Notification.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(notification)
        db.session.commit()
        return redirect(url_for('notification.notification_page'))
    return redirect(url_for('notification.notification_page'))
