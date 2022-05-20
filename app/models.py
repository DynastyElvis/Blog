from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func



class User(db.Model,UserMixin):
    '''
    create the user schema for the user table
    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(128))
    blog = db.relationship('Blog',lazy='dynamic')
    
    
