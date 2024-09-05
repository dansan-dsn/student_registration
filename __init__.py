from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)

    # Configuration
    basedir = os.path.abspath(os.path.dirname(__file__))    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'student.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)

    # Import and register blueprints
    from .student_blueprint import student
    app.register_blueprint(student, url_prefix='/student')

    return app
