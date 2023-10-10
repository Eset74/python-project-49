from random import randrange
from random import choice


def run_game():
    a, b, exp = randrange(10), randrange(10), choice(['+', '-', '*'])
    print(f'Question: {a} {exp} {b}')
    return eval(f'{a} {exp} {b}')
