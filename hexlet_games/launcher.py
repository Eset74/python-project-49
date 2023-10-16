import prompt
CHANCES = 3


def start(game):

    user = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {user}!')
    print(game.RULES)

    for _ in range(CHANCES):

        question, corr_answer = game.generate_data()
        print(f'Question: {question}')
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
