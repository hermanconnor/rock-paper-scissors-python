CHOICES: list[str] = ["rock", "paper", "scissors"]

BEATS: dict[str, str] = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

INPUT_MAP: dict[str, str] = {
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
