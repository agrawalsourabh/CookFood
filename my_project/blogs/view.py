from my_project import app, db
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from sqlalchemy import desc

# Forms
from my_project.blogs.forms import CreateBlog

# Models
from my_project.blogs.models import Blog

blog_bp = Blueprint("blog_bp", __name__, template_folder="templates")

@blog_bp.route("/")
@login_required
def blog():
    return render_template('blogs/blog.html')

@blog_bp.route("/create_blog", methods=['GET', 'POST'])
@login_required
def create_blog():
    form = CreateBlog()

    if form.validate_on_submit():
        dish_name = form.dish_name.data
        dish_receipe = form.dish_reciepe.data

        blog = Blog(email=current_user.email, dish_name=dish_name, dish_receipe=dish_receipe)

        db.session.add(blog)
        db.session.commit()

        flash("Blog  created successfully")

        return redirect(url_for('blog_bp.view_blogs'))

    return render_template('blogs/create_blog.html', form=form)


@blog_bp.route("/view_blogs")
@login_required
def view_blogs():

    blogs_list = Blog.query.order_by(desc(Blog.date)).all()
    return render_template('blogs/view_blogs.html', blogs_list=blogs_list)
