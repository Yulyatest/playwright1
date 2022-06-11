# def greeting9(name):
#     print(f'Hello, {name}')
# greeting9('Symon')

def user_guessing_game(secret_num, stop_char):
    user_input = ''
    while user_input != stop_char:
        user_input = input('\nGuess a number from 1 to 100: ')
        if user_input == secret_num:
            print('Bingo! You guessed')
        else:
            print(f"The number is {user_input}. Try again...")

user_guessing_game(str(19), 'stop')
user_guessing_game()