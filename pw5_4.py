def possiblemove(grid='list',r=int,c=int):
    '''Calculates if a move is possible within the given grid.
    : param grid: The game grid
    : type grid: list
    : param r: The row number
    : type r: int
    : param c: The column number
    : type c: int
    : return: True if a move is possible, else returns False
    : type return: bool'''
    
    if r != 0 and r != -1 and c != 0 and c != -1:
        return True if grid[r][c] == '  ' else False
    else:
        return False
