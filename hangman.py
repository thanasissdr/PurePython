import getpass
from enum import Enum
from typing import List, Tuple


class HangmanStates(Enum):

    ONE = (
        "   _____ \n"
        "  |      \n"
        "  |      \n"
        "  |      \n"
        "  |      \n"
        "  |      \n"
        "  |      \n"
        "__|__\n"
    )

    TWO = (
        "   _____ \n"
        "  |     | \n"
        "  |     |\n"
        "  |      \n"
        "  |      \n"
        "  |      \n"
        "  |      \n"
        "__|__\n"
    )

    THREE = (
        "   _____ \n"
        "  |     | \n"
        "  |     |\n"
        "  |     | \n"
        "  |      \n"
        "  |      \n"
        "  |      \n"
        "__|__\n"
    )

    FOUR = (
        "   _____ \n"
        "  |     | \n"
        "  |     |\n"
        "  |     | \n"
        "  |     O \n"
        "  |      \n"
        "  |      \n"
        "__|__\n"
    )

    FIVE = (
        "   _____ \n"
        "  |     | \n"
        "  |     |\n"
        "  |     | \n"
        "  |     O \n"
        "  |    /|\ \n"
        "  |    / \ \n"
        "__|__\n"
    )


def set_hangman_state():
    yield HangmanStates.ONE
    yield HangmanStates.TWO
    yield HangmanStates.THREE
    yield HangmanStates.FOUR
    yield HangmanStates.FIVE


def find_char_index(input_string: str, char: str) -> List[int]:
    char_indices = []
    for idx, i in enumerate(input_string):
        if i == char:
            char_indices.append(idx)
    return char_indices


def word_is_found(hidden_word: str, input_string: str) -> bool:
    return hidden_word == input_string


def replace_guess_in_hidden(
    input_string: str, guess: str, hidden_word_list: List[str]
) -> Tuple[str, List]:
    guess_indices = find_char_index(input_string, guess)
    if guess_indices:
        for guess_index in guess_indices:
            hidden_word_list[guess_index] = guess
    hidden_word = "".join(hidden_word_list)
    return hidden_word, hidden_word_list


def run(input_string: str, n_tries: int = 5) -> None:
    hidden_word = "-" * len(input_string)
    hidden_word_list = list(hidden_word)

    used_letters = set()
    hangman_state = set_hangman_state()

    print("\nRemaining n_tries:", n_tries)
    while n_tries > 0:
        guess = input("\nPlease insert a letter:")

        while guess in used_letters:
            guess = input("\nPlease insert a letter you haven't tried previously:")
        used_letters.add(guess)

        if guess in input_string:
            hidden_word, hidden_word_list = replace_guess_in_hidden(
                input_string, guess, hidden_word_list
            )

            word_found = word_is_found(input_string, hidden_word)
            if word_found:
                print(f"\CONGRATULATIONS! The hidden word was: {input_string}")
                return None

        else:

            print(next(hangman_state).value)
            n_tries -= 1

        if n_tries > 0:
            print("\nRemaining n_tries:", n_tries)
            print("Hidden word:", hidden_word)
        else:
            print(f"The hidden word was: {input_string}")


if __name__ == "__main__":
    hidden_input = getpass.getpass("Please insert a word:")
    run(hidden_input)
