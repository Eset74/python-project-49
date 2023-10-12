from random import randrange
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_data():
    rand_num = randrange(100)
    print(f'Question: {rand_num}')
    return 'yes' if rand_num % 2 == 0 else 'no'
