from random import randrange
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(rand_num):
    return rand_num % 2 == 0


def generate_data():
    rand_num = randrange(100)

    return (f'Question: {rand_num}', 'yes') if is_even(rand_num) else (f'Question: {rand_num}', 'no')
