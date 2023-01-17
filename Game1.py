
import os
import sys
import cfg
import random
import pygame


def isGameOver(board,size):
    assert isinstance(size,int)
    num_cells = size*size
    for i in range(num_cells-1):
        if board[i] != i: return False
    return True

def moveR(board, black_cell_idx, num_cols):
    if black_cell_idx%num_cols == 0: return black_cell_idx
    board[black_cell_idx-1],board[black_cell_idx] = board[black_cell_idx],board[black_cell_idx-1]
    return black_cell_idx-1

def moveL(board, black_cell_idx, num_cols):
    if (black_cell_idx+1)%num_cols == 0: return black_cell_idx
    board[black_cell_idx+1],board[black_cell_idx] = board[black_cell_idx],board[black_cell_idx+1]
    return black_cell_idx+1
    






if __name__ == '__main__':
    main()