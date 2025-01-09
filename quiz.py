# print("Welcome to my computer quiz!")

# playing = input("Do you want to play? : ").lower().strip()

# if playing != 'yes':
#     quit()
# print("Okay! Let's play :)")

# score = 0

# answer = input("What does CPU stand for? ").lower().strip()
# if answer == 'central processing unit':
#     print('Correct!')
#     score += 1
# else:
#     print('Incorrect!')
    
# answer = input("What does GPU stand for? ").lower().strip()
# if answer == 'graphics processing unit':
#     print('Correct!')
#     score += 1
# else:
#     print('Incorrect!')
    
# answer = input("What does RAM stand for? ").lower().strip()
# if answer == 'random access memory':
#     print('Correct!')
#     score += 1
# else:
#     print('Incorrect!')
    
# answer = input("What does PSU stand for? ").lower().strip()
# if answer == 'power supply unit':
#     print('Correct!')
#     score += 1
# else:
#     print('Incorrect!')

# print(f"You got {score} questions correct!")
# print(f"You got {int(score/4 * 100)}%")

    
    

def main():
    print("Welcome to my computer quiz!")
    
    if input("Do you want to play? (yes/no): ").lower().strip() != 'yes':
        print('Goodbye!')
        return
    
    print("Okay! Let's play :) ")
    
    
    questions_and_answers = {
        "What does CPU stand for?" : "central processing unit",
        "What does GPU stand for?" : "graphics processing unit",
        "What does RAM stand for?" : "random access memory",
        "What does PSU stand for?" : "power supply unit"
    }
    
    score = 0
    
    for question, correct_answer in questions_and_answers.items():
        answer = input(question + " ").lower().strip()
        if answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print('Incorrect!')
    
    print(f"You got {score} out of {len(questions_and_answers)} questions correct!")
    print(f"You score: {int(score / len(questions_and_answers) * 100)} %")
    
    
if __name__ == "__main__":
    main()