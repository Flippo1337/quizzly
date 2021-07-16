import random

from questions.math_questions.sample_questions import PolinomialPlot, QuadraticEqNumberOfRoots

class QuestionRegistry:
    def __init__(self):
        self.available_questions = [PolinomialPlot, QuadraticEqNumberOfRoots]

        self.tags_by_question = {question: question.tags for question in self.available_questions}

    def generate_questions(self, n=10, tag_filter=None):
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
        seeds = [random.random() for _ in range(n)]
        for ii, seed in enumerate(seeds):
            question_class = random.choice(filtered_questions)
            q = question_class(seed=seed)
            questions.append(q.generate())

        return questions



if __name__ == '__main__':
    registry = QuestionRegistry()
    questions = QuestionRegistry.generate_questions(10)
    print(questions)