import json
import uuid

from flask import render_template, request, Blueprint
from quiz_app.quiz.forms import GenerateQuizForm
from quiz_app.models import Question, Quiz
from quiz_app import db
from quiz_app.questions.question_types.utils.registry import QuestionRegistry
quiz = Blueprint('quiz', __name__)


@quiz.route('/')
@quiz.route('/index')
@quiz.route('/home')
def home():
    return render_template('home.html', title='Welcome')


@quiz.route('/create_quiz', methods=['GET', 'POST'])
def create_quiz():
    topic = False
    form = GenerateQuizForm()

    if form.validate_on_submit():
        topic = form.topic.data
        # teacher submits form
        # create quiz (mock it for now)
        # insert all quiz components into database
        question_registry = QuestionRegistry()
        questions = question_registry.generate_questions(10, seed=0)
        correct_answer_indices = [question['correct_answer_index'] for question in questions]
        json_questions = [json.dumps(question) for question in questions]

        # Add to db
        # Add quiz
        quiz_uid = uuid.uuid4()
        quiz = Quiz(quiz_uid=quiz_uid)
        db.session.add(quiz)
        quiz_id = db.session.query(Quiz).filter_by(quiz_uid=quiz_uid)
        i = 0
        for correct_answer_index, question_json in zip(correct_answer_indices, json_questions):
            question = Question(quiz_id=quiz_id,
                                question_json=question_json,
                                correct_answer_index=correct_answer_index,
                                question_number=i)
            db.session.add(question)
            i += 1

    return render_template('create_quiz.html', form=form, topic=topic)
