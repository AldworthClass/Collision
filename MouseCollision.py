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
pygame.display.set_caption("Collision with the cursor")

#This is what the user will try to click
target = pygame.Rect(325, 225, 50, 50)

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

        # --- Game logic should go here
        mouse_pos = pygame.mouse.get_pos()

        #Determines the color of the target
        if target.collidepoint(mouse_pos):
                target_color = RED
        else:
                target_color = BLUE


        # --- Screen-clearing code goes here
         #  Here, we clear the screen to white. 
        screen.fill(WHITE)

        # --- Drawing code should go here

        #Draws target
        pygame.draw.rect(screen, target_color, target)
        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        # --- Limit to 60 frames per second
        clock.tick(60)
        
# Close the window and quit.
pygame.quit()
