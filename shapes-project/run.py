import pprint as pp
from functools import partial

from src.shapes.build import AbstractShape, shape_builder_factory
from src.utils import load_json


def create_shape(config_path: str, shape: str) -> AbstractShape:
    config = load_json(config_path)
    shape_builder = shape_builder_factory(config)
    shape_instance = shape_builder.run(shape)
    return shape_instance


def main(config_path: str, shape: str) -> dict:
    shape_obj = create_shape(config_path, shape)
    shape_area = shape_obj.get_area()
    shape_perimeter = shape_obj.get_perimeter()

    return {
        "shape": shape_obj,
        "shape_area": shape_area,
        "shape_perimeter": shape_perimeter,
    }


if __name__ == "__main__":
    CONFIG_PATH = "./shapes-project/config.json"
    main_fixed_config = partial(main, config_path=CONFIG_PATH)

    SHAPE = "rectangle"
    pp.pprint(main_fixed_config(shape=SHAPE))
