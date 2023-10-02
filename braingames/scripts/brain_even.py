from brain_games import main as greetings
import braingames.cli
import prompt
import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):  # Return of tuple (is_even? and a correct answer phrase)
    return (True, 'yes') if num % 2 == 0 else (False, 'no')


def main():
    chances = 0

    greetings()
    print(RULES)

    while chances < 3:
        rand_num = random.randint(0, 100)  # Generate some int
        print(f'Question: {rand_num}')
        answer = prompt.string('Your answer: ').lower()
        even, correct_phrase = is_even(rand_num)
        if (even and answer == 'yes') or (not even and answer == 'no'):
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_phrase}\'')
            print(f'Let\'s try again, {braingames.cli.name}!')
            return
        chances += 1

    print(f'Congratulations, {braingames.cli.name}!')


main()
