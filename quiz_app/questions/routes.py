from flask import render_template, Blueprint
from quiz_app.questions.question_types.math_questions.sample_questions import QuadraticEqNumberOfRoots
import random

questions = Blueprint('questions', __name__)


@questions.route('/question')
def question():
    q = QuadraticEqNumberOfRoots(random.randint(0, 2 ** 10))
    question, correct_answer, wrong_answers = q.render()

    return render_template('question.html', title='Welcome', question=question, correct_answer=correct_answer, wrong_answers=wrong_answers)


