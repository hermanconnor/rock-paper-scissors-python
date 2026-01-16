import random
from typing import Literal, Dict, List
from colorama import Fore, Style, init

# Initialize colorama for cross-platform color support
init(autoreset=True)

CHOICES: List[str] = ["rock", "paper", "scissors"]

BEATS: Dict[str, str] = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

INPUT_MAP: dict[str, str] = {
    "r": "rock", "rock": "rock",
    "p": "paper", "paper": "paper",
    "s": "scissors", "scissors": "scissors",
    "q": "quit", "quit": "quit", "exit": "quit"
}


def get_player_choice() -> str | None:
    while True:
        prompt = f"\n{Fore.CYAN}Choose {', '.join(CHOICES)} (r/p/s) or 'q' to quit: {Style.RESET_ALL}"
        user_input = input(prompt).lower().strip()

        mapped = INPUT_MAP.get(user_input)
        if mapped == "quit":
            return None
        if mapped:
            return mapped

        print(f"{Fore.RED}Invalid input!{Style.RESET_ALL}")


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


def display_score(score: Dict[Literal['ties', 'player', 'computer'], int]) -> None:
    """Displays the current running score."""
    print(f"\n{Fore.WHITE}{Style.BRIGHT}{'=' * 40}")
    print(f"{Fore.CYAN}{Style.BRIGHT}SCOREBOARD")
    print(f"{Fore.WHITE}{'=' * 40}{Style.RESET_ALL}")

    player_score = score['player']
    computer_score = score['computer']

    player_color = Fore.GREEN if player_score > computer_score else Fore.WHITE
    computer_color = Fore.RED if computer_score > player_score else Fore.WHITE

    print(f"{player_color}Player: {player_score}{Style.RESET_ALL}")
    print(f"{computer_color}Computer: {computer_score}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Ties: {score['ties']}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{'=' * 40}{Style.RESET_ALL}")


def play_game() -> None:
    print(f"{Fore.GREEN}{Style.BRIGHT}{'=' * 40}")
    print(f"🎮 ROCK, PAPER, SCISSORS 🎮")
    print(f"{'=' * 40}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Type 'quit' or 'q' to exit anytime{Style.RESET_ALL}")

    # Initialize score
    score: Dict[Literal['ties', 'player', 'computer'], int] = {
        "player": 0,
        "computer": 0,
        "ties": 0
    }

    # Game loop
    while True:
        player_choice = get_player_choice()

        if player_choice is None:
            print(
                f"\n{Fore.CYAN}{Style.BRIGHT}Thanks for playing! Final Score:{Style.RESET_ALL}")
            display_score(score)
            break

        computer_choice = get_computer_choice()
        winner = determine_winner(player_choice, computer_choice)

        # Update score
        score[winner] += 1

        # Display result and score
        display_round_result(player_choice, computer_choice, winner)
        display_score(score)

        # Optional: prompt to keep the screen from scrolling too fast
        continue_game = input(
            f"\nPress Enter to continue or 'q' to quit: ").lower().strip()
        if continue_game in ['q', 'quit', 'exit']:
            print(
                f"\n{Fore.CYAN}{Style.BRIGHT}Thanks for playing! Final Score:{Style.RESET_ALL}")
            display_score(score)
            break


if __name__ == "__main__":
    play_game()
