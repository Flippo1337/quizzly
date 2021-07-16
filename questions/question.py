import numpy
import random
from collections.abc import Iterable
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import base64

class Question:
    tags = set()

    def __init__(self, seed=0, language='en'):
        self._seed = seed
        random.seed(seed)
        numpy.random.seed(seed)
        self.language = language


    def generate(self):
        pass

    def render(self):
        question_data = self.generate()
        if 'figure' in question_data:
            png = io.BytesIO()
            FigureCanvas(question_data['figure']).print_png(png)

            # Encode PNG image to base64 string
            png_str = "data:image/png;base64,"
            png_str += base64.b64encode(png.getvalue()).decode('utf8')
            question_data['figure_png'] = png_str
            del question_data['figure']
        return question_data

    def randint(self, lower_bound, upper_bound, exclude=None):
        # TODO: not a very efficient implementation
        if exclude is None:
            return random.randint(lower_bound, upper_bound)
        else:
            if not isinstance(exclude, Iterable):
                exclude = (exclude, )
            return random.choice(list(set(range(lower_bound, upper_bound+1))-set(exclude)))



