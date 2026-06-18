from dataclasses import dataclass
from typing import Protocol, dataclass_transform


class Runner(Protocol):
    def run(self) -> None: ...


REGISTRY: dict[str, type[Runner]] = {}


@dataclass_transform()
def register(cls: type[Runner]) -> None:
    dclass = dataclass(cls)
    REGISTRY[cls.__name__] = dclass


@register
class A:
    def run(self):
        print("Running A")


@register
class B:
    def run(self):
        print("Running B")


def get_from_registry(cls_name: str) -> type[Runner]:
    cls = REGISTRY.get(cls_name)
    if cls is None:
        raise KeyError(f"Class {cls_name} not found in registry")
    return cls


def main(cls_name: str) -> None:
    print(REGISTRY)
    cls = get_from_registry(cls_name)
    cls().run()


if __name__ == "__main__":
    main("C")
