from datetime import datetime
from quiz_app import db


# MODELS
class Quiz(db.Model):
    __tablename__ = 'quiz'

    quiz_id = db.Column(db.Integer, primary_key=True)
    quiz_uid = db.Column(db.String)

    def __init__(self, quiz_uid):
        self.quiz_uid = quiz_uid


class Question(db.Model):
    __tablename__ = 'question'

    question_id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.quiz_id'))
    question_number = db.Column(db.Integer)
    question_json = db.Column(db.String)
    correct_answer_index = db.Column(db.Integer)
    quiz = db.relationship('Quiz', backref='questions', lazy=True)

    def __init__(self, quiz_id, question_number, question_json, correct_answer_index):
        self.quiz_id = quiz_id
        self.question_number = question_number
        self.question_json = question_json
        self.correct_answer_index = correct_answer_index


class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.quiz_id'))
    user_name = db.Column(db.String)


class Answer(db.Model):
    __tablename__ = 'answer'

    answer_id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Text, db.ForeignKey('question.question_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    answer = db.Column(db.Text)
    question = db.relationship('Question', backref='answers', lazy=True)
    user = db.relationship('User', backref='answers', lazy=True)