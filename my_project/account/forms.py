from flask_wtf  import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from flask_wtf.file import FileAllowed, FileField
from wtforms.validators import EqualTo, DataRequired

from my_project.sign_up.models import User


class UpdateAccount(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")

    # email should be disable
    email = StringField("Email")

    old_password = PasswordField("Password")
    new_password = PasswordField("New Password", validators=[EqualTo('con_password', message="Password must match!!!")])
    con_password = PasswordField("Confirm Password")
    profile_pic = FileField('Update Profile Pic')

    submit = SubmitField("Update Account")
