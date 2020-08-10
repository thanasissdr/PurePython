from functools import wraps


def exceptions(g):
    def wrapper(f):
        @wraps(f)
        def inner(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except g() as z:
                print(f"{z} in {f.__name__} function.")

        return inner

    return wrapper


@exceptions
def division_handler():
    return ZeroDivisionError


@exceptions
def type_handler():
    return TypeError


@division_handler
@type_handler
def division(a, b):
    return a / b


print(division(20, 10))

print(division(20, "a"))

print(division(20, 0))

print(division)
