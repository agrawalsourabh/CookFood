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

db = SQLAlchemy(app=app)
Migrate(app=app, db=db)

login_manager.init_app(app=app)
login_manager.login_view = 'login'  # View called login

from .sign_up.view import signup_view_bp
from .login.view import login_view_bp

app.register_blueprint(signup_view_bp, url_prefix='/sign_up')
app.register_blueprint(login_view_bp, url_prefix='/login')