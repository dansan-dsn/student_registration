from flask import Blueprint,request, jsonify
from . import db,ma
from .model import Student

student = Blueprint('student',__name__)

class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        load_instance = True

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

@student.route('/new_student', methods=['POST'])
def new_student():
    name = request.json.get('name')
    reg_no = request.json.get('reg_no')
    course  = request.json.get('course')
    phone_no = request.json.get('phone_no')

    if not name or not reg_no or not course or not phone_no:
        return jsonify({'error': 'All fields are required'}), 400
    
    existing_student = Student.query.filter_by(reg_no=reg_no).first()
    if existing_student:
        return jsonify({'error': 'Student with the same registration number already exists'}), 400
    
    new_student = Student(name=name, reg_no=reg_no, course=course, phone_no=phone_no)
    db.session.add(new_student)
    db.session.commit()

    return student_schema.jsonify(new_student), 201

@student.route('/', methods=['GET'])
def get_student():
    all_students = Student.query.all()
    result = students_schema.dump(all_students)
    return jsonify(result), 200
