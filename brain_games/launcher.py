from brain_games.scripts.brain_games import welcome_user
from brain_games.scripts.brain_games import is_equal_answers
from brain_games.scripts.vars_const import CHANCES
import prompt


def start(game):
    user = welcome_user(game)

    for _ in range(CHANCES):
        corr_answer = game.run_game()
        user_answer = prompt.string('Your answer: ')

        if not is_equal_answers(user_answer, corr_answer, user):
            break
    else:
        print(f'Congratulations, {user}!')
