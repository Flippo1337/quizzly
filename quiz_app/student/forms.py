from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class EnterQuiz(FlaskForm):
    name = StringField("Name:")
    quiz_id = StringField("Quiz ID: ")
    submit = SubmitField('Submit')
