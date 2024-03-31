import getpass

from src.validators import (
    InputHasNotBeenUsed,
    InputIsAlpha,
    InputIsASingleCharacter,
    InputIsLower,
    InputValidator,
)

VALIDATORS = [
    InputIsASingleCharacter(),
    InputIsAlpha(),
    InputIsLower(),
    InputHasNotBeenUsed(),
]


def run_hangman(
    n_tries: int = 5, input_validators: list[InputValidator] | None = None
) -> None:
    input_word = getpass.getpass("Please enter a word: ")

    n_chars = len(input_word)
    encrypted_word = "-" * n_chars

    input_word_list = list(input_word)
    encrypted_word_list = list(encrypted_word)

    while n_tries > 0:
        if encrypted_word_list == input_word_list:
            print("SUCCESS!")
            return

        user_input = input("\nPlease enter a letter: ")

        if input_validators:
            user_input = validate_user_input(
                user_input, input_validators, n_tries, encrypted_word_list
            )

        if user_input in input_word_list:
            for idx, letter in enumerate(input_word_list):
                if user_input == letter:
                    encrypted_word_list[idx] = letter
            print("".join(encrypted_word_list))

        else:
            n_tries -= 1
            print(f"Number of remaining tries: {n_tries}")

    print(f"\nUnfortunately! :( The hidden word was '{input_word}'")


def validate_user_input(
    user_input: str,
    input_validators: list[InputValidator],
    n_tries: int,
    encrypted_word_list: list[str],
) -> str:
    user_input_is_valid = False

    while not user_input_is_valid:
        for input_validator in input_validators:
            if not input_validator.run(user_input):
                print(f"Number of remaining tries: {n_tries}")
                print("".join(encrypted_word_list))
                user_input = input("\nPlease enter a valid letter: ")
                break
        else:
            user_input_is_valid = True

    return user_input


if __name__ == "__main__":
    run_hangman(input_validators=VALIDATORS)
