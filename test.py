import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Rectangle Animation')

# Set up the rectangle
rect_width = 50
rect_height = 50
rect_x = window_width // 2 - rect_width // 2
rect_y = window_height // 2 - rect_height // 2
rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
rect_color = pygame.Color('red')

# Set up the clock
clock = pygame.time.Clock()

# Set the initial velocity of the rectangle
velocity_x = 3
velocity_y = 2

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the position of the rectangle
    rect.x += velocity_x
    rect.y += velocity_y

    # Check if the rectangle hits the boundaries of the window
    if rect.right >= window_width or rect.left <= 0:
        velocity_x = -velocity_x
    if rect.bottom >= window_height or rect.top <= 0:
        velocity_y = -velocity_y

    # Clear the screen
    window.fill(pygame.Color('white'))

    # Draw the rectangle
    pygame.draw.rect(window, rect_color, rect)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)
