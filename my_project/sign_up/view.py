from my_project import app, db
from flask import Blueprint, render_template, redirect, url_for, flash
from my_project.sign_up.forms import SignUp

from my_project.sign_up.models import User, UserInfo

signup_view_bp = Blueprint('signup_view_bp', __name__, template_folder='templates')

@signup_view_bp.route('/', methods= ['GET', 'POST'])
def signup():
    form = SignUp()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data

        check_user = UserInfo.query.filter_by(email=email).first()

        if check_user:
            return redirect(url_for('signup_view_bp.signup'))
            

        user = User(email=email, password=password)
        user_info = UserInfo(first_name=first_name, last_name=last_name)
        

        user.usersinfo.append(user_info)

        db.session.add(user)
        db.session.commit()

    
        return redirect(url_for('signup_view_bp.view_users'))

    return  render_template('sign_up/sign_up.html', form=form)

@signup_view_bp.route('/view_users')
def view_users():
    all_users = User.query.all()
    # return ""+str(len(all_users))

    return render_template('sign_up/list.html', all_users=all_users)
