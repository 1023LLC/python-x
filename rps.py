# import random


# emojis = {'r': '🗿', 'p': '📃', 's': '✂'}
# choices = ('r', 'p', 's')

# while True:
#     user_choice = input('Rock, Paper, or Scissors? (r/p/s): ').strip().lower()

#     if user_choice not in choices:
#         print('Invalid choice!')
        
#     computer_choice = random.choice(choices)

#     print(f'You chose {emojis[user_choice]} ')
#     print(f'Computer chose {emojis[computer_choice]} ')

#     if user_choice == computer_choice:
#         print('Tie')
#     elif (
#         (user_choice == 'r' and computer_choice == 's') or
#         (user_choice == 's' and computer_choice == 'p') or 
#         (user_choice == 'p' and computer_choice == 'r')):
#         print('You win!')
#     else:
#         print('You lose!')    
        
#     should_continue = input('Continue? (y/n): ').lower()
#     if should_continue == 'n':
#         break


import random


emojis = {'r': '🗿', 'p': '📃', 's': '✂'}
choices = ['r', 'p', 's']


def determine_winner(choice1, choice2):
    # Determine the winner between two choices.
    if choice1 == choice2:
        return 'tie'
    elif (
        (choice1 == 'r' and choice2 == 's') or
        (choice1 == 's' and choice2 == 'p') or
        (choice1 == 'p' and choice2 == 'r')
    ):
        return 'Player1'
    else:
        return 'Player2'
    
    
def single_player_mode():
    # Player vs Computer
    print("\n --- Single Player Mode: Best of 3 ---")
    
    player_wins = 0
    computer_wins = 0
    ties = 0
    
    while player_wins < 2 and computer_wins < 2:
        user_choice = input('Rock 🗿, Paper 📃, or Scissors ✂? (r/p/s): ').strip().lower()
        
        if user_choice not in choices:
            print('Invalid choice! Please choose r, p, or s')
            continue
        
        computer_choice = random.choice(choices)
        
        print(f'You chose {emojis[user_choice]}')
        print(f'Computer chose {emojis[computer_choice]}')
        
        result = determine_winner(user_choice, computer_choice)
        
        if result == 'tie':
            print("It's a tie!")
            ties += 1
        elif result == 'Player1':
            print("You win this round!")
            player_wins += 1
        else:
            print("Computer wins this round!")
            computer_wins += 1

        print(f"Score: You {player_wins}, Computer {computer_wins}, Ties {ties} \n")
        
    if player_wins == 2:
        print("Congratulations!!! You are the overall winner!")
    else:
        print("Game Over! The computer is the overall winner!")
        
    print(f"Final Statistics: Wins: {player_wins}, Losses: {computer_wins}, Ties: {ties}")   
    
    
def two_player_mode():
    # Player vs Player
    
    print("\n --- Two Player Mode: Best of 3 ---")
    
    player1_wins = 0 
    player2_wins = 0
    ties = 0
    
    while player1_wins < 2 and player2_wins < 2:
        player1_choice = input('Player 1: Rock 🗿, Paper 📃, or Scissors ✂? (r/p/s): ').strip().lower()
        if player1_choice not in choices:
            print('Invalid choice for Player 1! Please choose r, p, or s.')
            continue
        
        player2_choice = input('Player 2: Rock 🗿, Paper 📃, or Scissors ✂? (r/p/s): ').strip().lower()
        if player2_choice not in choices:
            print('Invalid choice for Player 2! Please choose r, p, or s.')
            continue
        
        print(f'Player 1 chose {emojis[player1_choice]}')
        print(f'Player 2 chose {emojis[player2_choice]}')
        
        result = determine_winner(player1_choice, player2_choice)
        if result == 'tie':
            print("It's a tie!")
            ties += 1
        elif result == 'Player1':
            print('Player1 wins this round!')
            player1_wins += 1
        elif result == 'Player2':
            print('Player2 wins this round!')
            player2_wins += 1
            
        print(f"Score: Player 1: {player1_wins}, Player 2: {player2_wins}, Ties: {ties}")
    
    if player1_wins == 2:
        print('Player 1 is the overall winner!!')
    else:
        print('Player 2 is the overall winner!!')
        
    print(f"Final Statistics: Player 1 wins: {player1_wins}, Player 2 wins: {player2_wins}, Ties: {ties}")
    
    
def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("1. Single Player (vs. Computer)")
    print("2. Two Player (Player vs Player)")
    
    while True:
        mode = input('Choose a mode, (1/2):').strip()
        if mode == '1':
            single_player_mode()
            break
        elif mode == '2':
            two_player_mode()
            break
        else:
            print("Invalid choice! Please choose 1 0r 2")
            
            
    print("Thanks for playing! Goodbye!")
    
    
main()