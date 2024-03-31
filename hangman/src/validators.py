from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class InputValidator(ABC):
    def run(self, input_str: str) -> bool:
        input_is_valid = self.input_is_valid(input_str)
        if not input_is_valid:
            self.set_message()
        return input_is_valid

    @abstractmethod
    def input_is_valid(self, input_str: str) -> bool:
        pass

    @abstractmethod
    def set_message(self) -> None:
        pass


class InputIsASingleCharacter(InputValidator):
    def input_is_valid(self, input_str):
        return len(input_str) == 1

    def set_message(self):
        print("Input should be a single character")


@dataclass
class InputHasNotBeenUsed(InputValidator):
    used_chars: set[str] = field(default_factory=set)

    def input_is_valid(self, input_str):
        res = input_str not in self.used_chars
        if res:
            self.used_chars.add(input_str)
        return res

    def set_message(self):
        print("Input should be a non used letter")


class InputIsLower(InputValidator):
    def input_is_valid(self, input_str: str) -> bool:
        return input_str.islower()

    def set_message(self) -> None:
        print("Input should be in lowercase")


class InputIsAlpha(InputValidator):
    def input_is_valid(self, input_str):
        return input_str.isalpha()

    def set_message(self) -> None:
        print("Input should be a letter")
