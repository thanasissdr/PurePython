from abc import abstractstaticmethod, ABC


class Child:
    def __init__(self, expensive_object=None):
        self.expensive_object = expensive_object


class Child1(Child):
    def run(self):
        return self.expensive_object + 10


class Child2(Child):
    def run(self):
        return self.expensive_object + 20


class IChildBuilder(ABC):
    @abstractstaticmethod
    def add_expensive_object(self):
        return NotImplemented


class ChildBuilder(IChildBuilder):
    def __init__(self, child: Child = None):

        if child:
            self.child = child
        else:
            self.child = Child()

    def add_expensive_object(self, value):
        self.child.expensive_object = value
        return self

    def build(self):
        return self.child
