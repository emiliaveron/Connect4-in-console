def showgrid(grid='list'):
    '''Displays the game grid.
    : param grid: The grid that will be shown.
    : type grid: list
    : return: None
    : type return: bool'''

    for r in range(8):
        for c in range(9):
            print(grid[r][c], end=' ')
        print()
        