"""Rock paper scissors game"""
import random

VALID_CHOICES = ['rock', 'paper', 'scissors']
def prompt(message):
    """Prepend a prompt symbol to a message."""
    print(f"==> {message}")

def check_winner(human_choice, machine_choice):
    """Check who won the game."""
    if human_choice == machine_choice:
        return "It's a tie!"
    if (human_choice == 'rock' and machine_choice == 'scissors') or \
       (human_choice == 'paper' and machine_choice == 'rock') or \
       (human_choice == 'scissors' and machine_choice == 'paper'):
        return "You won!"
    return "You lost!"

while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice. Please try again.")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {choice}. The computer chose {computer_choice}.')
    print(check_winner(choice, computer_choice))
    while True:
        """Keep asking until the user enters 'yes' or 'no'."""
        prompt("Would you like to play again? (yes, no)")
        answer = input().lower()
        if answer.startswith('n') or answer.startswith('y'):
            prompt("Thank you for playing!")
            break
        else:
            prompt("Please enter 'yes' or 'no'.")

    if answer[0] == 'n':
        break