from flask import render_template, session, request, redirect, url_for, flash
from shop import app, db
from flask_login import login_required
from datetime import datetime
from .models import Brand, Category , Products
from .forms import AddProducts



#===================product view==================
@app.route('/products', methods=['GET', 'POST'], endpoint='products')
@login_required
def products():
    endpoint = request.endpoint
    return render_template('product_temp/product.html', endpoint=endpoint,current_time=datetime.utcnow())


#============== add brand view==========
@app.route('/addbrand',methods=['GET','POST'], endpoint='addbrand')
@login_required
def addBrand():
    if request.method == 'POST':
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash("The brand {} was added to the database".format(brand.name), 'success')
        db.session.commit()

    return render_template('product_temp/addbrand.html', endpoint=request.endpoint,current_time=datetime.utcnow())

@app.route('/addcategory',methods=['GET','POST'], endpoint='addcategory')
@login_required
def addCategory():
    if request.method == 'POST':
        getCat = request.form.get('category')
        cat = Category(name=getCat)
        db.session.add(cat)
        flash("The brand {} was added to the database".format(cat.name), 'success')
        db.session.commit()

    return render_template('product_temp/addbrand.html', endpoint=request.endpoint,current_time=datetime.utcnow())


@app.route('/addproducts', methods=['GET','POST'])
def addProduct():
    form = AddProducts()

    return render_template('product_temp/addproducts.html', form=form, current_time=datetime.utcnow())