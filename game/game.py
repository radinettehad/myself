import random

choice = ("rock", "paper", "scissors")
def user_input():
    return input("Enter your choice (rock, paper, scissors): ")

def computer_choice():
    return random.choice(choice)
def determine_winner(user_input, computer_choice):
    if user_input == computer_choice:
        return "It's a tie!"
    elif (user_input == "rock" and computer_choice == "scissors") or \
         (user_input == "paper" and computer_choice == "rock") or \
         (user_input == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"
    
def main():
    user = user_input()
    computer = computer_choice()
    print(f"Computer chose: {computer}")
    result = determine_winner(user, computer)
    print(result)

answer = 'y'
while not answer == 'n':
     main()
     answer = input("Do you want to play again? (y/n): ").lower()

