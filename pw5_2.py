def cleargrid(grid='list'):
    '''Cleans the game grid for the next game.
    : param grid: The game grid to be cleaned
    : type grid: list
    : return: None
    : type return: bool'''
    
    for r in range(1,7):
        for c in range(1,8):
            grid[r][c] = '  '