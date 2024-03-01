from time import sleep
from random import randint
from pw5_2 import cleargrid
from pw5_3 import showgrid
from pw5_5 import move
from pw5_6 import four
from pw5_8 import recom2

grid = [
    ['  ','1 ','2 ','3 ','4 ','5 ','6 ','7 ',''],
    ['6 ','  ', '  ','  ','  ','  ','  ','  ','6'],
    ['5 ','  ', '  ','  ','  ','  ','  ','  ','5'],
    ['4 ','  ', '  ','  ','  ','  ','  ','  ','4'],
    ['3 ','  ', '  ','  ','  ','  ','  ','  ','3'],
    ['2 ','  ', '  ','  ','  ','  ','  ','  ','2'],
    ['1 ','  ', '  ','  ','  ','  ','  ','  ','1'],
    ['  ','1 ','2 ','3 ','4 ','5 ','6 ','7 ','']   
]


def mover():
    '''This function is a sum of all that's happening while the player makes its move. Put together so it's easier to write the game'''
    sleep(1)
    recom2(grid)
    sleep(2)
    m = int(input('\nNext move: write the number of the column to put your disc in.\n'))
    move(grid,m,'o ')
    showgrid(grid)
    sleep(1)
    four(grid)

def game():
    '''The game of Connect4 put together with all the modules. Finally!'''

    print("\n\n\nHello and welcome to Connect 4!\n")
    sleep(2)
    print("You will be playing against a machine.")
    sleep(1)
    print('Your disks will be shown as the letter o.\n')
    sleep(2)
    print('Okay,')
    sleep(0.5)
    print("We will now start the game!\n")
    cleargrid(grid)
    showgrid(grid)
    sleep(1)
    m = int(input('\nFirst move is yours! Just write the number of the column you want to put your disc in.\n'))
    move(grid,m,'o ')
    print('\n')
    showgrid(grid)
    sleep(1)
    print('\nThe machine is thinking...\n')
    sleep(2)
    move(grid,randint(1,7),'* ')
    print('\n')
    showgrid(grid)
    while four(grid) == None:
        mover()
        if four(grid) == 'y':
            print('\nYay!! Yellow formed a line of 4 discs!')
            break
        elif four(grid) == 'r':
            print('\nYay!! Red formed a line of 4 discs!')
            break
        else:
            print('\nThe machine is thinking...\n')
            sleep(2)
            move(grid,randint(1,7),'* ')
            showgrid(grid)
        
game()  