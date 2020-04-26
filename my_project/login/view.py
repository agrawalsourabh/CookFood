from my_project import app, db
from flask import Blueprint, render_template, redirect, url_for, flash, request
from my_project.login.forms import Login
from my_project.sign_up.models import User
from flask_login import login_user, current_user, login_required

login_view_bp = Blueprint('login_view_bp', __name__, template_folder='templates')

@login_view_bp.route('/', methods=['GET', 'POST'])
def login():
    form = Login()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email = email).first()

        if user.check_password(password) and user is not None:
            # login_user is the method of Login class
            login_user(user)    

            next = request.args.get('next')

            # if not is_safe_url(next):
            #     return flask.abort(400)

            if next == None or not next[0] == '/':
                next = '/welcome'

            return redirect(next)

    return render_template('login/login.html', form=form)
