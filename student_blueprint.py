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
def get_students():
    all_students = Student.query.all()
    result = students_schema.dump(all_students)
    return jsonify(result), 200

@student.route('/<id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({'msg': 'Student is not found'}), 404
    
    return student_schema.jsonify(student)

@student.route('/update/<id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"error": "Student not found "})
    data = request.json

    if 'name' in data:
        student.name = data['name']
    if 'reg_no' in data:
        student.reg_no = data['reg_no']
    if 'course' in data:
        student.course = data['course']
    if 'phone_no' in data:
        student.phone_no = data['phone_no']
    
    db.session.commit()

    return student_schema.jsonify(student), 200

@student.route('/remove/<id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"error": "Student not found"})
    db.session.delete(student)
    db.session.commit()

    return jsonify({"msg": "Student deleted successfully"})