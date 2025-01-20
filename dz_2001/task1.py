"""
Task 1
---------------
Write a Python program to detect the number
of local variables declared in a function.
"""

def test_function():
    earn = 80
    bonus = 16

    def tot_func(a, b):
        return a + b
    
    res = tot_func(earn, bonus)
    
    return res


def count_locals(func):
    func()
    return len(func.__code__.co_varnames)


print("Number of variables:", count_locals(test_function))