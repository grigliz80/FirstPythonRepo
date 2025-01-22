"""
Task2
----------------------
Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
"""


def stop_words(words: list):
    def dec_wrap(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            for word in words:
                res = res.replace(word, '*')
            return res
        return wrapper
    return dec_wrap


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str):
    return f'{name} drinks pepsi in his brand new BMW'


def main():
    print(create_slogan('Mykola'))


if __name__ == '__main__':
    main()