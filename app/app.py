import os
from datetime import datetime

from flask import Flask, render_template
from question_generator import generate_two_number_addition_or_subtraction_question
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, SubmitField
from wtforms.validators import DataRequired, NumberRange


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# FORMS
class GenerateQuizForm(FlaskForm):
    topic = RadioField("Choose topic:", choices=[('addition', 'Addition'), ('subtraction', 'Subtraction')])
    submit = SubmitField('Submit')


# MODELS
class Quiz(db.Model):
    __tablename__ = 'quiz'

    quiz_id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.Text)
    creation_datetime = db.Column(db.DateTime)

    def __init__(self, topic):
        self.topic = topic
        self.creation_datetime = datetime.utcnow()


class Question(db.Model):
    __tablename__ = 'question'

    question_id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Text, db.ForeignKey('quiz.quiz_id'))
    question_string = db.Column(db.Text)
    quiz = db.relationship('Quiz', backref='question', lazy=True)

    def __init__(self, quiz_id, question_string):
        self.quiz_id = quiz_id
        self.question_string = question_string


class Answer(db.Model):
    __tablename__ = 'answer'

    answer_id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Text, db.ForeignKey('question.question_id'))
    answer = db.Column(db.Text)
    question = db.relationship('Question', backref='answer', lazy=True)


# Create database
db.create_all()

# ROUTES
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/student_welcome')
def student_welcome():
    return render_template('student_welcome.html')


@app.route('/teacher_welcome', methods=['GET', 'POST'])
def teacher_welcome():
    topic = False
    form = GenerateQuizForm()

    if form.validate_on_submit():
        topic = form.topic.data
        quiz = Quiz(topic=topic)

        # Generate questions and answer for given submission
        db.session.add(quiz)
        db.session.commit()

    return render_template('teacher_welcome.html', form=form, topic=topic)


@app.route('/quiz/addition')
def addition_quiz():
    question_data = generate_two_number_addition_or_subtraction_question('addition')
    return render_template('quiz.html', question=question_data['question_string'],
                           answers=question_data['all_answers'])


@app.route('/quiz/subtraction')
def subtraction_quiz():
    question_data = generate_two_number_addition_or_subtraction_question('subtraction')
    return render_template('quiz.html', question=question_data['question_string'],
                           answers=question_data['all_answers'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8052)
