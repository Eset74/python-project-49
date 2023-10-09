from brain_games.scripts.brain_games import welcome_user
from brain_games.scripts.brain_games import show_question
from brain_games.scripts.brain_games import get_user_answer
from brain_games.scripts.brain_games import is_equal_answers
from brain_games.scripts.vars_const import CHANCES


def start(game):
    user = welcome_user(game)

    for _ in range(CHANCES):
        corr_answer = show_question(game)
        user_answer = get_user_answer(game)

        if not is_equal_answers(user_answer, corr_answer, user):
            break
    else:
        print(f'Congratulations, {user}!')
