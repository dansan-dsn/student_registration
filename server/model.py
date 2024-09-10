# from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    other_name = db.Column(db.String(100), nullable=True)
    reg_no = db.Column(db.String(255), nullable=True, unique=True)
    email = db.Column(db.String(50), nullable=True)
    phone_no = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    user_no = db.Column(db.String(255), nullable=True, default='0', unique=True)
    role = db.Column(db.String(50), nullable=False)

    def __init__(self, first_name, last_name, other_name, reg_no, email, phone_no, password, user_no, role):
        self.first_name = first_name
        self.last_name = last_name
        self.other_name = other_name
        self.reg_no = reg_no
        self.email = email
        self.phone_no = phone_no
        self.password = password
        self.user_no = user_no
        self.role = role

    
