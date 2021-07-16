from datetime import datetime
from quiz_app import db


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
