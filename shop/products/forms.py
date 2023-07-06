from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Email, Length, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired




#========= form class to get the product details from the user ==========
class AddProducts(FlaskForm):
    name = StringField('product name', validators=[DataRequired()], render_kw={"placeholder": "product name"})
    price = IntegerField('price', validators=[DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stuck', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    colors = TextAreaField('Color', validators=[DataRequired()])
#=============== form fields to collect product images ============
    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg', 'png','gif', 'jpeg'])], render_kw={"placeholder": "Images only please"})
    image_2 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg', 'png','gif', 'jpeg'])], render_kw={"placeholder": "Images only please"})
    image_3 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg', 'png','gif', 'jpeg'])], render_kw={"placeholder": "Images only please"})
    image_4 = FileField('Image 1', validators=[FileAllowed(['jpg', 'png','gif', 'jpeg'])],render_kw={"placeholder": "Images only please"})
    submit = SubmitField('submit')