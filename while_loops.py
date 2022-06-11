# a = 0
# while a < 5:
#     print("hello")
#     a += 1 # the same as a = a + 1
#
# for a in range(5):
#     print(f"hello, {a}")

# user_input = ''
# while user_input != '-1':
#     user_input = input('Type some number: ')
#     print(f"The number is {user_input}")

user_input = ''
while user_input != '-1':
    user_input = input('Guess a number from 1 to 100: ')
    if user_input == '77':
        print('Bingo! You guessed')
        break
    print(f"The number is {user_input}. Try again...")

