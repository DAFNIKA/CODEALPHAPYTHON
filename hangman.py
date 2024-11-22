import random

# Hangman stages
HANGMAN_PICS = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# Word list
WORDS = ["python", "programming", "hangman", "challenge", "developer", "code"]


def get_word():
    return random.choice(WORDS).upper()


def display_game(hangman_pics, word_completion, wrong_guesses):
    print(hangman_pics[len(wrong_guesses)])
    print(f"Word: {word_completion}")
    print(f"Wrong guesses: {', '.join(wrong_guesses)}")


def play_game():
    word = get_word()
    word_completion = "_" * len(word)
    guessed = False
    wrong_guesses = []
    correct_guesses = set()

    print("Welcome to Hangman!")

    while not guessed and len(wrong_guesses) < len(HANGMAN_PICS) - 1:
        display_game(HANGMAN_PICS, word_completion, wrong_guesses)
        guess = input("Guess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
        elif guess in correct_guesses or guess in wrong_guesses:
            print("You already guessed that letter.")
        elif guess in word:
            print(f"Good guess! {guess} is in the word.")
            correct_guesses.add(guess)
            word_completion = "".join(
                [letter if letter in correct_guesses else "_" for letter in word]
            )
            if "_" not in word_completion:
                guessed = True
        else:
            print(f"Sorry, {guess} is not in the word.")
            wrong_guesses.append(guess)

    if guessed:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        display_game(HANGMAN_PICS, word_completion, wrong_guesses)
        print(f"Game over! The word was: {word}")


# Run the game
if __name__ == "__main__":
    play_game()
