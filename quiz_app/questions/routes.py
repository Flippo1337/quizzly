from flask import render_template, Blueprint
from quiz_app.questions.question_types.question_generator import generate_two_number_addition_or_subtraction_question
import random

questions = Blueprint('questions', __name__)


@questions.route('/addition')
def addition_quiz():
    question_data = generate_two_number_addition_or_subtraction_question('addition')
    return render_template('question.html', question=question_data['question_string'],
                           answers=question_data['all_answers'])


@questions.route('/subtraction')
def subtraction_quiz():
    question_data = generate_two_number_addition_or_subtraction_question('subtraction')
    return render_template('question.html', question=question_data['question_string'],
                           answers=question_data['all_answers'])



