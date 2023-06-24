import os
from flask import render_template, session, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from flask_login import login_user, logout_user, login_required, current_user
from shop import app, db, bcrypt
from datetime import datetime
from .forms import LoginForm, SignUpForm
from .models import Users, Products

@app.shell_context_processor
def make_shell_context():
 return dict(db=db, Users=Users, products=Products)




@app.route('/')
def home():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

@app.route('/sign-up', methods=['GET', 'POST'])
def signUp():
    form = SignUpForm(request.form)


    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password1.data)

        img = request.files['profile_img']
        filename = secure_filename(img.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(path):
            flash('Image already exists')
            ''' remember to add a random string to the filename to avoid overwriting existing files
            or add current_user to the filename to avoid overwriting existing files'''
        if img == '':
            flash('No image selected for uploading')
        else:
           img.save(path)

        user = Users(fname=request.form.get('fname'), lname=form.lname.data, username=form.username.data, email=form.email.data, password=hash_password,profile_img=path)
        db.session.add(user)
        db.session.commit()
        #flash('Welcome back')
        return redirect(url_for('home'))
    return render_template("admin_temp/register.html", form=form,current_time=datetime.utcnow())

@app.route('/login', methods=['GET', 'POST'] )
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['username'] = user.username
            session['id'] = user.id
            flash('Welcome back')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
    
    return render_template('admin_temp/login.html',form=form, current_time=datetime.utcnow())

@app.route('/product', methods=['GET', 'POST'] )
def product():
    return render_template('product.html')

# handles errors 404 and 500 
@app.errorhandler(404)
def page_not_found(e):
 return "this is a 404 error page", 404
@app.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html'), 500