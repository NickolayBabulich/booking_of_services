import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'fdsf432twgwhH^#2tergsfd2fhT%Y$22GFGfdsgbb2t2g2%@%@2gfgdg22@2gfg1165FG@dfdbt4tT4$fgd'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.db')
