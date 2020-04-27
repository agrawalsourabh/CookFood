from my_project import app
from flask import Flask, render_template, flash, redirect, url_for, request
from flask_login import login_required, login_user, logout_user, current_user

# import flask login form
from my_project.login.forms import Login

# import signup  model
from my_project.sign_up.models import User

@app.route('/', methods=['GET', 'POST'])
def index():
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

    return render_template('index.html', form=form)

@app.route('/welcome')
@login_required
def welcome():
    user = current_user
    return render_template('welcome.html', user=user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)