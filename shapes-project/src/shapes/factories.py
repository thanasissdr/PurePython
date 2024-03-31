from .shapes import Rectangle, Square, Triangle


class SquareFactory:
    def create(self, a: float) -> Square:
        return Square(a)


class RectangleFactory:
    def create(self, a: float, b: float) -> Rectangle:
        return Rectangle(a, b)


class TriangleFactory:
    def create(self, a: float, b: float, c: float) -> Triangle:
        return Triangle(a, b, c)


def get_shape_factory(shape: str) -> SquareFactory | RectangleFactory | TriangleFactory:
    available_shape_factories = {
        "square": SquareFactory(),
        "rectangle": RectangleFactory(),
        "triangle": TriangleFactory(),
    }

    selected_shape_factory = available_shape_factories.get(shape)
    if selected_shape_factory is None:
        raise KeyError(
            f"Shape factory is not supported for shape '{shape}'. Available shapes are: {list(available_shape_factories)}"
        )

    return selected_shape_factory
