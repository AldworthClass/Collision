import pygame
# Define some colors, you may want to add more
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
pygame.init()
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Collision with the Cursor Extensions")

#Lists to store the colors and locations of each Rect
targets = []
target_colors = []

#Creates a 10 x 6 grid of blue rectangles
for i in range(100, 600, 50):   #10 across, i will be x-cord
        for j in range(100, 400, 50):   #6 down, j will be y-cord
                targets.append(pygame.Rect(i, j, 25, 25))
                target_colors.append(BLUE)

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
        # --- Main event loop

        # --- All events are detected here
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                        for i in range(len(targets)):
                                mouse_pos = pygame.mouse.get_pos()
                                if targets[i].collidepoint(mouse_pos):
                                        target_colors[i] = RED
                                else:
                                        target_colors[i] = BLUE

                        
        # --- Game logic should go here


        # --- Screen-clearing code goes here
         #  Here, we clear the screen to white. 
        screen.fill(WHITE)

        # --- Drawing code should go here

        #Draws targets
        for i in range(len(targets)):
                pygame.draw.rect(screen, target_colors[i], targets[i])

        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        # --- Limit to 60 frames per second
        clock.tick(60)
        
# Close the window and quit.
pygame.quit()
