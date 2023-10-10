from random import randrange
from brain_games.scripts.vars_const import RULES_PRIME

def run_game():
    print(RULES_PRIME)
    result = False
    rand_num = randrange(100)
    print(f'Question: {rand_num}')

    if rand_num > 1:
        for i in range(2, rand_num):
            if (rand_num % i) == 0:
                break
        else:
            result = True

    return 'yes' if result else 'no'
