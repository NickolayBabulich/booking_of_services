from flask import Flask
from app.models import db
from app.views import home_page
from app.auth.views.views import auth_bp, login_manager
from app.cabinet.views.views import cabinet_bp


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    db.init_app(app)

    app.add_url_rule('/', view_func=home_page)
    app.register_blueprint(auth_bp)
    app.register_blueprint(cabinet_bp, url_prefix='/cabinet/')
    login_manager.init_app(app)

    return app
