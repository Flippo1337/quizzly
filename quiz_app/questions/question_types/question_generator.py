import random


def generate_two_number_addition_or_subtraction_question(operator):
    """Generates a summation question"""
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    if operator == 'addition':
        correct_answer = a + b
        string_operator = '+'
    elif operator == 'subtraction':
        correct_answer = a - b
        string_operator = '-'
    else:
        raise ValueError("type argument must be 'addition' or 'subtraction'")

    incorrect_answers = [correct_answer + n for n in random.sample([i for i in range(-50, 50) if i != 0], 3)]
    return {'a': a,
            'b': b,
            'correct_answer': correct_answer,
            'incorrect_answers': incorrect_answers,
            'all_answers': incorrect_answers + [correct_answer],
            'question_string': f'{a} {string_operator} {b} ='}