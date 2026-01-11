import random
from typing import Literal, Dict, List

CHOICES: List[str] = ["rock", "paper", "scissors"]

BEATS: Dict[str, str] = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

INPUT_MAP: Dict[str, str] = {
    "r": "rock", "rock": "rock",
    "p": "paper", "paper": "paper",
    "s": "scissors", "scissors": "scissors"
}


def get_player_choice() -> (str | None):
    """Prompts player for input and validates it against the INPUT_MAP."""
    while True:
        prompt = f"\nChoose {', '.join(CHOICES)} (or r/p/s). Type 'q' to quit: "
        user_input = input(prompt).lower().strip()

        if user_input in ["q", "quit", "exit"]:
            return None

        if user_input in INPUT_MAP:
            return INPUT_MAP[user_input]

        print(
            f"Invalid input! Please use {', '.join(CHOICES)} or their initials.")


def get_computer_choice() -> str:
    """Randomly selects a choice for the computer."""
    return random.choice(CHOICES)


def determine_winner(player: str, computer: str) -> Literal['ties', 'player', 'computer']:
    """Calculates the winner using the BEATS dictionary."""
    if player == computer:
        return "ties"

    return "player" if BEATS[player] == computer else "computer"


def display_scoreboard(score: Dict[str, int], final: bool = False) -> None:
    """Prints the current or final score."""
    header = "FINAL SCORE" if final else "CURRENT SCORE"
    print(f"\n{'='*30}\n{header:^30}\n{'='*30}")
    print(
        f" Player: {score['player']} | Computer: {score['computer']} | Ties: {score['ties']}")
    print("="*30)


def play_game() -> None:
    print("Welcome to Rock, Paper, Scissors!")

    score = {"player": 0, "computer": 0, "ties": 0}

    while True:
        player_choice = get_player_choice()

        if player_choice is None:
            display_scoreboard(score, final=True)
            print("Thanks for playing! Goodbye.")
            break

        computer_choice = get_computer_choice()
        winner = determine_winner(player_choice, computer_choice)
        score[winner] += 1

        # Display round result
        print(
            f"\nResult: {player_choice.upper()} vs {computer_choice.upper()}")

        if winner == 'ties':
            print(">> It's a draw!")
        else:
            winning_choice = player_choice if winner == "player" else computer_choice
            losing_choice = computer_choice if winner == 'player' else player_choice
            print(
                f">> {winner.capitalize()} wins! {winning_choice.capitalize()} beats {losing_choice}.")

        display_scoreboard(score)


if __name__ == "__main__":
    play_game()
