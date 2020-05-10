import os

from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
login_manager = LoginManager()

app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app=app)
Migrate(app=app, db=db)

login_manager.init_app(app=app)
login_manager.login_view = 'login'  # View called login

from .sign_up.view import signup_view_bp
from .login.view import login_view_bp
from my_project.blogs.view import blog_bp
from my_project.account.view import account_view_bp
from my_project.setting.view import setting_view_bp
from my_project.error_pages.error_handler_view import error_pages_bp

app.register_blueprint(signup_view_bp, url_prefix='/sign_up')
app.register_blueprint(login_view_bp, url_prefix='/login')
app.register_blueprint(blog_bp, url_prefix='/blogs')
app.register_blueprint(account_view_bp)
app.register_blueprint(setting_view_bp, url_prefix='/settings')
app.register_blueprint(error_pages_bp)