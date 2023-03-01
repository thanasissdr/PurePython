from typing import List, Protocol

from dataclasses import dataclass, field


@dataclass
class ModelPerformance:
    _accuracy: float = 0.0
    observers: List = field(default_factory=lambda: [])

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    @property
    def accuracy(self):
        return self._accuracy

    @accuracy.setter
    def accuracy(self, value: float):
        self._accuracy = value
        self.notify()


class PerformanceObserver:
    def update(self, subject):
        print(f"Accuracy was updated to {subject.accuracy}")


if __name__ == "__main__":
    performance = ModelPerformance()
    observer = PerformanceObserver()

    performance.attach(observer)

    performance.accuracy = 0.80
    performance.accuracy = 0.75
    performance.accuracy = 0.60
