#!/usr/bin/env/python3
from brain_games.scripts.vars_const import *
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
    return user


def show_question(game):
    match game:

        case 'Even':
            rand_num = randrange(100)
            print(f'Question: {rand_num}')
            return 'yes' if rand_num % 2 == 0 else 'no'

        case 'Calc':
            a, b, exp = randrange(10), randrange(10), choice(['+', '-', '*'])
            print(f'Question: {a} {exp} {b}')
            return eval(f'{a} {exp} {b}')

        case 'Gcd':
            a, b = randrange(1, 100), randrange(1, 100)

            print(f'Question: {a} {b}')
            max_ab = max(a, b)
            min_ab = min(a, b)

            for i in range(max_ab, 0, -1):
                if abs(max_ab) % i == 0 and abs(min_ab) % i == 0:
                    return i


def get_user_answer(game):
    match game:
        case 'Even':
            return prompt.string('Your answer: ').lower()
        case 'Calc':
            return prompt.integer('Your answer: ')
        case 'Gcd':
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


def is_even(num):
    return num % 2 == 0


def main():
    pass


if __name__ == '__main__':
    main()
