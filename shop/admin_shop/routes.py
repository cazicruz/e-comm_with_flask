from flask import render_template, session, request, redirect, url_for
from shop import app, db, bcrypt
from datetime import datetime
from .forms import LoginForm, SignUpForm
from .models import Users, Products




@app.route('/')
def home ():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

@app.route('/sign-up', methods=['GET', 'POST'])
def signUp():
    form = SignUpForm(request.form)

    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = Users(username=form.username.data, password=hash_password, fname=form.fname.data, lname=form.lname.data, email=form.email.data, profile_img=form.photo.data )
        db.session.add(user)
        db.session.commit()
        #flash('Welcome back')
        return redirect(url_for('home'))
    return render_template("admin_temp/register.html", form=form,current_time=datetime.utcnow())

@app.route('/login', methods=['GET', 'POST'] )
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        return redirect(url_for('home'))    
    
    return render_template('admin_temp/login.html',form=form, current_time=datetime.utcnow())

@app.route('/product', methods=['GET', 'POST'] )
def product():
    return render_template('product.html')

# handles errors 404 and 500 
@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html'), 500