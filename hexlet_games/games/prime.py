
from random import randrange

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(rand_num):
    # Мой вариант мне хотя бы логично понятен,
    # и выполняется по скорости на 30% и выше % быстрее предложенного вами
    # Замерял таймером. Хотелось бы обоснования,
    # почему именно предложенный вами вариант является лучше написанного?
    # Только из-за количества итераций цикла?

    # if rand_num > 1:
    #     for i in range(2, rand_num):
    #         if (rand_num % i) == 0:
    #             break
    #     else:
    #         return True

    if rand_num <= 1:
        return False
    for i in range(2, int(rand_num ** 0.5) + 1):
        if rand_num % i == 0:
            return False
    return True


def generate_data():
    rand_num = randrange(100)
    return (f'Question: {rand_num}', 'yes') if is_prime(rand_num) else (f'Question: {rand_num}', 'no')
