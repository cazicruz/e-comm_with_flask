from flask import Flask
import os
from  flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_moment import Moment
#from flask_uploads import UploadSet, IMAGES, configure_uploads




app = Flask(__name__)
app.config['SECRET_KEY'] = "hardtoguessstring"
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI']= \
 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'shop/static/uploads'

# profile_photo = UploadSet('photos', IMAGES)
# products_photo = UploadSet('products', IMAGES)
# configure_uploads(app, profile_photo)
# configure_uploads(app, products_photo)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
moment = Moment(app)
bootstrap = Bootstrap(app)

from shop.admin_shop import routes
