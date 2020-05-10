from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required

# import form
from flask_wtf import FlaskForm
# from my_project.setting.form import form

# import db
from my_project import db

setting_view_bp = Blueprint("setting_view_bp", __name__, template_folder='templates')

@setting_view_bp.route('/')
@login_required
def setting():
    return render_template('setting/setting.html')