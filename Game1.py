
import os
import sys
import cfg
import random
import pygame


def isGameOver(board, size):
    assert isinstance(size, int)
    num_cells = size*size
    for i in range(num_cells-1):
        if board[i] != i:
            return False
    return True


def moveR(board, blank_cell_idx, num_cols):
    if blank_cell_idx % num_cols == 0:
        return blank_cell_idx
    board[blank_cell_idx -
          1], board[blank_cell_idx] = board[black_cell_idx], board[black_cell_idx-1]
    return blank_cell_idx-1


def moveL(board, blank_cell_idx, num_cols):
    if (blank_cell_idx+1) % num_cols == 0:
        return blank_cell_idx
    board[blank_cell_idx +
          1], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx+1]
    return blank_cell_idx+1


def moveD(board, blank_cell_idx, num_cols):
    if blank_cell_idx < num_cols:
        return blank_cell_idx
    board[blank_cell_idx-num_cols], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx-num_cols]
    return blank_cell_idx-num_cols


def moveU(board, blank_cell_idx, num_rows, num_cols):
    if blank_cell_idx >= (num_rows-1)*num_cols:
        return blank_cell_idx
    board[blank_cell_idx+num_cols], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx+num_cols]
    return blank_cell_idx+num_cols


def CreateBoard(num_rows, num_cols, num_cells):
    board = []
    for i in range(num_cells):
        board.append(i)

    blank_cell_idx = num_cells-1
    board[blank_cell_idx] = -1

    for i in range(cfg.RANDNUM):
        direction = random.randint(0, 3)

        if direction == 0:
            blank_cell_idx = moveL(board, blank_cell_idx, num_cols)
        elif direction == 1:
            blank_cell_idx = moveR(board, blank_cell_idx, num_cols)
        elif direction == 2:
            blank_cell_idx = moveU(board, blank_cell_idx, num_rows, num_cols)
        elif direction == 3:
            blank_cell_idx = moveD(board, blank_cell_idx, num_cols)
    return board, blank_cell_idx


def GeImagePaths(rootdir):
    imagenames = os.listdir(rootdir)
    assert len(imagenames) > 0
    return os.path.join(rootdir, random.choice(imagenames))


def ShowEndInterface(screen, width, height):
    screen.fill(cfg.BACKGROUNDCOLOR)
    font = pygame.font.Font(cfg.FONTPATH, width/15)
    title = font.render('Good Job! You Won!', True, (233, 150, 122))
    rect = title.get_rect()
    rect.midtop = (width/2, height/2.5)
    screen.blit(title, rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
        pygame.display.update()


def ShowStartInterface(screen, width, height):
    screen.fill(cfg.BACKGROUNDCOLOR)
    tfont = pygame.font.Font(cfg.FONTPATH, width//4)
    cfont = pygame.font.Font(cfg.FONTPATH, width//20)
    title = tfont.render('Puzzle', True, cfg.RED)
    content1 = cfont.render('Press H,M or L to choose your puzzle', True, cfg.BLUE)
    content2 = cfont.render('H- 5x5, M- 4x4, L- 3x3', True, cfg.BLUE)
    trect = title.get_rect()
    trect.midtop = (width/2,height/10)
    crect1 = content1.get_rect()
    crect1.midtop = (width/2, height/2.2)
    crect2 = content2.get_rect()
    crect2.midtop = (width/2, height/1.8)
    screen.blit(title, trect)
    screen.blit(content1, crect1)
    screen.blit(content2, crect2)
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key ==ord('l'): return 3
                if event.key ==ord('m'): return 4
                if event.key ==ord('h'): return 5
        pygame.display.update()
        
if __name__ == '__main__':
    main()
