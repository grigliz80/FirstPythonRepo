"""
Task 2
---------------
Write a Python program to access a function inside a function
(Tips: use function, which returns another function)
"""

#---------V1---------------
def test_func(x, y):

    def adder(a, b):
        return a + b
    
    return adder(x, y)


#---------V2---------------
def outer_func():
    def inner_func():
        return 'Hello from inner function!'
    return inner_func


my_variable = outer_func()

#----------------------------------------
def main():
    
    print(test_func(5, 7))
    print(my_variable())


if __name__ == '__main__':
    main()