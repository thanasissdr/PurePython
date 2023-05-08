import getpass

from abc import ABC, abstractmethod
from enum import Enum
from typing import Callable, Dict, List, Optional, Tuple

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
    return [idx for idx, c in enumerate(input_string) if c == char]


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

    @abstractmethod
    def update_guess(self):
        pass


class AlphaValidator(InputGuessValidator):
    def run(self, guess: str) -> bool:
        return guess.isalpha()

    def update_guess(self) -> str:
        return input("Please insert a letter and not any other symbol: ")


@dataclass
class NotInUsedLettersValidator(InputGuessValidator):
    used_letters: List[str] = field(default_factory=list)

    def run(self, guess: str) -> bool:
        return guess not in self.used_letters

    def update_guess(self) -> str:
        return input("Please insert a letter you have not used before: ")


@dataclass
class SingleCharacterValidator(InputGuessValidator):
    def run(self, guess: str) -> bool:
        return len(guess) == 1

    def update_guess(self) -> str:
        return input("Please insert only a single character: ")


def validate_input_string(
    guess: str, validators: Dict[str, InputGuessValidator]
) -> str:
    guess_is_valid = False
    while not guess_is_valid:
        for validator in validators.values():
            if not validator.run(guess):
                guess = validator.update_guess()
                return validate_input_string(guess, validators)
            else:
                continue
        guess_is_valid = True

    return guess


class HangmanRunner:
    def __init__(
        self,
        validators: Optional[Dict[str, List[InputGuessValidator]]] = None,
        n_tries: int = 5,
    ):
        self.n_tries = n_tries
        self.used_letters = []
        self.validators = validators if validators else {}

    def update_validators(self) -> None:
        self.update_not_in_used_letters_validator()

    def update_not_in_used_letters_validator(self):
        not_in_used_letters_validator = self.validators.get("not_in_used_letters", None)
        if not_in_used_letters_validator is not None:
            not_in_used_letters_validator.used_letters = self.used_letters

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

                if input_string == hidden_word:
                    self.set_game_success_message(input_string)
                    return None

            else:
                print(next(hangman_state).value)
                self.n_tries -= 1

            self.set_game_status(self.n_tries, hidden_word, input_string)

    def set_game_status(
        self, n_tries: int, hidden_word: str, input_string: str
    ) -> None:
        if n_tries > 0:
            print("\nRemaining n_tries:", n_tries)
            print("Hidden word:", hidden_word)
        else:
            print(f"\nSORRY! :( The hidden word was: {input_string}")

    def set_game_success_message(self, input_string) -> None:
        print(f"\nCONGRATULATIONS! :) The hidden word was: {input_string}")
        return None


if __name__ == "__main__":
    hidden_input = getpass.getpass("Please insert a word: ")
    validators = {
        "is_alpha": AlphaValidator(),
        "not_in_used_letters": NotInUsedLettersValidator(),
        "is_single_character": SingleCharacterValidator(),
    }
    runner = HangmanRunner(n_tries=5, validators=validators)
    print(runner.run(hidden_input))
