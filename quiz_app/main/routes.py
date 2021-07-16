from flask import render_template, request, Blueprint
from quiz_app.questions.question_types.question_generator import generate_two_number_addition_or_subtraction_question

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/index')
@main.route('/home')
def index():
    return render_template('home.html')


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route('/teacher-login')
def teacher_login():
    return render_template('teacherlogin.html')
