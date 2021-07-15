from flask import Flask
from quiz_app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    #
    # db.init_app(quiz_app)
    # bcrypt.init_app(quiz_app)
    # login_manager.init_app(quiz_app)
    # mail.init_app(quiz_app)
    #
    # from flaskblog.users.routes import users
    # from flaskblog.posts.routes import posts
    # from flaskblog.main.routes import main
    from quiz_app.main.routes import main
    from quiz_app.questions.routes import questions
    app.register_blueprint(main)
    app.register_blueprint(questions)
    return app