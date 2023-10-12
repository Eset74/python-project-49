import prompt


def welcome_user():
    user = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {user}!')

    return user
