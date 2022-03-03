#requried packages
pip install flask flask-sqlalchemy flask-wtf flask-api flask_restful
pip install mysql-connector
pip install pymysql
pip install cryptography
pip instal Flask-Migrate

#from python command line
from app import db
db.create_all()

#flask migrate package for project migration from flask command line
flask db init
flask db migrate -m "Migrate first time."
flask db upgrade


#flask migrate package for project migration from flask command line
flask db migrate -m "Migrate second time-add password field."
flask db upgrade