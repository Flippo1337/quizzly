from flask import Flask
from quiz_app.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from quiz_app.main.routes import main
    from quiz_app.questions.routes import questions
    from quiz_app.teacher.routes import teacher
    from quiz_app.student.routes import student
    app.register_blueprint(main)
    app.register_blueprint(questions)
    app.register_blueprint(teacher)
    app.register_blueprint(student)
    return app