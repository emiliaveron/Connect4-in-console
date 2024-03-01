from pw5_4 import possiblemove

def recom2(grid='list'):
    '''Recommends a beneficial for the player column to play in.
    : param grid: the game grid
    : type grid: list
    : return: None
    : type return: bool'''
    
    smol = {1:'₁',2:'₂',3:'₃',4:'₄',5:'₅',6:'₆',7:'₇'}
    for c in range(1,8):
        for r in range(6,0,-1):
            if grid[r][c-1] == grid[r][c+1] != '  ' or grid[r-1][c-1] == grid[r+1][c+1] != '  ' or grid[r+1][c-1] == grid[r-1][c+1] != '  ':
                if possiblemove(grid,r,c) == True:
                    print('ₚₛₛₜ... ᵧₒᵤ 𝒸ₐₙ ₘₐₖₑ ₐ ₘₒᵥₑ ₐₜ 𝒸ₒₗᵤₘₙ',smol[c])
                    break
                else:
                    continue
            else:
                continue