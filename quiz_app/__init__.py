from flask import Flask, request, g
from flask_sqlalchemy import SQLAlchemy
from quiz_app.config import Config
from flask_babel import Babel



db = SQLAlchemy()




def create_app(config_class=Config):


    app = Flask(__name__)
    app.config['SECRET_KEY'] = Config.SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)
    app.config.from_object(config_class)
    babel = Babel(app)

    @babel.localeselector
    def get_locale():
        # if a user is logged in, use the locale from the user settings
        # user = getattr(g, 'user', None)
        # if user is not None:
        #     return user.locale
        # otherwise try to guess the language from the user accept
        # header the browser transmits.  We support de/fr/en in this
        # example.  The best match wins.
        return request.accept_languages.best_match(['de', 'fr', 'en'])


    from quiz_app.main.routes import main
    from quiz_app.questions.routes import questions
    from quiz_app.quiz.routes import quiz
    from quiz_app.student.routes import student
    app.register_blueprint(main)
    app.register_blueprint(questions)
    app.register_blueprint(quiz)
    app.register_blueprint(student)
    return app
