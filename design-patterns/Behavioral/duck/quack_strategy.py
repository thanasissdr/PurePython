from abc import ABC, abstractmethod


class QuackStrategy(ABC):
    @abstractmethod
    def quack(self):
        pass


class LoudQuack(QuackStrategy):
    def quack(self):
        return "QUACK QUACK!"


class GentleQuack(QuackStrategy):
    def quack(self):
        return "quack"
