from random import randrange
RULES = 'Find the greatest common divisor of given numbers.'


def get_gcd(a, b):
    max_ab = max(a, b)
    min_ab = min(a, b)

    for i in range(max_ab, 0, -1):
        if abs(max_ab) % i == 0 and abs(min_ab) % i == 0:
            return i


def generate_data():
    a, b = randrange(1, 100), randrange(1, 100)
    question = f'Question: {a} {b}'
    corr_answer = str(get_gcd(a, b))
    return question, corr_answer
