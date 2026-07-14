import random
tools = ['rock', 'paper', 'scisors']
is_playing = True
while is_playing:
    choice = input('Rock - Paper - Scisors : ').lower()
    robot_choice = random.choice(tools)
    if (choice == 'rock' and robot_choice == 'paper') or (choice == 'scisors' and robot_choice == 'rock') or (choice == 'paper' and robot_choice == 'scisors'):
        print(f"You lose. You choosed {choice} and the robot {robot_choice}.")
        play_again = input('You still want to play (y/n): ').lower()
        if play_again == 'n':
            is_playing = False
            print('Thanks for playing!')
        elif play_again == 'y':
            continue
        else:
            print('invalid input!')
    elif (choice == 'paper' and robot_choice == 'rock') or (choice == 'rock' and robot_choice == 'scisors') or (choice == 'scisors' and robot_choice == 'paper'):
        print(f"You Win. You choosed {choice} and the robot {robot_choice}.")
        play_again = input('You still want to play (y/n): ').lower()
        if play_again == 'n':
            is_playing = False
            print('Thanks for playing!')
        elif play_again == 'y':
            continue
        else:
            print('invalid input!')
    elif choice == robot_choice:
        print(f"Draw. You choosed {choice} and the robot {robot_choice}.")
        play_again = input('You still want to play (y/n): ').lower()
        if play_again == 'n':
            is_playing = False
            print('Thanks for playing!')
        elif play_again == 'y':
            continue
        else:
            print('invalid input!')
    else:
        print('Invalid input!')



