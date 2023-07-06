import os
from flask import render_template, session, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from flask_login import login_user, login_required, current_user, LoginManager, logout_user
from shop import app, db, bcrypt
from datetime import datetime
from .forms import LoginForm, SignUpForm
from .models import Users

@app.shell_context_processor
def make_shell_context():
 return dict(db=db, Users=Users)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    user = Users.query.get(int(user_id))
    return user    


#================= home view================
@app.route('/', endpoint='home')
def home():
    return render_template('index.html', current_time=datetime.utcnow(), endpoint=request.endpoint)


#================ sign-up view=================
@app.route('/sign-up', methods=['GET', 'POST'], endpoint='signUp')
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
        flash('Welcome back', 'success')
        return redirect(url_for('home'))
    return render_template("admin_temp/register.html", form=form,current_time=datetime.utcnow(), endpoint=request.endpoint)

# ===========login view============
@app.route('/login', methods=['GET', 'POST'], endpoint='login' )
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('user logged in successfully', 'success')
#=============== if user was redirected by protected route =================
#=============== access that route after a successful auth =================
            next_route = request.args.get('next')
            if next_route:
               return redirect(next_route) 
            #====== else go to home route =========           
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('admin_temp/login.html',form=form, current_time=datetime.utcnow(), endpoint=request.endpoint)



# =========================logout view======================= 
@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
   logout_user()
   flash('user logged out successfully', 'success')
   return redirect(url_for('login'))
   
   

#==================== handles errors 404 and 500================= 
@app.errorhandler(404)
def page_not_found(e):
 return "this is a 404 error page", 404
@app.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html'), 500