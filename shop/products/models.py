from shop import db
from datetime import datetime


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(120), unique=False, nullable=False)
    item = db.Column(db.String(80), unique=False, nullable=False)
    product_name = db.Column(db.String(80), unique=False, nullable=False)
    price = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(400), unique=False, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image_1 = db.Column(db.String(180), nullable=True, default='product.jpg')
    image_2 = db.Column(db.String(180), nullable=True, default='product.jpg')
    image_3 = db.Column(db.String(180), nullable=True, default='product.jpg')
    image_4 = db.Column(db.String(180), nullable=True, default='product.jpg')
    image_5 = db.Column(db.String(180), nullable=True, default='product.jpg')
    

    def __repr__(self):
        return '<Products %r>' % self.username


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),nullable=False, unique=True)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),nullable=False, unique=True)


