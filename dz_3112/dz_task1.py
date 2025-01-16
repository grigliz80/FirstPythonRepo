import random

win_phr = ['WOW! YOU DID IT!\n', 'BINGO!\n', 'YOU WON!\n', 'WINNER!\n'
            , 'GOOD BOY!\n', 'YOU GUESSED IT! BRAVO!\n']
los_phr = ['YOU LOSE\n', 'DEFEATED\n', 'ELIMINATED\n', 'TRY AGAIN\n'
            , 'NOT THIS TIME DUDE XD\n', 'MISSION FAILED\n']

game_is_running = True
attempt = 3

while game_is_running:
    s_u_number = input('Enter number between 1 and 10: ')

    if s_u_number.isdigit() == False:
        print('WRONG INPUT')
        continue
    else:    
        u_number = int(s_u_number)

        if u_number > 10 or u_number < 1:
            print('WRONG INPUT')
            continue
        else:
            c_number = random.randint(1, 10)
            print(f'YOU: {u_number}, CPU: {c_number}')

            if u_number == c_number:
                print('%s' % win_phr[random.randint(0, len(win_phr) - 1)])
            else:
                attempt -= 1
                print('%s %d ATTEMPTS LEFT\n' 
                    % (los_phr[random.randint(0, len(los_phr) - 1)], attempt))
                if attempt == 0:
                    game_is_running = False
else:
    print('GAME OVER!\n HAPPY NEW YEAR!')