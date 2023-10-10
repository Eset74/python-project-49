#!/usr/bin/env/python3
import prompt


def welcome_user(game):
    user = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {user}!')

    return user


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
