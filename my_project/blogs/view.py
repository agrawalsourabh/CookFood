from my_project import app, db
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from sqlalchemy import desc

# Picture handler
from my_project.account.picture_handler import add_dish_pic

# Forms
from my_project.blogs.forms import CreateBlog

# Models
from my_project.blogs.models import Blog

from datetime import datetime

blog_bp = Blueprint("blog_bp", __name__, template_folder="templates")

@blog_bp.route("/create_blog", methods=['GET', 'POST'])
@login_required
def create_blog():
    form = CreateBlog()

    if form.validate_on_submit():
        dish_name = form.dish_name.data
        dish_receipe = form.dish_reciepe.data

        count = db.session.query(Blog).filter_by(email=current_user.email).count()
        blog = Blog(email=current_user.email, dish_name=dish_name, dish_receipe=dish_receipe, count=count)

        print(blog)
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

@blog_bp.route("/update_blog/<blog_id>", methods=['GET', 'POST'])
@login_required
def update_blog(blog_id):
    blog_to_be_updated = Blog.query.filter_by(blog_id=blog_id).first()
    print(blog_to_be_updated.dish_name)
    print(blog_to_be_updated.dish_receipe)
    form = CreateBlog()

    if form.validate_on_submit():

        if form.dish_name.data:
            blog_to_be_updated.dish_name = form.dish_name.data

        if form.dish_reciepe.data:
            blog_to_be_updated.dish_receipe = form.dish_reciepe.data



        if form.dish_img.data:
            print(form.dish_img.data)
            pic = add_dish_pic(pic_upload=form.dish_img.data, blog_id=blog_id)
            blog_to_be_updated.recipe_img = pic
            print("Image uploaded")
        
        # blog_to_be_updated.date = datetime.utcnow

        db.session.add(blog_to_be_updated)
        db.session.commit()

        return redirect(url_for('blog_bp.view_blogs'))

    elif request.method == "GET":
        form.dish_name.data = blog_to_be_updated.dish_name
        # form.email.data = current_user.email
        form.dish_reciepe.data = blog_to_be_updated.dish_receipe


        
    return render_template('blogs/update_blog.html', blog=blog_to_be_updated, form=form)
    

@blog_bp.route("/<blog_id>")
@login_required
def view_blog(blog_id):
    blog = Blog.query.filter_by(blog_id=blog_id).first()
    return render_template('blogs/blog.html', blog=blog)