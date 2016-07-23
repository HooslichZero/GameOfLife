import time

import pygame

import game_of_life_funcs as gol_funcs
import game_of_life_globals as gol_globals

# Define some colours:
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
RED = ( 255, 0, 0)

# Define width and height of each square:
width = 20
height = 20

# Set margin between sqares:
margin = 3

# Initialise pygame:
pygame.init()

# Initialise boards:
NUM_ROWS = 20
board = gol_funcs.initialiseBoard(NUM_ROWS)

# Set height and width of screen:
size = [463,463]
screen = pygame.display.set_mode(size)

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

    screen.fill(BLACK)

    # Draw grid:
    for i in range(0,NUM_ROWS):
        for j in range(0,NUM_ROWS):
            color = WHITE
            if board[i][j] == 1:
                color = RED
            pygame.draw.rect(screen, color, [(margin+width)*j + margin, (margin+height)*i+margin, width, height])

    # Limit updates to 4 per second
    clock.tick(4)

    # Update screen:
    pygame.display.flip()
                                                  
    board = gol_funcs.generate_next_board(board, NUM_ROWS)
    time.sleep(0.05)

pygame.quit()
        
