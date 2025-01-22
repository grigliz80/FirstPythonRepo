"""
Task1
----------------------
Write a decorator that prints a function with arguments passed to it.
Note! It should print the function, not the result of its execution!
"""


def dec_logger(func):
    def wrapper(*args, **kwargs):
        its_args = ', '.join(map(str, args)) if args else ''
        its_kwargs = ', '.join(f'{k}={v}' for k, v in  kwargs.items()) if kwargs else ''
        if args and kwargs:
            print(f'{func.__name__} called with: {its_args}, {its_kwargs}')
        elif args:
            print(f'{func.__name__} called with: {its_args}')
        elif kwargs:
            print(f'{func.__name__} called with: {its_kwargs}')
        else:
            print(f'{func.__name__} called without any incoming data')       
        return func(*args, **kwargs)
    return wrapper


@dec_logger
def hello_world():
    return 'Hello, world!'


@dec_logger
def add(x, y):
    return x + y


@dec_logger
def square_func(*args):
    return [i**2 for i in args]


@dec_logger
def func_with_dict(*args, **kwargs):
    return list(args) + [f'{k} is {v}' for k, v in kwargs.items()]


def main():
    hello_world()
    add(2, 7)
    square_func(2, 3, 5, 7)
    func_with_dict(22, 'January', 2025, name='Grigoriy',age=44, is_programmer=True)


if __name__ == '__main__':
    main()