import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

from quiz_app.questions.question_types.utils.question import Question


import gettext
try:
    _("")
except:
    _ = gettext.gettext

print(_("hu"))

class Multiplication(Question):
    tags = ('multiplication')
    def __init__(self, seed=0, lower_bound=0, upper_bound=10):
        super().__init__(seed=seed)
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound

    def generate(self):
        a = random.randint(self.lower_bound, self.upper_bound + 1)
        b = random.randint(self.lower_bound, self.upper_bound + 1)

        question = f'What is {a} * {b} ?'

        correct_answer = a * b
        wrong_answers = []

        while len(wrong_answers) < 3:
            x = random.randint(self.lower_bound, self.upper_bound + 1)
            y = random.randint(self.lower_bound, self.upper_bound + 1)

            if x * y != correct_answer and x * y not in wrong_answers:
                wrong_answers.append(x * y)

        all_answers = wrong_answers + [correct_answer]
        correct_answer_index = 3

        response = {'question_string': question, 'all_answers': all_answers, 'correct_answer_index': correct_answer_index}
        return response


class QuadraticEqNumberOfRoots(Question):
    tags = ('quadratic', 'roots')
    def __init__(self, seed=0, lower_bound=-10, upper_bound=10):
        super().__init__(seed=seed)
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound


    def generate(self):
        # with a 1/3 chance pick an equation that has only 1 root
        if random.random() < 1/3:
            root = self.randint(-3, 3+1)
            r = self.randint(-5, 5+1, exclude=0)
            a = r
            b = -r * 2 * root
            c = r * root ** 2

        # else use a random equation
        else:
            a = self.randint(self.lower_bound, self.upper_bound + 1, exclude=[0])
            b = self.randint(self.lower_bound, self.upper_bound + 1)
            c = self.randint(self.lower_bound, self.upper_bound + 1)

        question = f'What is the number of real roots of this equation? $${a}x^2+{b}x+{c}$$'

        discriminant = b**2-4*a*c
        if discriminant == 0:
            correct_answer = 1
        elif discriminant > 0:
            correct_answer = 2
        else:
            correct_answer = 0

        all_answers = [0, 1, 2, 3]
        correct_answer_index = all_answers.index(correct_answer)




        response = {'question_string': question, 'all_answers': all_answers, 'correct_answer_index': correct_answer_index}
        return response

class LinearEquationsPlot(Question):
    tags = ('linear', 'plot')

    def __init__(self, seed=0, language='en', lower_bound=-10, upper_bound=10):
        super().__init__(seed=seed)
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound



    def generate(self):

        question = _(f'What function is plotted here?')

        parameters = []
        while len(parameters) < 4:
            params = tuple(np.random.randint(-10, 10, size=2))
            if params not in parameters:
                parameters.append(params)


        random.shuffle(parameters)


        correct_answer = f'$${parameters[0][0]}x {"+ " if parameters[0][1]>=0 else ""}{parameters[0][1]}$$'

        wrong_answers = [f'$${parameters[ii][0]}x {"+ " if parameters[ii][1]>=0 else ""}{parameters[ii][1]}$$' for ii in range(1,4)]

        all_answers = wrong_answers + [correct_answer]
        correct_answer_index = 3

        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        x = np.linspace(-1, 1)
        y = parameters[0][0] * x + parameters[0][1]
        axis.plot(x, y)
        axis.grid()


        response = {'question_string': question, 'all_answers': all_answers, 'correct_answer_index': correct_answer_index, 'figure': fig}
        return response



def Playground():
    try:
        from StringIO import StringIO as BytesIO
    except ImportError:
        from io import BytesIO

    import matplotlib.pyplot as plt

    def render_latex(formula, fontsize=12, dpi=300, format_='svg'):
        """Renders LaTeX formula into image."""
        fig = plt.figure()
        text = fig.text(0, 0, formula, fontsize=fontsize)

        fig.savefig('formula.png', dpi=dpi)  # triggers rendering

        bbox = text.get_window_extent()
        width, height = bbox.size / float(dpi) + 0.05
        fig.set_size_inches((width, height))

        dy = (bbox.ymin / float(dpi)) / height
        text.set_position((0, -dy))

        buffer_ = BytesIO()
        fig.savefig('formula.png', dpi=dpi, transparent=True, format=format_)
        plt.close(fig)
        buffer_.seek(0)

        return buffer_


    image_bytes = render_latex(r'a^b and $\alpha > \beta$', format_='png')
    # with open('formula.png', 'wb') as image_file:
    #     image_file.write(image_bytes)


if __name__ == '__main__':
    q = LinearEquationsPlot(1)
    print(q.render())

    # q = QuadraticEqNumberOfRoots()
    # print(q.generate())

    # Playground()

