from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField


# FORMS for quiz creation. PLACEHOLDER FOR NOW, MVP is student UI
class GenerateQuizForm(FlaskForm):
    submit = SubmitField('Submit')
