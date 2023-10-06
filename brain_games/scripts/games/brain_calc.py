from brain_games.scripts.brain_games import *


def start():
    user = welcome_user('Calc')

    for _ in range(CHANCES):
        corr_answer = show_question('Calc')
        user_answer = get_user_answer('Calc')

        if not is_equal_answers(user_answer, corr_answer, user):
            break
    else:
        print(f'Congratulations, {user}!')

#start()
