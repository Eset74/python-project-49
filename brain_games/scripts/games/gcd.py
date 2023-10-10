from random import randrange
from brain_games.scripts.vars_const import RULES_GCD


def run_game():
    print(RULES_GCD)
    a, b = randrange(1, 100), randrange(1, 100)

    print(f'Question: {a} {b}')
    max_ab = max(a, b)
    min_ab = min(a, b)

    for i in range(max_ab, 0, -1):
        if abs(max_ab) % i == 0 and abs(min_ab) % i == 0:
            return str(i)
