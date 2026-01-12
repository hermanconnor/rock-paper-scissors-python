import random
from typing import Literal, Dict, List
from colorama import Fore, Back, Style, init

# Initialize colorama for cross-platform color support
init(autoreset=True)

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


def get_best_of_n():
    """
    Prompts the player to choose best-of-N format.
    Returns the number of rounds needed to win.
    """
    while True:
        print(f"\n{Fore.CYAN}Choose game mode: ")
        print(f"{Fore.CYAN}1. Endless Mode (play until you quit)")
        print(f"{Fore.CYAN}2. Best of N (first to win N/2 + 1 rounds)")

        choice = input(
            f"\n{Fore.YELLOW}Enter 1 or 2: {Style.RESET_ALL}").strip()

        if choice == "1":
            return None
        elif choice == "2":
            while True:
                try:
                    n = int(input(
                        f"{Fore.YELLOW}Enter odd number of rounds (e.g., 3, 5, 7): {Style.RESET_ALL}"))
                    if n > 0 and n % 2 == 1:
                        rounds_to_win = (n // 2) + 1
                        print(
                            f"{Fore.GREEN}First to win {rounds_to_win} rounds wins the match! {Style.RESET_ALL}")
                        return rounds_to_win
                    else:
                        print(
                            f"{Fore.RED}Please enter a positive odd number!{Style.RESET_ALL}")
                except ValueError:
                    print(
                        f"{Fore.RED}Invalid input! Please enter a number.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Invalid choice! Please enter 1 or 2.{Style.RESET_ALL}")


def get_player_choice() -> (str | None):
    """Prompts player for input and validates it against the INPUT_MAP."""
    while True:
        prompt = f"\n{Fore.CYAN}Choose {', '.join(CHOICES)} (or r/p/s). Type 'q' to quit: {Style.RESET_ALL}"
        user_input = input(prompt).lower().strip()

        if user_input in ["q", "quit", "exit"]:
            return None

        if user_input in INPUT_MAP:
            return INPUT_MAP[user_input]

        print(
            f"{Fore.RED}Invalid input! Please use {', '.join(CHOICES)} or their initials.{Style.RESET_ALL}")


def get_computer_choice() -> str:
    """Randomly selects a choice for the computer."""
    return random.choice(CHOICES)


def determine_winner(player: str, computer: str) -> Literal['ties', 'player', 'computer']:
    """Calculates the winner using the BEATS dictionary."""
    if player == computer:
        return "ties"

    return "player" if BEATS[player] == computer else "computer"


def display_round_result(player: str, computer: str, winner: Literal['ties', 'player', 'computer']) -> None:
    """Displays the result of a single round with color coding."""

    print(f"\n{Style.BRIGHT}You chose: {Fore.BLUE}{player}{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}Computer chose: {Fore.MAGENTA}{computer}{Style.RESET_ALL}")
    print(Fore.WHITE + "-" * 40)

    if winner == "ties":
        print(f"{Fore.YELLOW}{Style.BRIGHT}It's a tie!{Style.RESET_ALL}")
    elif winner == "player":
        print(f"{Fore.GREEN}{Style.BRIGHT}🎉 You win! {player.capitalize()} beats {computer}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}{Style.BRIGHT}Computer wins! {computer.capitalize()} beats {player}{Style.RESET_ALL}")


# def display_scoreboard(score: Dict[str, int], final: bool = False) -> None:
#     """Prints the current or final score."""
#     header = "FINAL SCORE" if final else "CURRENT SCORE"
#     print(f"\n{'='*30}\n{header:^30}\n{'='*30}")
#     print(
#         f" Player: {score['player']} | Computer: {score['computer']} | Ties: {score['ties']}")
#     print("="*30)


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
