from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class User(UserMixin, db.Model):


    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    verification_token = db.Column(db.String(150), unique=True, nullable=False)
    is_verified = db.Column(db.Boolean, nullable=False, default=False)
    password = db.Column(db.String(), nullable=False)


    #from app import login
    def __init__(self, username, password, email, verification_token, is_verified, *arg, **kwarg):
            self.username = username
            self.email = email
            self.verification_token = verification_token
            self.is_verified = is_verified
            self.set_password(password)
            
    def set_password(self, password):
            self.password = generate_password_hash(password)

    def check_password(self, password):
            return check_password_hash(self.password, password)
