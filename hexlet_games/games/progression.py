from random import randrange
RULES = 'What number is missing in the progression?'


def generate_data():
    arithmetic_progression = []

    start_num = randrange(100)  # Start number of arithmetic progression
    step = randrange(1, 10)  # Step of progression
    random_index = randrange(1, 10)  # Random num to hide the field progression

    for i in range(10):
        arithmetic_progression.append(start_num + step)
        start_num += step
    corr_answer = str(arithmetic_progression[random_index])
    arithmetic_progression[random_index] = '..'

    return f'{" ".join(map(str, arithmetic_progression))}', corr_answer
