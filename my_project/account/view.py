from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
# import UpdateAccount Form
from flask_wtf import FlaskForm
from my_project.account.forms import UpdateAccount
# import signup.models User and UserInfo
from my_project.sign_up.models import User, UserInfo
from sqlalchemy import desc
# import db
from my_project import db

# Models
from my_project.blogs.models import Blog

account_view_bp = Blueprint("account_view_bp", __name__, template_folder='templates')

@account_view_bp.route('/account', methods=['GET', 'POST'])
@login_required
def account_view():
    form = UpdateAccount()

    user_info = UserInfo.query.filter_by(email=current_user.email).first()
    blogs_list = Blog.query.order_by(desc(Blog.date)).filter_by(email=current_user.email).all()

    # first_name = form.first_name.data
    # last_name = form.last_name.data
    # email = form.email.data

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data # disabled

        user_info.first_name = first_name
        user_info.last_name = last_name

        db.session.add(user_info)
        db.session.commit()

        return redirect(url_for('blog_bp.view_blogs'))

    return render_template('account/update_account.html', form=form, user_info=user_info, blogs_list=blogs_list)


        





