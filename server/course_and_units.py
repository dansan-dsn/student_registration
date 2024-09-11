from flask import Blueprint, request, jsonify
from .model import Course, Unit
from . import db, ma

course_and_units = Blueprint('course_and_units',__name__)

class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course
        include_fk = True
        load_instance = True


class UnitSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Unit
        include_fk = True
        load_instance = True

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)
unit_schema = UnitSchema()
unit_schema = UnitSchema(many=True)

@course_and_units.route('/', methods=['POST'])
def create_course():
    data = request.get_json()
    name  = data.get('name')
    code = data.get('code')
    years_studied = data.get('years_studied')
    
