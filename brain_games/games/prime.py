from random import randrange
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(rand_num):
    if rand_num > 1:
        for i in range(2, rand_num):
            if (rand_num % i) == 0:
                break
        else:
            return True


def generate_data():
    rand_num = randrange(100)
    question = f'Question: {rand_num}'
    return (question, 'yes') if is_prime(rand_num) else (question, 'no')
