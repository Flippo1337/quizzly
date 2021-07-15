from flask import Flask, render_template
from question_generator import generate_two_number_addition_or_subtraction_question

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')


@app.route('/quiz/addition')
def addition_quiz():
    question_data = generate_two_number_addition_or_subtraction_question('addition')
    return render_template('quiz.html',
                           question=question_data['question_string'],
                           answers=question_data['all_answers'],
                           title='Addition Quiz')


@app.route('/quiz/subtraction')
def subtraction_quiz():
    question_data = generate_two_number_addition_or_subtraction_question('subtraction')
    return render_template('quiz.html',
                           question=question_data['question_string'],
                           answers=question_data['all_answers'],
                           title='Subtration Quiz')


if __name__ == '__main__':
    app.run(debug=True, port=81, host='0.0.0.0')
