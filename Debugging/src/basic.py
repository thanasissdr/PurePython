import numpy as np


class Simple:
    def __init__(self, a):
        self.a = a

    def squared(self):
        return self.a ** 2

    def __str__(self):
        return self.a
