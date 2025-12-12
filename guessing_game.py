import random as rnd




def validate_user_input(min_allowed: int, max_allowed: int) -> int:
    """Return a valid integer guess within range."""

    while True:
        user_guess = input("Enter your guess: ")
        try:
            guess = int(user_guess)
        except ValueError:
            print(f"Invalid Answer. Must be an Integer.")
            continue
        if guess < min_allowed or guess > max_allowed:
            print(f"Invalid Answer. Integer must be between {min_allowed} and {max_allowed}")
            continue

        return guess

def play_guessing_game(min_ingame, max_ingame, guess_limit) -> bool:
    """Run the guessing loop and report win/lose."""

    answer = rnd.randint(min_ingame, max_ingame)
    won = False

    for attempts in range(1, guess_limit + 1):
        guess = validate_user_input(min_ingame, max_ingame)

        if guess == answer:
            print(f"{answer} is correct! You won!")
            won = True
            break

        elif attempts < guess_limit:
            print("Wrong. Try again.")
            print("Guesses Left:", guess_limit - attempts)
            print("." * 50)

    if not won:
        print(f"You Lose. The correct answer was {answer}")




if __name__ == '__main__':
    play_guessing_game(min_ingame=1, max_ingame=10, guess_limit=5)