from abc import abstractmethod, ABC


class LightStrategy(ABC):
    @abstractmethod
    def lights_on(self):
        pass


class TenSeconds(LightStrategy):
    def lights_on(self):
        return "Lights on for 10 seconds"

