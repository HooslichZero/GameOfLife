import time
from functions import *
import pygame


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
board = initialiseBoard()

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
    for i in range(0,n):
        for j in range(0,n):
            color = WHITE
            if board[i][j] == 1:
                color = RED
            pygame.draw.rect(screen, color, [(margin+width)*j + margin, (margin+height)*i+margin, width, height])

    # Limit to 20 FPS:
    clock.tick(20)

    # Update screen:
    pygame.display.flip()
                                                  
    updatePos(board)
    time.sleep(0.05)

pygame.quit()
        
