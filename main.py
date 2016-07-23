
"""
Basic implementation of Conway's Game of Life
"""

import time

import pygame

import game_of_life_funcs as gol_funcs

# Define some colours:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define width and height of each square:
WIDTH = 20
HEIGHT = 20

# Set margin between sqares:
MARGIN = 3

# Initialise pygame:
pygame.init()

# Initialise boards:
NUM_ROWS = 20
board = gol_funcs.initialiseBoard(NUM_ROWS)

# Set height and width of screen:
SIZE = [463,463]
SCREEN = pygame.display.set_mode(SIZE)

# Set title of screen:
pygame.display.set_caption("Game of Life")

# Loop until user clicks close button:
done = False

# Used to manage how fast the screen updates:
clock = pygame.time.Clock()


# Call functions here to create specific patters. Format: makeFOO(board)


while done == False:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

    SCREEN.fill(BLACK)

    # Draw grid:
    for i in range(0, NUM_ROWS):
        for j in range(0, NUM_ROWS):
            color = WHITE
            if board[i][j] == 1:
                color = RED
            pygame.draw.rect(SCREEN, color, [(MARGIN+WIDTH)*j + MARGIN, (MARGIN+HEIGHT)*i+MARGIN, WIDTH, HEIGHT])

    # Limit updates to 4 per second
    clock.tick(4)

    # Update screen:
    pygame.display.flip()

    board = gol_funcs.generate_next_board(board, NUM_ROWS)
    time.sleep(0.05)

pygame.quit()

