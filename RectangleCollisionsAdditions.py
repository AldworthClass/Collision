import pygame
import random

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
pygame.display.set_caption("Colliding Rectangles")
pygame.mouse.set_visible(False)

#Stationary target to collide with
targets = []
target_colors = []
#Makes 10 targets in a random location within the bounds of the window
for i in range(10):
    targets.append(pygame.Rect(random.randint(0, size[0] - 50), random.randint(0, size[1] - 50), 50, 50))
    target_colors.append(RED)

#Player character that will follow the mouse
player = pygame.Rect(0, 0, 25, 25)
player_color = BLACK

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
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            player.x = mouse_pos[0]
            player.y = mouse_pos[1]

    # --- Game logic should go here
    for i in range(len(targets)):
        if targets[i].contains(player):
            target_colors[i] = GREEN
        elif targets[i].colliderect(player):
            target_colors[i] = BLUE
        else:
            target_colors[i] = RED

    # --- Screen-clearing code goes here
    #  Here, we clear the screen to white.
    screen.fill(WHITE)

    # --- Drawing code should go here

    #  Draws all targets
    for i in range(len(targets)):
        pygame.draw.rect(screen, target_colors[i], targets[i])

    pygame.draw.rect(screen, player_color, player)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
