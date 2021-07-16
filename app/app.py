from flask import Flask, render_template, Response
import random
import base64
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import gettext
el = gettext.translation('base', localedir='../locales', languages=['de'])
el.install('base')
# _ = el.gettext


from question_generator import generate_two_number_addition_or_subtraction_question
from questions.math_questions.sample_questions import QuadraticEqNumberOfRoots, PolinomialPlot



print(_(f'What function is plotted here?'))


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/quiz/addition')
def addition_quiz():
    question_data = generate_two_number_addition_or_subtraction_question('addition')
    return render_template('quiz.html', question=question_data['question_string'],
                           answers=question_data['all_answers'])


@app.route('/quiz/subtraction')
def subtraction_quiz():
    question_data = generate_two_number_addition_or_subtraction_question('subtraction')
    return render_template('quiz.html', question=question_data['question_string'],
                           answers=question_data['all_answers'])

@app.route('/quiz/quadratic')
def quadratic_quiz():

    q = QuadraticEqNumberOfRoots(random.randint(0, 2 ** 10))
    question_data = q.generate()
    all_answers = question_data['wrong_answers']+[question_data['correct_answer']]

    return render_template('quiz.html', question=question_data['question'],
                           answers=all_answers)

@app.route('/quiz/plot')
def plot_quiz():

    q = PolinomialPlot(random.randint(0, 2 ** 10))
    question_data = q.generate()
    all_answers = question_data['wrong_answers']+[question_data['correct_answer']]
    if 'figure' in question_data:
        # Generate plot
        # fig = Figure()
        # axis = fig.add_subplot(1, 1, 1)
        # axis.set_title("title")
        # axis.set_xlabel("x-axis")
        # axis.set_ylabel("y-axis")
        # axis.grid()
        # axis.plot(range(5), range(5), "ro-")




        # Convert plot to PNG image
        png = io.BytesIO()
        FigureCanvas(question_data['figure']).print_png(png)

        # Encode PNG image to base64 string
        png_str = "data:image/png;base64,"
        png_str += base64.b64encode(png.getvalue()).decode('utf8')

        return render_template('quiz.html', question=question_data['question'],
                               answers=all_answers, image=png_str)
    else:
        return render_template('quiz.html', question=question_data['question'],
                               answers=all_answers)





@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
