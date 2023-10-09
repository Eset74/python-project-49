from brain_games.scripts.brain_games import *


def start(game):
    user = welcome_user(game)

    for _ in range(CHANCES):
        corr_answer = show_question(game)
        user_answer = get_user_answer(game)

        if not is_equal_answers(user_answer, corr_answer, user):
            break
    else:
        print(f'Congratulations, {user}!')
