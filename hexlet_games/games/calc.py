from random import choice
from random import randrange

RULES = 'What is the result of the expression?'


def generate_data():
    result = ''
    a, b, exp = randrange(10), randrange(10), choice(['+', '-', '*'])

    match exp:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b

    return f'{a} {exp} {b}', str(result)
