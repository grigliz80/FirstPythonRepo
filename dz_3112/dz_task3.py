import random

my_string = input('Write here: ')
    
for _ in range(5):
    o_l_ms = list(my_string)
    random.shuffle(o_l_ms)
    print(''.join(o_l_ms))