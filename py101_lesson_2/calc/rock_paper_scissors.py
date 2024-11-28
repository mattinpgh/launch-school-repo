"""Rock paper scissors game, now with lizards and spock"""
import random
import os
import platform

GAME_DATA = {
    'rock': {'alias': ['1', 'r', 'rock'], 'beats': ['scissors', 'lizard']},
    'paper': {'alias': ['2', 'p', 'paper'], 'beats': ['rock', 'spock']},
    'scissors': {'alias': ['3', 's', 'scissors'], 'beats': ['paper', 'lizard']},
    'lizard': {'alias': ['4', 'l', 'lizard'], 'beats': ['spock', 'paper']},
    'spock': {'alias': ['5', 'sp', 'spock'], 'beats': ['scissors', 'rock']}
}

ALIAS_TEXT = "\n".join(f"{key.capitalize()}={value['alias']}"
                       for key, value in GAME_DATA.items())

def prompt(message):
    """
    Prepend a prompt symbol to a message.
    """
    print(f"==> {message}")


def normalize_choice(user_choice):
    """
    Returns user input from any alias back to a key
    to simplify finding a winner
    """
    for key, value in GAME_DATA.items():
        if user_choice in value['alias']:
            return key
    return None


def check_winner(human_choice_compare, machine_choice_compare):
    """
    Determines the winner of an individual game.

    Returns:
        The result of the game as a string: "human", "machine", or "tie".
    """
    if human_choice_compare == machine_choice_compare:
        return "tie"
    if human_choice_compare in GAME_DATA[machine_choice_compare]['beats']:
        return "machine"
    if machine_choice_compare in GAME_DATA[human_choice_compare]['beats']:
        return "human"
    return None


def check_grand_winner(current_human_wins, current_machine_wins):
    """
    Check if a grand winner has been determined.

    Returns:
        A tuple where the first element indicates if the
        game is over (True/False), and the second element is the winner
        ('human', 'machine', or '').
    """
    if current_human_wins >= 3:
        return True, "human"
    if current_machine_wins >= 3:
        return True, "machine"

    return False, ""


def clear_screen():
    """Clear the screen"""
    system = platform.system()
    os.system('cls' if system == 'Windows' else 'clear')


def make_choice():
    """
    Clears the screen and prompts the user to make a choice.
    Returns the choice as a lowercase string.

    Checks that the choice is valid and repeats the prompt if not.
    """
    while True:
        clear_screen()
        prompt(f'Choose one:\n{ALIAS_TEXT}')
        choice = input("==>")
        normalized_choice = normalize_choice(choice)

        if normalized_choice:
            return normalized_choice.lower()
        prompt("That's not a valid choice. Please try again.")


def main():
    """
    This function simulates a game where a human and computer take turns making
    choices, tracks wins for each, and determines a grand winner after each round.
    """
    human_wins = 0
    machine_wins = 0
    play_again = "continue"

    while True:
        human_choice = make_choice()
        computer_choice = random.choice(list(GAME_DATA.keys()))
        round_winner = check_winner(human_choice, computer_choice)
        prompt(f'You chose {human_choice}. The computer chose {computer_choice}.')

        match round_winner:
            case "human":
                human_wins += 1
                print(f'You won! You have {human_wins} points and the computer has {machine_wins}.')
            case "machine":
                machine_wins += 1
                print(f'The computer won! The computer has {machine_wins} '
                      f'points and you have {human_wins}.')
            case "tie":
                print('It\'s a tie! No points awarded.')

        game_over, winner = check_grand_winner(human_wins, machine_wins)
        if game_over:
            print('The game is over! Resetting the score.')
            human_wins, machine_wins = 0, 0
            play_again = "start a new game"

            if winner == "human":
                print("Congratulations! You are the grand winner!")
            elif winner == "machine":
                print("Sorry, but the computer is the grand winner!")

        while True:
            prompt(f"Would you like to {play_again}? (yes, no)")
            answer = input().lower()
            if answer.startswith('n') or answer.startswith('y'):
                prompt("Thank you for playing!")
                break
            prompt("Please enter 'yes' or 'no'.")

        if answer[0] == 'n':
            break

main()
