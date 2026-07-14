import random

is_playing = True
while is_playing:
    answer = input('Roll the dice (y/n): ')
    if answer.lower() == 'y':
        dic1 = random.randint(1,6)
        dic2 = random.randint(1,6)
        print(f'({dic1}, {dic2})')
    elif answer.lower() == 'n':
        print('Thanks for playing!')
        is_playing = False
    else:
        print('Invalid choice!')

