from random import randrange
from brain_games.scripts.vars_const import RULES_EVEN


def run_game():
    print(RULES_EVEN)
    rand_num = randrange(100)
    print(f'Question: {rand_num}')
    return 'yes' if rand_num % 2 == 0 else 'no'
