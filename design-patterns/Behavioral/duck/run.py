from lights_strategy import TenSeconds
from quack_strategy import LoudQuack, GentleQuack


class Duck:
    def __init__(self, quack_strategy, light_strategy):
        self.quack_strategy = quack_strategy
        self.light_strategy = light_strategy

    def quack(self):
        return self.quack_strategy.quack()

    def lights_on(self):
        return self.light_strategy.lights_on()


# Types of Ducks
class VillageDuck(Duck):
    def __init__(self):
        super().__init__(LoudQuack(), None)


class GentleDuck(Duck):
    def __init__(self):
        super().__init__(GentleQuack(), None)


class RobotDuck(Duck):
    def __init__(self):
        super().__init__(GentleQuack(), TenSeconds())


print(VillageDuck().quack())
print("\n")
print(GentleDuck().quack())
print("\n")
robot_duck = RobotDuck()
print(robot_duck.quack())
print(robot_duck.lights_on())
