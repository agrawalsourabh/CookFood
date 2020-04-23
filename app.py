from my_project import app
from flask import Flask, render_template, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You logged out")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)