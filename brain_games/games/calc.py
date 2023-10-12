from random import randrange
from random import choice


RULES = 'What is the result of the expression?'


def generate_data():

    a, b, exp = randrange(10), randrange(10), choice(['+', '-', '*'])
    question = f'Question: {a} {exp} {b}'

    match exp:
        case '+':
            result = str(a + b)
        case '-':
            result = str(a - b)
        case '*':
            result = str(a * b)

    return question, result
