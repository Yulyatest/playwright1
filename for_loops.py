# for item in 'Hello':
#     print(item)
# for item in range(4):
#     print(item)

names = ['Test1', 'Test2', 'test3']
for x in names:
    print( f'Hello, {x}')
    if x == 'Test2':
        print(f"{x} is my sun")
        for x in names:
            print("I'm inside the if")
    else:
        print('Hello there...')
