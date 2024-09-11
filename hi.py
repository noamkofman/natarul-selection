import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CUBE_SIZE = 50
CUBE_COLOR = (0, 128, 255)  # RGB color for the cube
BACKGROUND_COLOR = (0, 0, 0)  # RGB color for the background
TEXT_COLOR = (255, 255, 255)  # RGB color for the text

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pygame Cube with Name')

# Set up font for rendering text
font = pygame.font.Font(None, 36)  # Default font, size 36

class Cube:
    def __init__(self, x, y, size, color, name):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.name = name

    def draw(self, screen):
        # Draw the cube
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.size, self.size))
        
        # Render and draw the name
        text_surface = font.render(self.name, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(self.x + self.size // 2, self.y + self.size + 20))
        screen.blit(text_surface, text_rect)

# Create a cube instance
cube = Cube((SCREEN_WIDTH - CUBE_SIZE) // 2, (SCREEN_HEIGHT - CUBE_SIZE) // 2, CUBE_SIZE, CUBE_COLOR, "MyCube")

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the cube with its name
    cube.draw(screen)
    
    # Update the display
    pygame.display.flip()
