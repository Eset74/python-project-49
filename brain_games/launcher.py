from brain_games.cli import welcome_user
import prompt
CHANCES = 3


def start(game):
    user = welcome_user()
    print(game.RULES)
    for _ in range(CHANCES):
        corr_answer = game.generate_data()
        user_answer = prompt.string('Your answer: ')

        if user_answer == corr_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{corr_answer}'")
            print(f"Let's try again, {user}!")
            break
    else:
        print(f'Congratulations, {user}!')
