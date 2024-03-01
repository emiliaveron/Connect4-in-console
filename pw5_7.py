from pw5_4 import possiblemove
from random import randint

def recom1(grid='list'):
    '''Recommends a random column to put a disc into.
    : param grid: the game grid
    : type grid: list
    : return: None
    : type return: bool'''

    c = randint(1,7)
    smol = {1:'₁',2:'₂',3:'₃',4:'₄',5:'₅',6:'₆',7:'₇'}
    if possiblemove(grid,1,c) == True:
        print('ₚₛₛₜ... ᵧₒᵤ 𝒸ₐₙ ₘₐₖₑ ₐ ₘₒᵥₑ ₐₜ 𝒸ₒₗᵤₘₙ', smol[c])
