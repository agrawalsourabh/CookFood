from flask_bcrypt import Bcrypt
from my_project import db, app, login_manager
from flask_login import UserMixin

bcrypt = Bcrypt(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password_hash = db.Column(db.Text, nullable=False)


    def __init__(self, email, password):

        self.email = email
        self.password_hash = bcrypt.generate_password_hash(password=password)


    def __repr__(self):
        return "Username: {} {}".format(self.id, self.email)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password=password)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password=password)

class UserInfo(db.Model):

    __tablename__ = 'usersinfo'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.Integer, db.ForeignKey('users.email'),
        nullable=False)
    profile_image = db.Column(db.String(80), nullable=False, default='default.png')

    user = db.relationship('User',backref=db.backref('usersinfo', lazy=True, cascade="all,delete"))

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "Name: {} {} Email: {}".format(self.first_name, self.last_name, self.user)