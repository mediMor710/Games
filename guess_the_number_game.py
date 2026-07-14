number_to_guess = int(input('Keep a number in your mind: '))
is_guessed = False
while not(is_guessed):
    try:
        user_guess = int(input('Guess the number between 1 and 100: '))
        difference = abs(number_to_guess - user_guess)
        if (user_guess > number_to_guess and difference >= 25) or (user_guess < number_to_guess and difference >= 25):
            print('Too Far.')
        elif (user_guess > number_to_guess and difference <= 15 and difference > 5):
            print('Too High.')
        elif (user_guess < number_to_guess and difference <= 15 and difference > 5):
            print('Too Low.')    
        elif (user_guess > number_to_guess and difference <= 5) or (user_guess < number_to_guess and difference <= 5):
            print('Too close.')
        elif user_guess == number_to_guess:
            print('Congratulations, you got the right number!')
            play_again = input('Do you still want to play (y/n): ').lower()
            if play_again == 'n':
                is_guessed = True
                print('Thanks for playing!')
            elif play_again == 'y':
                continue
            else:
                print('invalid input!')
    except:
        print('Invalid input!')