import numpy
import random

class Question():
    def __init__(self, seed=0, language='en'):
        self._seed = seed
        random.seed(seed)
        numpy.random.seed(seed)
        print(random.random())
        print(numpy.random.randint(0, 100))

        self.language = language

    def render(self):
        pass
