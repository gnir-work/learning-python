import inspect
from typing import Callable


class NoSuchMethod(Exception):
    pass


def get_overloaded_functions_key(func):
    return f"{func.__name__}-overloads"


def overload(func: Callable):
    """
    A decorator which allows overlaoding the wrapped function.
    Currently the overlaoding takes into account only the number of parameters, however
    in the future this functionality can be extended to take into account kwargs and
    type hints.
    :param func: The function that should support overloading.
    """
    # The upper frame which contains the created function before the class is created.
    class_creation_frame = inspect.stack()[1].frame

    # Extract the cached functions by number of parameters
    overloaded_functions = class_creation_frame.f_locals.get(
        get_overloaded_functions_key(func), dict()
    )

    # Add the current function
    overloaded_functions[func.__code__.co_argcount] = func

    # Save the new mapping
    class_creation_frame.f_locals[get_overloaded_functions_key(func)] = overloaded_functions

    def overloaded_function(*args):
        """
        Custom function which returns the corresponding overloaded
        function by number of paramters
        """
        try:
            overloaded_function = overloaded_functions[len(args)]
        except KeyError as e:
            raise NoSuchMethod(
                f"No overload for {func.__name__} with {len(args)} parameters"
            ) from e
        else:
            return overloaded_function(*args)

    return overloaded_function


@overload
def first_function():
    print('hello1')


@overload
def first_function(num: int):
    print('hello2', num)


if __name__ == "__main__":
    first_function()
    first_function(10)
