from random import randrange
RULES = 'What number is missing in the progression?'


def generate_data():
    arithmetic_list = []

    start_num = randrange(100)  # Start number of arithmetic progression
    step = randrange(1, 10)  # Step of progression
    hide_num = randrange(1, 10)  # Random num to hide the field progression

    for i in range(10):
        arithmetic_list.append(start_num + step)
        start_num += step

    arithmetic_list[hide_num] = '..'

    return f'Question: {" ".join(map(str, arithmetic_list))}', str(arithmetic_list[hide_num])
