from flask import render_template, request, Blueprint

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/index')
@main.route('/home')
def home():
    return render_template('home.html', title='Welcome')


@main.route("/about")
def about():
    return render_template('about.html', title='About')