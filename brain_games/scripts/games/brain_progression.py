from brain_games.scripts.brain_games import *


def start():
    user = welcome_user('Progression')

    for _ in range(CHANCES):
        corr_answer = show_question('Progression')
        user_answer = get_user_answer('Progression')

        if not is_equal_answers(user_answer, corr_answer, user):
            break
    else:
        print(f'Congratulations, {user}!')

#start()
