from pw5_4 import possiblemove

def move(grid='list', c=int, sign=str):
    '''Creates a character on the game grid to signify a move.
    : param grid: the game grid
    : type grid: list
    : param c: the column where the move is made
    : type c: int
    : param sign: the sign that will be put onto the grid
    : type sign: str'''
    
    for r in range(6,0,-1):
        if possiblemove(grid,r,c) == True:
            grid[r][c] = sign
            break
        else:
            continue
    else:
        print('No available space!')
