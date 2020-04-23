from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, RadioField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

class Login(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])

    submit = SubmitField("Log In")