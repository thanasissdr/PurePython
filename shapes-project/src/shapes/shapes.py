import math
from abc import ABC, abstractmethod
from dataclasses import dataclass


class AbstractShape(ABC):
    pass

    @abstractmethod
    def get_area(self) -> float:
        pass

    @abstractmethod
    def get_perimeter(self) -> float:
        pass


@dataclass
class Square(AbstractShape):
    a: float

    def get_area(self) -> float:
        return self.a**2

    def get_perimeter(self) -> float:
        return 4 * self.a


@dataclass
class Rectangle(AbstractShape):
    a: float
    b: float

    def get_area(self) -> float:
        return self.a * self.b

    def get_perimeter(self) -> float:
        return 2 * self.a + 2 * self.b


@dataclass
class Triangle(AbstractShape):
    a: float
    b: float
    c: float

    def get_area(self) -> float:
        semi_perimeter = self._get_semiperimeter()

        # Calculate the area using Heron's formula
        area = math.sqrt(
            semi_perimeter
            * (semi_perimeter - self.a)
            * (semi_perimeter - self.b)
            * (semi_perimeter - self.c)
        )
        return area

    def _get_semiperimeter(self):
        return self.get_perimeter() / 2

    def get_perimeter(self):
        return self.a + self.b + self.c
