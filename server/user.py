from flask import Blueprint,request, jsonify
from . import db,ma
from .model import User
import random
from werkzeug.security import generate_password_hash, check_password_hash

user = Blueprint('user',__name__)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

user_schema = UserSchema()
users_schema = UserSchema(many=True)

def generate_user_number(role):
    if role == 'admin':
        code = 'admin' + str(random.randint(1000, 9999))
        print(code)
        return code 
    elif role == 'student':
        return 'stud' + str(random.randint(1000, 9999))
    return None 

@user.route('/new_user', methods=['POST'])
def new_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No Input data"})

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    other_name = data.get('other_name')
    reg_no = data.get('reg_no')
    email  = data.get('email')
    phone_no = data.get('phone_no')
    password = data.get('password')
    role = data.get('role')

    if role not in ['admin', 'student']:
        return jsonify({"error": "Role must be either admin or student"}), 400

    if role == 'admin' and reg_no is not None:
        return jsonify({"error": 'All Admins cannot have reg_no'}), 400
    elif role == 'student' and  reg_no is None:
        return jsonify({"error": "All Students must have reg_no"}), 400
    
    user_number = generate_user_number(role)
    
    if not first_name or not last_name or not other_name or not email or not phone_no or not password or not role:
        return jsonify({'error': 'All fields are required'}), 400
    
    existing_user = User.query.filter_by(reg_no=reg_no).first()
    if existing_user:
        return jsonify({'error': 'Student with the same registration number already exists'}), 401
    
    hashed_password = generate_password_hash(password)
    
    new_user = User(first_name=first_name, last_name=last_name, other_name=other_name, reg_no=reg_no,email=email, phone_no=phone_no, password=hashed_password, role=role, user_no=user_number)

    db.session.add(new_user)
    db.session.commit()
    
    return user_schema.jsonify(new_user), 201

@user.route('/', methods=['GET'])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result), 200

@user.route('/admins', methods=['GET'])
def get_admins():
    all_admins = User.query.filter_by(role='admin')
    result = users_schema.dump(all_admins)
    return jsonify(result), 200

@user.route('/students', methods=['GET'])
def get_students():
    all_students = User.query.filter_by(role='student')
    result = users_schema.dump(all_students)
    return jsonify(result), 200

@user.route('/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'msg': 'User not found'}), 404
    
    return user_schema.jsonify(user)

@user.route('/update/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found "}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data to update"}), 400

    if 'first_name' in data:
        user.first_name = data['first_name']
    if 'last_name' in data:
        user.last_name = data['last_name']
    if 'other_name' in data:
        user.other_name = data['other_name']
    if 'reg_no' in data:
        user.reg_no = data['reg_no']
    if 'email' in data:
        user.email = data['email']
    if 'phone_no' in data:
        user.phone_no = data['phone_no']
    
    db.session.commit()

    return user_schema.jsonify(user), 200

@user.route('/forgot_password', methods=['POST'])
def forgot_password():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input found"}), 400
    password = data.get('password')
    user_no = data.get('user_no')

    user = User.query.filter_by(user_no=user_no).first()
    if not user:
        return jsonify({"error": "user not found"}), 404
    
    hashed_password = generate_password_hash(password)
    user.password = hashed_password
    db.session.commit()

    return jsonify({"success": f"Password for {user_no} changed successfully"}), 200

@user.route('/remove/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"})
    db.session.delete(user)
    db.session.commit()

    return jsonify({"msg": f"User {id} deleted successfully"}), 200

@user.route('/login', methods=['POST'])
def login(): 
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
 
    user = User.query.filter_by(user_no=username).first()
    if not user:
            return jsonify({"error": "User does not exist"}), 404
    
    is_a_match = check_password_hash(user.password, password)
    if not is_a_match:
        return jsonify({"error": "Password does not match"}), 401
    
    return jsonify({'success': f'User {username} logged in successfully'}), 200