from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

class CreateBlog(FlaskForm):
    dish_name = StringField("Dish Name")
    dish_reciepe = TextAreaField("Receipe")
    save_blog = SubmitField("Save Blog")