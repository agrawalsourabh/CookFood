from my_project import app, db
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

# Forms
from my_project.blogs.forms import CreateBlog

create_blog_bp = Blueprint("create_blog_bp", __name__, template_folder="templates")

@create_blog_bp.route("/", methods=['GET', 'POST'])
@login_required
def create_blog():
    form = CreateBlog()

    if form.validate_on_submit():
        dish_name = form.dish_name.data
        dish_receipe = form.dish_reciepe

        return redirect(url_for('create_blog'))

    return render_template('blogs/create_blog.html', form=form)

