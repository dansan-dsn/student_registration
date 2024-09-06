from . import db

class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    reg_no = db.Column(db.String(255), nullable=False, unique=True)
    course = db.Column(db.String(100), nullable=False)
    phone_no = db.Column(db.String(15), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='student')

    def __init__(self, name, reg_no, course, phone_no):
        self.name = name
        self.reg_no = reg_no
        self.course = course
        self.phone_no = phone_no