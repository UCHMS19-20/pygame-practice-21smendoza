import sys
import pygame

purple = (180, 0, 200)
yellow = (180, 200, 0)
# Initialize pygame so it runs in the background and manages things
pygame.init()

font = pygame.font.SysFont("Garamond", 100)

text = font.render("Sam", True, yellow) 

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (400, 300) )

# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        print(event)
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
    screen.fill(purple)

    screen.blit(text, pygame.mouse.get_pos() )
    

    pygame.display.flip()
