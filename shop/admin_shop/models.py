from shop import db
from datetime import datetime


class Users(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20),unique=False, nullable=False)
    lname = db.Column(db.String(20), unique=False,nullable=False)
    username = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(50),unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    profile_img = db.Column(db.String(180), nullable=True, default='profile.jpg')
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(120), unique=False, nullable=False)
    item = db.Column(db.String(80), unique=False, nullable=False)
    product_name = db.Column(db.String(80), unique=False, nullable=False)
    price = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(400), unique=False, nullable=False)

    def __repr__(self):
        return '<Products %r>' % self.username
    
#db.create_all()