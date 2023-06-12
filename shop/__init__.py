from flask import Flask
import os
from  flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_moment import Moment




app = Flask(__name__)
app.config['SECRET_KEY'] = "hardtoguessstring"
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI']= \
 'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
moment = Moment(app)
bootstrap = Bootstrap(app)

from shop.admin_shop import routes
