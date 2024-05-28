from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin): #This is the user class that we are going to use to create users
    id = db.Column(db.Integer, primary_key=True) #This is the id of the user
    email = db.Column(db.String(150), unique=True) #This is the email of the user
    password = db.Column(db.String(150)) #This is the password of the user
    first_name = db.Column(db.String(150)) #This is the first name of the user
