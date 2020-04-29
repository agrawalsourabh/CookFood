from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, RadioField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileAllowed, FileField

from my_project.sign_up.models import User

class SignUp(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])

    email = StringField("Email", validators=[DataRequired(), Email()])

    password = PasswordField("Password", validators=[DataRequired(), EqualTo('con_password', message="Password must match!!!")])
    con_password = PasswordField("Confirm Password", validators=[DataRequired()])

    submit = SubmitField("Create Account")

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email has been already registered!!!")



    
