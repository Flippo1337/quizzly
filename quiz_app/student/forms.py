from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class EnterQuiz(FlaskForm):
    name = StringField("Username:")
    quiz_id = StringField("Quiz ID: ")
    submit = SubmitField('Submit')
