from random import randrange
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_data():
    rand_num = randrange(100)

    return (f'{rand_num}', 'yes') \
        if is_even(rand_num) else (f'{rand_num}', 'no')
