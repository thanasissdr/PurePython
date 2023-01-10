from enum import Enum
from typing import List, Protocol

class Connection(Enum):
    OFF = 0
    ON  = 1


class Device(Protocol):

    def connect(self):
        ...
    def disconnect(self):
        ...

    def get_status(self):
        if self.is_connected == Connection.OFF:
                return self.disconnect()
        elif self.is_connected == Connection.ON:
            return self.connect()
        else:
            raise ValueError(f"{self.is_connected} is not supported.")


class SmartLight(Device):

    def __init__(self, is_connected = Connection.OFF):
        self.is_connected = is_connected

    def connect(self) -> None:
        self.is_connected = Connection.ON
        print("Smart light connected")

    def disconnect(self) -> None:
        self.is_connected = Connection.OFF
        print("Smart light disconnected")
        

class SmartSpeaker(Device):

    def __init__(self, is_connected = Connection.ON):
        self.is_connected = is_connected

    def connect(self) -> None:
        self.is_connected = Connection.ON
        print("Smart speaker connected")

    def disconnect(self) -> None:
        self.is_connected = Connection.OFF
        print("Smart speaker disconnected")


def get_devices_status(devices: List[Device]):
    for device in devices:
        device.get_status()

if __name__ == "__main__":
    get_devices_status([SmartLight(is_connected=Connection.OFF), SmartSpeaker()])