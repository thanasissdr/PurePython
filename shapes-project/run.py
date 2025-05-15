import pprint as pp
from functools import partial

from src.shapes.factories import get_shape_factory
from src.shapes.shapes import AbstractShape
from src.utils.file.read import load_json


def get_shape_from_config(config: dict, shape: str) -> AbstractShape:
    shape_config = config.get(shape, {})
    shape_factory = get_shape_factory(shape)
    return shape_factory.create(**shape_config)


def get_shape_chars(shape: AbstractShape) -> dict:
    shape_area = shape.get_area()
    shape_perimeter = shape.get_perimeter()

    return {
        "shape": shape.__class__.__name__,
        "shape_params": shape.get_params(),
        "shape_area": shape_area,
        "shape_perimeter": shape_perimeter,
    }


def run(config_path: str, shape: str) -> dict:
    config = load_json(config_path)
    shape_instance = get_shape_from_config(config, shape)
    return get_shape_chars(shape_instance)


def main():
    CONFIG_PATH = "config.json"
    main_fixed_config = partial(run, config_path=CONFIG_PATH)

    SHAPE = "circle"
    pp.pprint(main_fixed_config(shape=SHAPE))


if __name__ == "__main__":
    main()
