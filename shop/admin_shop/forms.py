from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, SelectField
from wtforms.validators import DataRequired, InputRequired, Email, Length, EqualTo, ValidationError
from shop import bcrypt
from admin_shop import Users


class LoginForm(FlaskForm):
    username = StringField(' Username: ', validators=[InputRequired()], render_kw={"placeholder": "username"})
    password = PasswordField(' Password: ',validators=[DataRequired(message='Required'), Length(10)], render_kw={"placeholder": "password"})
    loginButton = SubmitField('Login')

    def login_validation(self , username, password):
        user = Users.query.filter_by(username=username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, password.data):
                return True
            else:
                raise ValidationError("Wrong Login Credentials.")
        return False


class SignUpForm(FlaskForm):
    fname = StringField('firstname', validators=[DataRequired()],  render_kw={"placeholder": "first name"})
    lname = StringField('lastname', validators=[DataRequired()], render_kw={"placeholder": "last name"})
    email = EmailField('email', validators=[InputRequired()],  render_kw={"placeholder": "Email"})
    username = StringField('Username', validators=[DataRequired()],render_kw={"placeholder": "pick a username"})
    address = StringField('address', validators=[DataRequired(), Length(10)], render_kw={"placeholder": "address"})
    password1 = PasswordField(U' Password: ',validators=[InputRequired(message='Required'), Length(10)])
    password2 = PasswordField(U'Confirm Password: ',validators=[InputRequired(message='Required'), Length(10), EqualTo('password1')])
    roleSelection = SelectField('Type of user', choices=[('Patient', 'Patient'), ('Doctor', 'Doctor')], validators=[InputRequired(message='select a role')])
    submit = SubmitField('submit')

    def validate_username(self, username):
        existing_username = Users.query.filter_by(username=username.data).first()
        if existing_username:
            raise ValidationError('username exists already.')
