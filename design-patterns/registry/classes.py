from functools import wraps

config = {}


def register_class_type(cls):
    @wraps(cls)
    def inner():
        return cls

    print(f"Registering class type {cls.__name__}")
    config[cls.__name__] = cls

    return inner


@register_class_type
class A:
    pass


@register_class_type
class B:
    pass


if __name__ == "__main__":
    print(config)
