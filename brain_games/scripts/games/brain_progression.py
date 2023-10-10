from random import randrange


def run_game():
    arithmetic_list = []

    start_int = randrange(100)  # Start number of arithmetic progression
    step_int = randrange(1, 10)  # Step of progression
    hide_num = randrange(1, 10)  # Random num to hide the field progression

    for i in range(10):
        arithmetic_list.append(start_int + step_int)
        start_int += step_int

    corr_answer = arithmetic_list[hide_num]
    arithmetic_list[hide_num] = '..'
    print(f'Question: {" ".join(map(str, arithmetic_list))}')
    return corr_answer
