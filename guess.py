# import random


# def guess_the_number():
#     number_to_guess = random.randint(1,100)
#     attempts = 0


#     while True:
#         try:
#             guess = int(input('Guess the number between 1 and 100: '))
#             attempts += 1
#             if guess < number_to_guess:
#                 print('Too low!')
#             elif guess > number_to_guess:
#                     print('Too high!')
#             else:
#                 print('Congratulations! You guessed it right!!!')
#                 print('')
#                 print(f'You guessed the number in {attempts} attempts')
#                 break
#         except ValueError:
#             print('Please enter a valid number!')
            
# guess_the_number()


import random


def guess_the_number():
    print('Welcome to the Enhanced Number Guessing Game!')
    print('')
    
    while True:
        try:
            min_value = int(input('Enter the minimum value for the range: '))
            max_value = int(input('Enter the maximum value for the range: '))
            
            if min_value >= max_value:
                print('Minimum value must be less than maximum value. Try again!')
            else:
                break
        except ValueError:
            print('Invalid input! Please enter valid numbers.')
            
    
    number_to_guess = random.randint(min_value, max_value)
    max_attempts = int(input('Enter the maximum number of attempts allowed: '))
    attempts = 0
    best_score = None
    
    print(f'I have picked a number between {min_value} and {max_value}. You have {max_attempts} attempts to guess it!')
    
    
    while attempts < max_attempts:
        try:
            
            player_guess = int(input(f'Attempt {attempts + 1 }/{max_attempts} - Enter your guess:'))
            attempts += 1
            
            
            if player_guess < min_value or player_guess > max_value:
                print(f'Please enter a number between {min_value} and {max_value} !')
            elif player_guess < number_to_guess:
                print('Too low! Try again.')
            elif player_guess > number_to_guess:
                print('Too high! Try again.')
            else:
                print(f'Congratulations! You guessed the number in {attempts} attempts')
                print()
                if best_score is None or attempts < best_score:
                    best_score = attempts
                    print(f'Your best score: {best_score} attepmts.')
                    break
        except ValueError:
            print('Invalid input! Please enter a valid number.')
       
            
        if attempts == max_attempts and player_guess != number_to_guess:
            print(f'Game Over! You have used up all your attempts.')
            print(f'The correct number was: {number_to_guess}')
            
        
            play_again = input('Would you like to play again? (yes/no): ').strip().lower()
            if play_again == "yes":
                guess_the_number()
            else:
                print('Thanks for playing. Good Bye!')
            

guess_the_number()