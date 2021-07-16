from flask import render_template, request, Blueprint

teacher = Blueprint('teacher', __name__)


@teacher.route('/')
@teacher.route('/index')
@teacher.route('/home')
def home():
    return render_template('home.html', title='Welcome')
