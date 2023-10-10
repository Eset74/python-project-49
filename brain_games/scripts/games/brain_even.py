from random import randrange


def run_game():
    rand_num = randrange(100)
    print(f'Question: {rand_num}')
    return 'yes' if rand_num % 2 == 0 else 'no'
