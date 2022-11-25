from pass_expensive_object.expensive_function import run_expensive_function
from pass_expensive_object.child import Child, ChildBuilder, Child1, Child2


class BaseRunner:
    def get_expensive_object(self, seconds=3):
        self.expensive_object = run_expensive_function(seconds)

    def _build_child(self, child: Child):
        child_builder = ChildBuilder(child)
        child_builder.add_expensive_object(self.expensive_object)
        return child_builder.build()

    def run(self, child: Child):
        self._build_child(child)
        return child.run()


class Main:
    def setup(self, seconds=3):
        self.base_runner = BaseRunner()
        self.base_runner.get_expensive_object(seconds)

    def run(self, child):
        return self.base_runner.run(child)


if __name__ == "__main__":
    main = Main()
    main.setup(seconds=4)

    ch1 = Child1()
    ch2 = Child2()

    print(main.run(ch1))
    print(main.run(ch2))
