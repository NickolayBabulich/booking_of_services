from flask import Flask
from app.models import db, Notification
from app.views import home_page, cabinet_page
from app.auth.views.views import auth_bp, login_manager
from app.employees.views.views import employees_bp
from app.services.views.views import services_bp
from app.scheduler.views.views import scheduler_bp
from app.reserve.views.views import reserve_bp
from app.notification.views.views import notification_bp


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    db.init_app(app)
    app.add_url_rule('/', view_func=home_page)
    app.add_url_rule('/cabinet/', view_func=cabinet_page)
    app.register_blueprint(auth_bp)
    app.register_blueprint(employees_bp, url_prefix='/cabinet/')
    app.register_blueprint(services_bp, url_prefix='/cabinet/')
    app.register_blueprint(scheduler_bp, url_prefix='/cabinet/')
    app.register_blueprint(reserve_bp)
    app.register_blueprint(notification_bp, url_prefix='/cabinet/')
    login_manager.init_app(app)

    @app.context_processor
    def inject_notifications():
        notifications = db.session.query(Notification).all()
        return dict(notifications=notifications)

    return app
