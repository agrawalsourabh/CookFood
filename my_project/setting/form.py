from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, RadioField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileAllowed, FileField

from my_project.sign_up.models import User

class PasswordForm(FlaskForm):
    
    old_password = PasswordField("Old Password", validators=[DataRequired()])
    new_password = PasswordField("New Password", validators=[DataRequired(), EqualTo('con_password', message="Password must match!!!")])
    con_password = PasswordField("Confirm Password", validators=[DataRequired()])

    submit = SubmitField("Change Password")


    
