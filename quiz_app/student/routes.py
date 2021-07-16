from flask import render_template, request, Blueprint
from quiz_app.questions.question_types.question_generator import generate_two_number_addition_or_subtraction_question

student = Blueprint('student', __name__)


@student.route('/question')
def question():
    question_data = generate_two_number_addition_or_subtraction_question('addition')
    return render_template('question.html',
                           question=question_data['question_string'],
                           answers=question_data['all_answers'],
                           title='Addition Quiz')
