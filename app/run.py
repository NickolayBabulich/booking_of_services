from flask import Flask
from app.views import home_page

app = Flask(__name__)

app.add_url_rule('/', view_func=home_page)

if __name__ == '__main__':
    app.run(debug=True)
