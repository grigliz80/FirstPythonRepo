"""
Task 3
---------------
Write a function called "choose_func" which takes a list of nums and 2 callback functions.
If all nums inside the list are positive, execute the first function on that list and return
the result of it. Otherwise, return the result of the second one
"""

def choose_func(nums: list, func1, func2):
       
    if all(i >= 0 for i in nums):
         return func1(nums)
    else:
         return func2(nums)
    

def square_nums(nums_list):
        return [i ** 2 for i in nums_list]
    
def remove_negatives(num_list):
    return [i for i in num_list if i > 0]
    

print(choose_func([1, 2, 3, 4, 5], square_nums, remove_negatives))
print(choose_func([1, -2, 3, -4, 5], square_nums,remove_negatives))