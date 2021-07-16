from flask import render_template, request, Blueprint, redirect, url_for, flash
from quiz_app.questions.question_types.question_generator import generate_two_number_addition_or_subtraction_question
from quiz_app.student.forms import EnterQuiz
from quiz_app import db
from quiz_app.models import Quiz, User

student = Blueprint('student', __name__)


@student.route('/student_landing', methods=['GET', 'POST'])
def student_landing():
    name = None
    quiz_id = None
    form = EnterQuiz()
    if form.validate_on_submit():
        name = form.name.data
        quiz_id = form.quiz_id.data

        # Check if quiz exists
        try:
            db.session.query(Quiz).filter_by(quiz_id=quiz_id).one()
        except:
            flash("Quiz ID not found")
            return redirect(url_for('student.student_landing'))

        user = User(quiz_id=quiz_id, user_name=name)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('student.student_quiz_lobby'))

    return render_template('student_landing.html', form=form, name=name)


@student.route('/student_quiz_lobby')
def student_quiz_lobby():
    return render_template('student_quiz_lobby.html')


@student.route('/question')
def question():
    question_data = generate_two_number_addition_or_subtraction_question('addition')
    return render_template('question.html',
                           question=question_data['question_string'],
                           answers=question_data['all_answers'],
                           title='Addition Quiz')
