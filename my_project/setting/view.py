from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required

# import form
from flask_wtf import FlaskForm
from my_project.setting.form import PasswordForm, DeactivateUserForm

# import db
from my_project import db
from my_project.sign_up.models import User

setting_view_bp = Blueprint("setting_view_bp", __name__, template_folder='templates')

@setting_view_bp.route('/', methods=['GET', 'POST'])
@login_required
def setting():
    # user_name
    from my_project.current_username import user_name

    form = PasswordForm()
    deativate_user_form = DeactivateUserForm()

    user = User.query.filter_by(email=current_user.email).first()

    if  form.validate_on_submit():
        old_password = form.old_password.data
        new_password = form.new_password.data

        if user.check_password(password=old_password):
            print("Password Matches!")
            user.set_password(new_password)

            db.session.add(user)
            db.session.commit()

            print("Password updated!")

            return redirect(url_for('setting_view_bp.setting'))

        else:
            print("Wrong password")

    elif deativate_user_form.validate_on_submit():

        if user is not None:
            db.session.delete(user)
            db.session.commit()
            print("user deleted")

            return redirect('/')


        print("form deactivate btn clicked")


    return render_template('setting/setting.html', form=form,  deativate_user_form=deativate_user_form, profile_image=user_name())