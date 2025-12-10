import random as rnd



def guessing_game_v1(min_number, max_number, max_guess_count) -> bool:
    """
    Run a complete guessing-game session and report whether the user wins.
    Takes a numeric range and a guess limit, executes the game once, and returns a boolean.

    :param min_number: Lowest selectable number in the game.
    :param max_number: Highest selectable number in the game.
    :param max_guess_count: Total number of guesses allowed to the player.
    """

    def validate_user_input(min_allowed: int, max_allowed: int) -> int:
        """
        Read user input and return a valid integer within the allowed range.
        Loops until the user enters an integer that fits the numeric boundaries.

        :param min_allowed: Minimum acceptable value.
        :param max_allowed: Maximum acceptable value.
        """
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
        """
        Run the internal game loop and evaluate each user guess.
        Generates a secret number, handles attempts, and returns True on success.

        :param min_ingame: Lowest possible secret number.
        :param max_ingame: Highest possible secret number.
        :param guess_limit: Number of attempts permitted.
        """
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

        return won

    return play_guessing_game(min_number, max_number, max_guess_count)



if __name__ == '__main__':
    guessing_game_v1(1,10,5)


# def better_guess_game():
#     # Game Rules.
#     min_number = 1
#     max_number = 10
#     answer = rnd.randint(min_number,max_number)
#     max_guess_count = 5
#     won = False
#     guess = None
#
#     # Welcome Message.
#     print("-" * 50)
#     print("Welcome to the Guessing Game!")
#     print(f"Try to guess the number between {min_number} and {max_number}.")
#     print("-" * 50)
#     print()
#
#     for i in range(1, max_guess_count + 1):
#
#         while True:
#             user_guess = input("Enter your guess: ")
#
#             try:
#                 guess = int(user_guess)
#             except ValueError:
#                 print(f"Invalid Answer; Must be an Integer.")
#                 continue
#             if guess < min_number or guess > max_number:
#                 print(f"Invalid Answer; Integer must be between {min_number} and {max_number}")
#                 continue
#
#             break
#
#         if guess == answer:
#             print(f"Congratulations! {answer} is Correct. You win! 🥳")
#             won = True
#             break
#
#         # Looping back to guess
#         elif i < max_guess_count:
#                 print("You guessed wrong. Try again."
#                       f"\nGuesses Left: {max_guess_count - i}/{max_guess_count}")
#
#     # Message when out of guesses
#     if not won:
#         print(f"You're out of guesses. You lose! The correct answer was {answer}")
# def guess_between_ten():
#     answer = rnd.randint(1,10)
#     guess_count = 1
#     guess = int(input("Guess a number between 1 and 10: "))
#
#     if guess == answer:
#         print("Hooray! You win! 👌")
#
#     else:
#         while guess != answer and guess_count < 5:
#             print(f"{5 - guess_count} Guesses left.")
#             guess = int(input("Wrong answer. Try again: "))
#             guess_count += 1
#             if guess_count == 5:
#                 print("Out guesses. You lose!")