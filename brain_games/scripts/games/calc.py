from random import randrange
from random import choice
from brain_games.scripts.vars_const import RULES_CALC


def run_game():
    print(RULES_CALC)
    a, b, exp = randrange(10), randrange(10), choice(['+', '-', '*'])
    print(f'Question: {a} {exp} {b}')
    return str(eval(f'{a} {exp} {b}'))
