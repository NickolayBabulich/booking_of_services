from flask import Flask
from app.views import home_page
from app.auth.views.views import auth_bp

app = Flask(__name__)

app.add_url_rule('/', view_func=home_page)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)
