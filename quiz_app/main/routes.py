from flask import render_template, request, Blueprint
from quiz_app.questions.question_types.question_generator import generate_two_number_addition_or_subtraction_question
from flask_babel import gettext

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/index')
@main.route('/home')
def index():
    return render_template('home.html')


@main.route("/about")
def about():
    print(gettext('Hello World'))
    return render_template('about.html', title=gettext('About'))
