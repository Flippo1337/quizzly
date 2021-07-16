from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class EnterQuiz(FlaskForm):
    name = StringField("Username:")
    quiz_id = StringField("Quiz ID: ")
    submit = SubmitField('Submit')

class Lobby(FlaskForm):
    start = SubmitField('Start Quiz')

class Answer(FlaskForm):
    name = StringField("Username:")
    quiz_id = StringField("Quiz ID: ")
    submit = SubmitField('Submit')