from random import randrange
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_data():
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
