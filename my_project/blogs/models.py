from my_project import app, db
from my_project.sign_up.models import User
from datetime import datetime


class Blog(db.Model):

    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    
    dish_name = db.Column(db.String(60), nullable=False)
    dish_receipe = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    email = db.Column(db.String(80), db.ForeignKey('users.email'), nullable=False)
    user = db.relationship('User', backref=db.backref('blogs', lazy=True))
    

    def __init__(self, email, dish_name, dish_receipe):
        self.email = email
        self.dish_name = dish_name
        self.dish_receipe = dish_receipe

    def __repr__(self):
        return "User: {} \n Receipe Name: {} \n Receipe: {} ".format(self.email, self.dish_name, self.dish_receipe)
