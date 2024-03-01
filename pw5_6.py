def four(grid='list'):
    '''Checks if the player has aligned 4 disks either vertically, horizontally or diagonally.
    : param grid: the game grid that is being checked
    : type grid: list
    : return: True if the alignment has been found, else none
    : type return: str,bool'''
    
    for r in range(6, 0, -1):
        for c in range(7, 0, -1):
            if grid[r][c] == 'o ':
                if grid[r][c] == grid[r-1][c+1] == grid[r-2][c+2] == grid[r-3][c+3]:
                    return 'y'
                elif grid[r][c] == grid[r+1][c+1] == grid[r+2][c+2] == grid[r+3][c+3]:
                    return 'y'
                elif grid[r][c] == grid[r+1][c] == grid[r+2][c] == grid[r+3][c]:
                    return 'y'
                elif grid[r][c] == grid[r][c+1] == grid[r][c+2] == grid[r][c+3]:
                    return 'y'
                elif grid[r][c] == grid[r][c-1] == grid[r][c-2] == grid[r][c-3]:
                    return 'y'
                else:
                    continue
            elif grid[r][c] == '* ':
                if grid[r][c] == grid[r-1][c+1] == grid[r-2][c+2] == grid[r-3][c+3]:
                    return 'r'
                elif grid[r][c] == grid[r+1][c+1] == grid[r+2][c+2] == grid[r+3][c+3]:
                    return 'r'
                elif grid[r][c] == grid[r+1][c] == grid[r+2][c] == grid[r+3][c]:
                    return 'r'
                elif grid[r][c] == grid[r][c+1] == grid[r][c+2] == grid[r][c+3]:
                    return 'r'
                elif grid[r][c] == grid[r][c-1] == grid[r][c-2] == grid[r][c-3]:
                    return 'r'
                else:
                    continue

