from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from quiz_app.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = Config.SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
    db = SQLAlchemy(app)
    db.create_all()
    app.config.from_object(config_class)

    from quiz_app.main.routes import main
    from quiz_app.questions.routes import questions
    from quiz_app.teacher.routes import teacher
    from quiz_app.student.routes import student
    app.register_blueprint(main)
    app.register_blueprint(questions)
    app.register_blueprint(teacher)
    app.register_blueprint(student)
    return app, db