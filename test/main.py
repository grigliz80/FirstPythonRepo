# The first steps to "Guessin Words By Letter" application
# Please don't touch any modules related to this file

import random
from modules.data import quiz_pairs

cubick = random.randint(0, len(quiz_pairs) - 1)
tsk = quiz_pairs[cubick][1]
tsk_dscr = quiz_pairs[cubick][0]

print(tsk + '\n')
print(tsk_dscr + '\n')

while True:

    u_inp = input("Enter letter here: ")

    if u_inp.upper() not in tsk.upper() or len(u_inp) > 1:
        print('TRY AGAIN')
        continue
    else:
        print('YESTY TAKAYA BUKVAAA!', u_inp.upper())

