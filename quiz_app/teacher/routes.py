from flask import render_template, request, Blueprint
from quiz_app.teacher.forms import GenerateQuizForm
from quiz_app.models import Quiz
from quiz_app import db
teacher = Blueprint('teacher', __name__)


@teacher.route('/')
@teacher.route('/index')
@teacher.route('/home')
def home():
    return render_template('home.html', title='Welcome')


@teacher.route('/teacher_landing', methods=['GET', 'POST'])
def teacher_landing():
    topic = False
    form = GenerateQuizForm()

    if form.validate_on_submit():
        topic = form.topic.data
        quiz = Quiz(topic=topic)

        # Generate questions and answer for given submission
        db.session.add(quiz)
        db.session.commit()

    return render_template('teacher_landing.html', form=form, topic=topic)
