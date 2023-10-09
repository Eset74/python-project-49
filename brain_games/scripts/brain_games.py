#!/usr/bin/env/python3
from brain_games.scripts.vars_const import *
# from brain_games.cli import welcome_user
from random import randrange
from random import choice
import prompt


def welcome_user(game):
    user = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {user}!')

    match game:
        case 'Even':
            print(RULES_EVEN)
        case 'Calc':
            print(RULES_CALC)
        case 'Gcd':
            print(RULES_GCD)
        case 'Progression':
            print(RULES_PROGRESSION)
        case 'Prime':
            print(RULES_PRIME)

    return user


def launch_even():
    rand_num = randrange(100)
    print(f'Question: {rand_num}')
    return 'yes' if rand_num % 2 == 0 else 'no'


def launch_calc():
    a, b, exp = randrange(10), randrange(10), choice(['+', '-', '*'])
    print(f'Question: {a} {exp} {b}')
    return eval(f'{a} {exp} {b}')


def launch_gcd():
    a, b = randrange(1, 100), randrange(1, 100)

    print(f'Question: {a} {b}')
    max_ab = max(a, b)
    min_ab = min(a, b)

    for i in range(max_ab, 0, -1):
        if abs(max_ab) % i == 0 and abs(min_ab) % i == 0:
            return i


def launch_progression():
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


def launch_prime():
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


def show_question(game):
    match game:

        case 'Even':

            return launch_even()

        case 'Calc':

            return launch_calc()

        case 'Gcd':

            return launch_gcd()

        case 'Progression':

            return launch_progression()

        case 'Prime':

            return launch_prime()


def get_user_answer(game):
    match game:
        case 'Even' | 'Prime':
            return prompt.string('Your answer: ').lower()
        case 'Calc' | 'Gcd' | 'Progression':
            return prompt.integer('Your answer: ')


def is_equal_answers(user_answer, corr_answer, user):
    if user_answer == corr_answer:
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{corr_answer}'")
        print(f"Let's try again, {user}!")
        return False


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

if __name__ == '__main__':
    main()
