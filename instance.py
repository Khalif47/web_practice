import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.secret_key = "sjfgiefyhube"
DB_URL = 'mysql://{user}:{pw}@{url}/{db}'.format(user='root', pw='root', url='localhost',
                                                 db='students')

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Country = db.Column(db.String(200), unique=False, nullable=True)
    time = db.Column(db.String, unique=False, nullable=True)


db.create_all()

time = ['2', '3', '4', '4']
Country = ['new york', 'melbourne',
           'Athens00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
           'Nairobi']
pd.set_option('display.max_colwidth', 1000)
print(pd.DataFrame({'Country': Country, 'time': time}))
