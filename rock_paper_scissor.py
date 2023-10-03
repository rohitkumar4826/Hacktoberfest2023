import random

print("Welcome to Rock, Paper, Scissors!")
user_score = 0
comp_score = 0
ties = 0

name = input("Enter your name here: ")

while True:
    print("""1. Paper vs Rock --> Paper 
2. Rock vs Scissor --> Rock
3. Scissors vs Paper --> Scissor""")
    
    choice = int(input("Enter your choice (1-3): "))
    print()

    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid input: "))

    if choice == 1:
        user_choice = "rock"
    elif choice == 2:
        user_choice = "paper"
    else:
        user_choice = "scissor"

    print("Your choice is:", user_choice)
    print("Now it's the computer's turn")

    computer = random.randint(1, 3)

    if computer == 1:
        comp_choice = "rock"
    elif computer == 2:
        comp_choice = "paper"
    else:
        comp_choice = "scissor"

    print("The computer's choice is:", comp_choice)

    if (user_choice == "paper" and comp_choice == "rock") or (user_choice == "rock" and comp_choice == "paper"):
        print("Paper wins")
        result = "paper"
    elif (user_choice == "scissor" and comp_choice == "rock") or (user_choice == "rock" and comp_choice == "scissor"):
        print("Rock wins")
        result = "rock"
    elif user_choice == comp_choice:
        print("It's a tie")
        result = "tie"
    else:
        print("Scissor wins")
        result = "scissor"

    if result == "tie":
        ties += 1
    elif result == user_choice:
        print("You win!")
        user_score += 1
    else:
        print("Computer wins")
        comp_score += 1

    print("\nScores:")
    print(name + "'s score is", user_score)
    print("Computer's score is", comp_score)
    print("Ties:", ties)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

print("Thanks for playing!")
