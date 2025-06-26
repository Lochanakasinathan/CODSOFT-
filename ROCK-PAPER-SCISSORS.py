import random

# Score Tracking (Optional)
user_score = 0
computer_score = 0

while True:
    # User Input: Prompt the user to choose rock, paper, or scissors.
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    # Validate input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Try again.")
        continue

    # Computer Selection: Generate a random choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Display Result: Show the user's choice and the computer's choice.
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    # Game Logic: Determine the winner
    if user_choice == computer_choice:
        print("It's a tie.")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        user_score += 1
    else:
        print("You lose.")
        computer_score += 1

    # Display current score
    print("Score -> You:", user_score, "| Computer:", computer_score)

    # Play Again: Ask the user if they want to play another round.
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
