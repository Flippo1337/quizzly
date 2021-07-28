import pandas as pd
from flask import render_template, request, Blueprint, redirect, url_for, flash, session
import json

from quiz_app.questions.question_types.question_generator import generate_two_number_addition_or_subtraction_question
from quiz_app.student.forms import EnterQuiz, Lobby
from quiz_app import db
from quiz_app.models import Quiz, User, Answer, Question

student = Blueprint('student', __name__)


@student.route('/student_landing', methods=['GET', 'POST'])
def student_landing():
    name = None
    quiz_id = request.args.get('quiz_id')
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
        session['quiz_id'] = quiz_id
        session['username'] = name
        return redirect(url_for('student.student_quiz_lobby'))

    form.quiz_id.data = quiz_id
    return render_template('student_landing.html', form=form, name=name)


@student.route('/student_quiz_lobby', methods=['GET', 'POST'])
def student_quiz_lobby():

    form = Lobby()
    if form.validate_on_submit():
        return redirect(url_for('student.question'))

    return render_template('student_quiz_lobby.html', form=form)


@student.route('/question', methods=['GET', 'POST'])
def question():
    quiz_id = session['quiz_id']
    username = session['username']
    user = db.session.query(User).filter_by(quiz_id=quiz_id, user_name=username).all()
    user = user[0]
    # TODO: make sure we only have one user and identify by id (in session?)

    if request.method == 'POST':
        answer_index = int(request.values.get('answer_index'))
        question_id = request.values.get('question_id')
        answer = Answer(user=user, question_id=question_id, answer_index=answer_index)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('student.quiz_results'))


    answers = user.answers
    if len(answers) > 0:
        current_question_index = max([answer.question.question_number for answer in answers]) + 1
    else:
        current_question_index = 0

    current_question = db.session.query(Question).filter_by(quiz_id=quiz_id, question_number=current_question_index).one()

    n_questions = db.session.query(Question).filter_by(quiz_id=quiz_id).count()

    question_data = json.loads(current_question.question_json)

    if 'figure_png' in question_data:
        optional_arguments = {'figure_png': question_data['figure_png']}
    else:
        optional_arguments ={}

    return render_template('question.html',
                           question_id=current_question.question_id,
                           question_index=current_question_index,
                           n_questions=n_questions,
                           question=question_data['question_string'],
                           answers=question_data['all_answers'],
                           title='TODO: add question title',
                           **optional_arguments)


@student.route('/quiz_results')
def quiz_results():
    quiz_id = session['quiz_id']
    username = session['username']
    user = db.session.query(User).filter_by(quiz_id=quiz_id, user_name=username).all()
    user = user[0]
    user_id = user.user_id

    answers = db.session.query(Answer).filter_by(user_id=user_id).join(Question).filter_by(quiz_id=quiz_id).\
        order_by(Question.question_number.desc()).all()

    answered_correctly = answers[0].question.correct_answer_index == answers[0].answer_index
    score = {}

    for answer in answers:
        score[answer.question.question_number] = (answer.question.correct_answer_index == answer.answer_index)

    print(score)
    df = pd.DataFrame(data=score.items())

    users = db.session.query(User).filter_by(quiz_id=quiz_id).all()



    # temp to show example - would need dynamic update
    question_data = generate_two_number_addition_or_subtraction_question('addition')
    return render_template('quiz_results.html',
                           question=question_data['question_string'],
                           correct_answer=question_data['correct_answer'],
                           answered_correctly=answered_correctly,
                           table=df.to_html())
