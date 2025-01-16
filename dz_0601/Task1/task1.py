# mod_second
def very_long_name_function_for_adding_numbers(a, b):
    return a + b


# mod_first
from mod_second import very_long_name_function_for_adding_numbers as adder

print(adder(18, 2))