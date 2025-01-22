"""
Task3
----------------------
Write a decorator 'arg_rules' that validates arguments passed to the function.

A decorator should take 3 arguments:
- type_: str
- max_length: 15
- contains: []  - list of symbols that an argument should contain

If some of the rules' checks returns False, the function should return False and print
the reason it failed; otherwise, return the result.
"""


def arg_rules(type_: type, max_length: int, contains: list):
    def dec_wrap(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, type_):
                    print(f'Failed: Argument "{arg}" is not type of type {type_.__name__}.')
                    return False
                if len(arg) > 15:
                    print(f'Failed: Argument "{arg}" exceeds maximum of {max_length}.')
                    return False
                if not all(symb in arg for symb in contains):
                    miss = [sym for sym in contains if sym not in arg]
                    print(f'Failed: Argument "{arg}" is missing required symbols: {miss}')
                    return False
                else:
                    print(func(*args, **kwargs))              
            return func(*args, **kwargs)
        return wrapper
    return dec_wrap


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f'{name} drinks pepsi in his brand new BMW!'


def main():
    create_slogan('Fefir Stepanovych')
    create_slogan(5005)
    create_slogan('yan07@gmail.com')
    create_slogan('yan05@gmail.com')


if __name__ == '__main__':
    main()