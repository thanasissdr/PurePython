import getpass
from abc import ABC, abstractmethod
from enum import Enum
from typing import Callable, Dict, List, Tuple

from dataclasses import dataclass, field


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


def set_hangman_state() -> Callable:
    for hangman_state in [
        HangmanStates.ONE,
        HangmanStates.TWO,
        HangmanStates.THREE,
        HangmanStates.FOUR,
        HangmanStates.FIVE,
    ]:
        yield hangman_state


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


class InputGuessValidator(ABC):
    @abstractmethod
    def run(self, guess: str):
        pass


class AlphaValidator(InputGuessValidator):
    def run(self, guess: str) -> bool:
        return guess.isalpha()


@dataclass
class NotInUsedLettersValidator(InputGuessValidator):
    used_letters: List[str] = field(default_factory=list)

    def run(self, guess: str) -> bool:
        return guess not in self.used_letters


def validate_input_string(
    guess: str, validators: Dict[str, InputGuessValidator]
) -> str:
    while True:
        input_string_is_valid = [
            validator.run(guess) for validator in validators.values()
        ]
        if all(input_string_is_valid):
            return guess
        else:
            guess = input("Please enter a valid guess: ")


class HangmanRunner:
    def __init__(self, n_tries: int = 5):
        self.n_tries = n_tries
        self.used_letters = []
        self.validators = {
            "is_alpha": AlphaValidator(),
            "not_in_used_letters": NotInUsedLettersValidator(),
        }

    def update_validators(self) -> None:
        self.validators["not_in_used_letters"].used_letters = self.used_letters

    def run(self, input_string) -> None:
        hidden_word = "-" * len(input_string)
        print(hidden_word)
        hidden_word_list = list(hidden_word)

        hangman_state = set_hangman_state()

        print("\nRemaining n_tries: ", self.n_tries)
        while self.n_tries > 0:
            print(f"Used letters: {self.used_letters}")
            guess = input("\nPlease insert a letter: ")
            guess = validate_input_string(guess, self.validators)

            self.used_letters.append(guess)
            self.update_validators()

            if guess in input_string:
                hidden_word, hidden_word_list = replace_guess_in_hidden(
                    input_string, guess, hidden_word_list
                )

                word_found = word_is_found(input_string, hidden_word)
                if word_found:
                    print(f"\nCONGRATULATIONS! :) The hidden word was: {input_string}")
                    return None

            else:
                print(next(hangman_state).value)
                self.n_tries -= 1

            if self.n_tries > 0:
                print("\nRemaining n_tries:", self.n_tries)
                print("Hidden word:", hidden_word)
            else:
                print(f"\nSORRY! :( The hidden word was: {input_string}")


if __name__ == "__main__":
    hidden_input = getpass.getpass("Please insert a word: ")
    validators = [AlphaValidator(), NotInUsedLettersValidator()]
    runner = HangmanRunner(n_tries=5)
    print(runner.run(hidden_input))
