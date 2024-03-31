from dataclasses import dataclass

from .factories import get_shape_factory
from .shapes import AbstractShape


def get_shape_config(shapes_config: dict, shape: str) -> dict:
    return shapes_config.get(shape, {})


@dataclass
class ShapeBuilder:
    shapes_config: dict

    def run(self, shape: str) -> AbstractShape:
        shape_config = get_shape_config(self.shapes_config, shape)
        shape_factory = get_shape_factory(shape)
        shape_instance = shape_factory.create(**shape_config)
        return shape_instance


def shape_builder_factory(config: dict) -> ShapeBuilder:
    return ShapeBuilder(config)
