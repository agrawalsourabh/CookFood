from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required

# import form
from flask_wtf import FlaskForm
from my_project.setting.form import PasswordForm

# import db
from my_project import db
from my_project.sign_up.models import User

setting_view_bp = Blueprint("setting_view_bp", __name__, template_folder='templates')

@setting_view_bp.route('/', methods=['GET', 'POST'])
@login_required
def setting():
    form = PasswordForm()
    user = User.query.filter_by(email=current_user.email).first()

    if  form.validate_on_submit():
        old_password = form.old_password.data
        new_password = form.new_password.data

        if(user.check_password(password=old_password)):
            print("Password Matches!")
            return redirect(url_for('setting_view_bp.setting'))

        else:
            print("Wrong password")


    return render_template('setting/setting.html', form=form)