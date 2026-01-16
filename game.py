import random
from typing import Literal, Dict, List, TypedDict
from colorama import Fore, Back, Style, init

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


class ChoiceStats(TypedDict):
    rock: int
    paper: int
    scissors: int


class GameStats(TypedDict):
    total_rounds: int
    choices: ChoiceStats
    current_streak: int
    longest_streak: int


def get_best_of_n() -> int | None:
    while True:
        print(f"\n{Fore.CYAN}Choose game mode: ")
        print(f"1. Endless Mode\n2. Best of N")
        choice = input(
            f"\n{Fore.YELLOW}Enter 1, 2, or 'q' to quit: {Style.RESET_ALL}").strip().lower()

        if choice in ["q", "quit", "exit"]:
            return "QUIT_GAME"

        if choice == "1":
            return None
        elif choice == "2":
            while True:
                try:
                    n = int(input(
                        f"{Fore.YELLOW}Enter odd number of rounds (3, 5, 7...): {Style.RESET_ALL}"))
                    if n > 0 and n % 2 == 1:
                        return (n // 2) + 1
                    print(
                        f"{Fore.RED}Please enter a positive ODD number.{Style.RESET_ALL}")
                except ValueError:
                    print(
                        f"{Fore.RED}Invalid input! Please enter a number.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Invalid choice!{Style.RESET_ALL}")


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


def display_score(score: Dict[Literal['ties', 'player', 'computer'], int], rounds_to_win: int | None = None) -> None:
    """
    Displays the current score with color coding.
    If rounds_to_win is set, shows progress toward winning the match.
    """
    print(f"\n{Fore.WHITE}{Style.BRIGHT}{'=' * 40}")
    print(f"{Fore.CYAN}{Style.BRIGHT}SCOREBOARD")
    print(f"{Fore.WHITE}{'=' * 40}{Style.RESET_ALL}")

    # Color code based on who's winning
    player_score = score['player']
    computer_score = score['computer']
    player_color = Fore.GREEN if player_score > computer_score else Fore.WHITE
    computer_color = Fore.RED if computer_score > player_score else Fore.WHITE

    print(f"{player_color}Player: {player_score}{Style.RESET_ALL}")
    print(f"{computer_color}Computer: {computer_score}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Ties: {score['ties']}{Style.RESET_ALL}")

    # If best-of-N mode, show progress
    if rounds_to_win:
        print(f"{Fore.CYAN}First to {rounds_to_win} wins!{Style.RESET_ALL}")

    print(f"{Fore.WHITE}{'=' * 40}{Style.RESET_ALL}")


def update_statistics(stats: GameStats, player_choice: Literal['rock', 'paper', 'scissors'], winner: Literal['player', 'computer', 'ties']) -> None:
    """
    Updates the statistics dictionary with the latest round data.

    Args:
        stats: Dictionary containing all statistics
        player_choice: What the player chose this round
        winner: Who won ('player', 'computer', or 'ties')
    """
    # Track total rounds
    stats['total_rounds'] += 1

    # Track choice frequency
    stats['choices'][player_choice] += 1

    # Update win streak
    if winner == "player":
        stats['current_streak'] += 1
        stats['longest_streak'] = max(
            stats['longest_streak'], stats['current_streak'])
    else:
        stats['current_streak'] = 0


def play_game() -> None:
    print(f"{Fore.GREEN}{Style.BRIGHT}{'=' * 40}")
    print(f"🎮 ROCK, PAPER, SCISSORS 🎮")
    print(f"{'=' * 40}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Type 'quit' or 'q' to exit anytime{Style.RESET_ALL}")

    # Get game mode
    rounds_to_win = get_best_of_n()

    if rounds_to_win == "QUIT_GAME":
        print(f"\n{Fore.CYAN}{Style.BRIGHT}Exiting game. Goodbye!{Style.RESET_ALL}")
        return

    # Initialize score
    score = {"player": 0, "computer": 0, "ties": 0}

    # Initialize statistics
    stats = {
        'total_rounds': 0,
        'choices': {'rock': 0, 'paper': 0, 'scissors': 0},
        'current_streak': 0,
        'longest_streak': 0
    }

    # Game loop
    while True:
        # Get player choice
        player_choice = get_player_choice()

        if player_choice is None:
            print(
                f"\n{Fore.CYAN}{Style.BRIGHT}Thanks for playing!{Style.RESET_ALL}")
            display_score(score, rounds_to_win)
            break

        # Get computer choice
        computer_choice = get_computer_choice()

        # Determine winner
        winner = determine_winner(player_choice, computer_choice)

        # Update score and statistics
        score[winner] += 1
        update_statistics(stats, player_choice, winner)

        # Display result
        display_round_result(player_choice, computer_choice, winner)
        display_score(score, rounds_to_win)

        # Check if someone won the match (best-of-N mode)
        if rounds_to_win:
            if score['player'] >= rounds_to_win:
                print(
                    f"\n{Fore.GREEN}{Style.BRIGHT}🏆 CONGRATULATIONS! YOU WON THE MATCH! 🏆{Style.RESET_ALL}")
                break
            elif score['computer'] >= rounds_to_win:
                print(
                    f"\n{Fore.RED}{Style.BRIGHT}💻 Computer won the match. Better luck next time!{Style.RESET_ALL}")
                break
        else:
            # Endless mode - ask if player wants to continue
            continue_game = input(
                f"\n{Fore.YELLOW}Play again? (y/n): {Style.RESET_ALL}").lower().strip()
            if continue_game not in ['y', 'yes']:
                print(
                    f"\n{Fore.CYAN}{Style.BRIGHT}Thanks for playing!{Style.RESET_ALL}")
                display_score(score, rounds_to_win)
                break


if __name__ == "__main__":
    play_game()
