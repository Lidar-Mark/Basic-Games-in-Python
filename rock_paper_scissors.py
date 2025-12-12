import random as rnd

"""
This is a game of Rock Paper Scissors.

In this game there 2 'Users', 1 is a Human and the 2nd is a Computer.
the Rules to win a round of R. P. S. are simple:
    Rock < Paper.
    Paper < Scissors.
    Scissors < Rock.

Inorder to win the game, 1 of the Users need to score a total score (Wins) of 3.
"""

# Win-Map: defines which choice beats which.
WIN_MAP = {
    frozenset(["paper", "rock"]): "paper",
    frozenset(["rock", "scissors"]): "rock",
    frozenset(["scissors", "paper"]): "scissors",
}

# Allowed inputs for the game.
CHOICES = ("rock", "paper", "scissors")


def get_user_input():
    """Reads and validates a user's choice until a legal value is entered."""
    while True:
        user_input = input("Rock, Paper, Scissors – Shoot!: ").lower().strip()
        if user_input not in CHOICES:
            print("Try again.")
            continue
        return user_input


# Computer Output
def get_computer_choice():
    """Randomly selects rock, paper, or scissors for the computer."""
    return rnd.choice(CHOICES)


# Results of a round
def game_round():
    """Runs a single round and returns who won: USER, COMPUTER, or DRAW."""
    user_input = get_user_input()
    computer_input = get_computer_choice()

    if user_input == computer_input:
        print(f"DRAW! Both players choose {user_input}")
        return "DRAW"

    winner = WIN_MAP[frozenset((user_input, computer_input))]

    if winner == user_input:
        print(f"User WON! {user_input.capitalize()} > {computer_input.capitalize()}")
        return "USER"
    else:
        print(f"Computer WON! {computer_input.capitalize()} > {user_input.capitalize()}")
        return "COMPUTER"


def play_rock_paper_scissors():
    """Runs full game logic until either player reaches 3 wins."""
    player_score = 0
    computer_score = 0

    while player_score < 3 and computer_score < 3:
        result = game_round()

        if result == "USER":
            player_score += 1
        elif result == "COMPUTER":
            computer_score += 1

        print(f"SCORE: Player {player_score} | Computer {computer_score}")

    if player_score == 3:
        print("PLAYER HAS WON!")
    else:
        print("COMPUTER HAS WON!")


if __name__ == "__main__":
    play_rock_paper_scissors()
