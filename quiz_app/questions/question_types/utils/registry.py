import random

from quiz_app.questions.question_types.math_questions.sample_questions import LinearEquationsPlot, QuadraticEqNumberOfRoots

class QuestionRegistry:
    def __init__(self):
        self.available_questions = [LinearEquationsPlot, QuadraticEqNumberOfRoots]

        self.tags_by_question = {question: question.tags for question in self.available_questions}

    def generate_questions(self, n=10, seed=None, tag_filter=None):
        if seed is not None:
            random.seed(seed)
        # generate seeds to pass to questions
        seeds = [random.randint(0, 2 ** 32 - 1) for _ in range(n)]

        if tag_filter is None:
            filtered_questions = self.available_questions
        else:
            filtered_questions = []
            for question in self.available_questions:
                for tag in self.tags_by_question[question]:
                    if tag_filter(tag):
                        filtered_questions.append(question)
                        break

        if len(filtered_questions) == 0:
            raise ValueError('no question class found that match the filter')

        questions = []

        for ii, question_seed in enumerate(seeds):
            question_class = random.choice(filtered_questions)
            q = question_class(seed=question_seed)
            questions.append(q.render())

        return questions



if __name__ == '__main__':
    registry = QuestionRegistry()
    questions = registry.generate_questions(10, seed=0)
    print(questions)

    q = questions[0]

    import pickle
    import json

    sp = pickle.dumps(q)
    len(json.dumps(q))



    print(registry.tags_by_question)