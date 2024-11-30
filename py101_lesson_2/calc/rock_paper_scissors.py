"""Rock paper scissors game, now with lizards and spock"""
import random
import time
import sys
import os
import platform


class GameConfig:
    """
    Initialize the GameConfig object with flexible keyword arguments because
    pylint kept getting mad about how many arguments I had in the constructor.

    Keyword Args:
        # game_data (dict, optional): Initial game configuration.
        # Defaults to a predefined setup.
        # games_to_win (int, optional): Target number of games to win. Defaults to 3.
        # human_wins (int, optional): Initial human win count. Defaults to 0.
        # machine_wins (int, optional): Initial machine win count. Defaults to 0.
        # play_again (str, optional): Initial play state. Defaults to "continue".
    """
    def __init__(self, **kwargs):
        self.game_data = kwargs.get("game_data") or self._default_game_data()
        self.games_to_win = kwargs.get("games_to_win", 3)
        self.human_wins = kwargs.get("human_wins", 0)
        self.machine_wins = kwargs.get("machine_wins", 0)
        self.play_again = kwargs.get("play_again", "continue")

    @staticmethod
    def _default_game_data():
        """Returns the default game configuration."""
        return {
            'rock': {'alias': ['1', 'r', 'rock'], 'beats': ['scissors', 'lizard']},
            'paper': {'alias': ['2', 'p', 'paper'], 'beats': ['rock', 'spock']},
            'scissors': {'alias': ['3', 's', 'scissors'], 'beats': ['paper', 'lizard']},
            'lizard': {'alias': ['4', 'l', 'lizard'], 'beats': ['spock', 'paper']},
            'spock': {'alias': ['5', 'sp', 'spock'], 'beats': ['scissors', 'rock']}
        }


    def get_win_flavor(self, winning_choice, losing_choice):
        """
        Flavor text for winning and losing combinations.
        """
        match winning_choice:
            case "rock":
                match losing_choice:
                    case "scissors":
                        r_value = "Rock breaks scissors!"
                    case "lizard":
                        r_value = "Rock crushes lizard!"
                    case _:
                        r_value = "Error"
            case "paper":
                match losing_choice:
                    case "rock":
                        r_value = "Paper covers rock!"
                    case "spock":
                        r_value = "Paper disproves Spock!"
                    case _:
                        r_value = "Error"
            case "scissors":
                match losing_choice:
                    case "paper":
                        r_value = "Scissors cut paper!"
                    case "lizard":
                        r_value = "Scissors decapitate lizard!"
                    case _:
                        r_value = "Error"
            case "lizard":
                match losing_choice:
                    case "spock":
                        r_value = "Lizard poisons Spock!"
                    case "paper":
                        r_value = "Lizard eats paper!"
                    case _:
                        r_value = "Error"
            case "spock":
                match losing_choice:
                    case "scissors":
                        r_value = "Spock melts scissors!"
                    case "rock":
                        r_value = "Spock vaporizes rock!"
                    case _:
                        r_value = "Error"
            case _:
                r_value = "Error"
        return r_value


    def get_game_alias_text(self):
        """
        Prints a string of game aliases
        """
        return "\n".join(
            f"{key.capitalize()}={value['alias']}"
            for key, value in self.game_data.items())

def prompt(message):
    """
    Prepend a prompt symbol to a message.
    """
    print(f"==> {message}")


def spinner(duration):
    """
    Displays a spinner animation for the specified duration.

    duration (float): How long the spinner should run in seconds.
    """
    spinner_chars = "|/-\\"
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in spinner_chars:
            sys.stdout.write(f"\r{char} ")
            sys.stdout.flush()
            time.sleep(0.1)


def normalize_choice(user_choice, config_object):
    """
    Returns user input from any alias back to a key
    to simplify finding a winner
    """
    for key, value in config_object.game_data.items():
        if user_choice.lower() in value['alias']:
            return key
    return None


def resolve_round(human_choice_compare, machine_choice_compare, config_object):
    """
    Resolve a round of the game. Compare human and machine choices and determine
    a winner. Increment the score, print the result.

    No return value

    """
    if human_choice_compare == machine_choice_compare:
        print('It\'s a tie! No points awarded.')
    if human_choice_compare in config_object.game_data[machine_choice_compare]['beats']:
        config_object.machine_wins += 1
        print(config_object.get_win_flavor(machine_choice_compare, human_choice_compare))
        print(f'The computer won! The computer has {config_object.machine_wins} '
              f'points and you have {config_object.human_wins}.')
    if machine_choice_compare in config_object.game_data[human_choice_compare]['beats']:
        config_object.human_wins += 1
        print(config_object.get_win_flavor(human_choice_compare, machine_choice_compare))
        print(f'You won! You have {config_object.human_wins} '
              f'points and the computer has {config_object.machine_wins}.')


def cleanup_game(winner, config_object):
    """
    Resets wins on the configuration object
    announces the winner and the end of the game
    sets the play_again flag to start a new game

    no return value
    """

    config_object.human_wins, config_object.machine_wins = 0, 0
    config_object.play_again = "start a new game"

    if winner == "human":
        print("Congratulations! You are the grand winner!")
    elif winner == "machine":
        print("Sorry, but the computer is the grand winner!")


def check_grand_winner(config_object):
    """
    Check if a grand winner has been determined. If a winner is found,
    clean up the game and set play_again to 'start a new game'. If not,
    ensure play_again remains 'continue'.
    """
    if config_object.human_wins >= 3:
        cleanup_game("human", config_object)
        return
    if config_object.machine_wins >= 3:
        cleanup_game("machine", config_object)
        return

    config_object.play_again = "continue"


def clear_screen():
    """Clear the screen"""
    system = platform.system()
    os.system('cls' if system == 'Windows' else 'clear')


def make_choice(config_object):
    """
    Clears the screen and prompts the user to make a choice.
    Returns the choice as a lowercase string.

    Checks that the choice is valid and repeats the prompt if not.
    """
    fixit = 0
    while True:
        clear_screen()
        if fixit:
            prompt("That's not a valid choice. Please try again.")
        prompt(f'Choose one:\n{config_object.get_game_alias_text()}')
        choice = input("==>")
        normalized_choice = normalize_choice(choice, config_object)

        if normalized_choice:
            fixit = 0
            return normalized_choice.lower()
        fixit = 1

def want_to_play_again(config_object):
    """
    Encapsulates the logic for determining whether to play again.
    """
    while True:
        prompt(f"Would you like to {config_object.play_again}? (yes, no)")
        answer = input().lower()
        if answer in {'yes', 'y'}:
            return 1
        if answer in {'no', 'n'}:
            return 0
        prompt("Please enter 'yes' or 'no'.")

def main():
    """
    This function simulates a game where a human and computer take turns making
    choices, tracks wins for each, and determines a grand winner after each round.
    """
    config = GameConfig(
        game_data=None,
        games_to_win=3,
        human_wins=0,
        machine_wins=0,
        play_again="continue")

    while True:
        human_choice = make_choice(config)
        computer_choice = random.choice(list(config.game_data.keys()))
        spinner(0.5)
        prompt(f'You chose {human_choice}. The computer chose {computer_choice}.')

        resolve_round(human_choice, computer_choice, config)
        check_grand_winner(config)

        if not want_to_play_again(config):
            break

main()
