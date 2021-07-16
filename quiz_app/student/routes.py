from flask import render_template, request, Blueprint
from quiz_app.questions.question_types.question_generator import generate_two_number_addition_or_subtraction_question
from quiz_app.student.forms import EnterQuiz

student = Blueprint('student', __name__)



@student.route('/student_landing', methods=['GET', 'POST'])
def student_landing():
    name = None
    quiz_id = None
    form = EnterQuiz()
    if form.validate_on_submit():
        name = form.topic.data
        quiz_id = form.quiz_id.data

    return render_template('student_landing.html', form=form, name=name)


@student.route('/question')
def question():
    question_data = generate_two_number_addition_or_subtraction_question('addition')
    return render_template('question.html',
                           question=question_data['question_string'],
                           answers=question_data['all_answers'],
                           title='Addition Quiz')
