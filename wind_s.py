import sys
from termcolor import colored, cprint

logo = '''
                    Welcome to the GAME!

            A LONG STORY OF ADVENTURER AND FRIENDS
       '''

menu = '''
            ******************************************************************************************************************************
            *                                                                                                                            *
            *                                                   1. Play                                                                  *
            *                                                   2. Continue                                                              *
            *                                                   3. Load                                                                  *
            *                                                   4. Options                                                               *
            *                                                   5. Exit                                                                  *
            *                                                                                                                            *
            ******************************************************************************************************************************
       '''

pause = '''
                    1. Return to game
                    2. Save game
                    3. Load game
                    4. Settings
                    5. Main Menu
                    6. Exit
        '''


def start_win():    
    cprint(logo, 'red', attrs=['blink', 'bold'])
    print(menu)
    op = int(input("==> "))
    if op == 1:
        return 1
    elif op == 2:
        return 2
    elif op == 3:
        return 3
    elif op == 4:
        return 4
    elif op == 5:
        return 5
    else:
        start_win() 


def pause_win():
    print(pause)
    op = int(input("==> "))
    if op == 1:
        return 1
    elif op == 2:
        return 2
    elif op == 3:
        return 3
    elif op == 4:
        return 4
    elif op == 5:
        return 5
    elif op == 6:
        return 6
    else:
        pause_win() 
