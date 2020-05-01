from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField

class CreateBlog(FlaskForm):
    dish_name = StringField("Dish Name")
    dish_reciepe = TextAreaField("Receipe")
    dish_img = FileField("Image")
    save_blog = SubmitField("Add")