# import random


# while True:
#     choice =  input('Roll the dice? (y/n): ').lower()
#     if choice == 'y':
#         die1 = random.randint(1, 6)
#         die2 = random.randint(1, 6)
#         print(f'{die1}, {die2}')
#     elif choice == 'n':
#         print('Thanks for playing!')
#         break
#     else:
#         print('Invalid choice!')

def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]


def get_num_dice():
    
    while True:
        try:
            num_dice = int(input("How many dice would you like to roll? (Enter a number): "))
            if num_dice > 0:
                return num_dice
            else:
                print("Please enter a positive number of dice!")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def play_dice_game():
    
    print("Welcome to the dice rolling game!!!")
    
    total_rolls = 0     # Counter for total rolls
    
    while True:
        choice = input("Roll the dice? (y/n): ").strip().lower()
        if choice == "y":
            num_dice = get_num_dice()
            results = roll_dice(num_dice)
            print(f'You rolled: {", ".join(map(str, results))}')
            total_rolls += 1
        elif choice == 'n':
            print(f'Thanks for playing! You rolled the dice {total_rolls} time(s) in total.')
            break
        
        else:
            print("Invalid choice! Please enter 'y' to roll and 'n' to quit" )

if __name__ == "main":
    play_dice_game()