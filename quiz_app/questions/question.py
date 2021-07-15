import numpy
import random
from collections.abc import Iterable

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

    def randint(self, lower_bound, upper_bound, exclude=None):
        # TODO: not a very efficient implementation
        if exclude is None:
            return random.randint(lower_bound, upper_bound)
        else:
            if not isinstance(exclude, Iterable):
                exclude = (exclude, )
            return random.choice(list(set(range(lower_bound, upper_bound+1))-set(exclude)))

