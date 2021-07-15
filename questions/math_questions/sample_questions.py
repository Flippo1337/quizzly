from questions.question import Question
import random

class Multiplication(Question):
    def __init__(self, seed=0, language='en', upper_bound=10, lower_bound=0):
        super().__init__(seed=seed, language=language)
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound

    def render(self):
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

        return question, correct_answer, wrong_answers


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
    q = Multiplication(1)
    print(q.render())
    Playground()

