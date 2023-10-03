from brain_games.scripts.vars_const import CHANCES
from brain_games.scripts.vars_const import RULES
from random import randrange
import prompt

def is_even(num):
    return num % 2 == 0


def print_random_num():
    rand_num = randrange(100)
    print(f'Question: {rand_num}')
    return rand_num


def get_user_answer():
    return prompt.string('Your answer: ').lower()


def get_correct_answer(rand_num):
    return 'yes' if is_even(rand_num) else 'no'


def is_equal_answers(user_answer, corr_answer, user):
    if user_answer == corr_answer:
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{corr_answer}'")
        print(f"Let's try again, {user}!")
        return False


def welcome_user():
    print('Welcome to the Brain Games!')
    user = prompt.string('May I have your name? ')
    print(f'Hello, {user}!')
    return user


def start():
    print(RULES)

    user = welcome_user()

    for _ in range(CHANCES):
        rand_num = print_random_num()
        corr_answer = get_correct_answer(rand_num)
        user_answer = get_user_answer()

        if not is_equal_answers(user_answer, corr_answer, user):
            break
    else:
        print(f'Congratulations, {user}!')

#start()