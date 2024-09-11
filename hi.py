from distutils.util import change_root
from turtle import speed
import pygame
import sys
import random 
import time
# Initialize Pygame
pygame.init()
hi = ['1', "2", "3", "4",]
# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
IMAGE_PATH = 'natarul selection\\1000_F_506725496_kvJPVTdPAdmjHO6b9TOkHzm3Zqn5cILX-removebg-preview.png'  # Replace with your image file path
IMAGE_SIZE = (50, 50)  # Desired size for the image

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Display Image Example')

# Load and scale the image
cube = pygame.image.load(IMAGE_PATH)
cube1 = pygame.image.load(IMAGE_PATH)
cube2 = pygame.image.load(IMAGE_PATH)
cube3 = pygame.image.load(IMAGE_PATH)

scaled_cube = pygame.transform.scale(cube, IMAGE_SIZE)
scaled1_cube = pygame.transform.scale(cube, IMAGE_SIZE)
scaled2_cube = pygame.transform.scale(cube, IMAGE_SIZE)
scaled3_cube = pygame.transform.scale(cube, IMAGE_SIZE)


# List to hold cloned images
cloned_images = []
SPEED = 50

# Initial image position
positions = [
    [50, 50],
    [700, 45],
    [50, 550],
    [700, 550]
]
velocities = [
    [random.uniform(-SPEED, SPEED), random.uniform(-SPEED, SPEED)],
    [random.uniform(-SPEED, SPEED), random.uniform(-SPEED, SPEED)],
    [random.uniform(-SPEED, SPEED), random.uniform(-SPEED, SPEED)],
    [random.uniform(-SPEED, SPEED), random.uniform(-SPEED, SPEED)]
]
clock = pygame.time.Clock()
feed = False
# Flag to track if key has been pressed
key_pressed = False
action_start_time = None
action_duration = 4  # Duration in seconds
action_active = False
FPS = 60
# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if not action_active:
            action_start_time = time.time()
            action_active = True
            feed = True    # Check if the left arrow key is pressed
    if keys[pygame.K_LEFT]:
        if not key_pressed:  # Clone the image only if the key was not pressed before
            # Clone the image and add it to the list with a new position
            cloned_image = scaled_cube.copy()
            cloned_images.append((cloned_image, (50, 100 + len(cloned_images) * 60)))
            key_pressed = True  # Set flag to indicate the key is pressed
    else:
        key_pressed = False  # Reset the flag when the key is not pressed

    # Clear the screen
    screen.fill((0, 0, 0))  # Black background


    # Draw the original image
    screen.blit(scaled_cube, (positions[0]))
    screen.blit(scaled1_cube, (positions[1]))
    screen.blit(scaled2_cube, (positions[2]))
    screen.blit(scaled3_cube, (positions[3]))
    # below we use a 2d array to optimize the speed 
    # we decide if feed is true if it is then...
    if feed == True:
        # we define i as an object of the length of positions 
        for i in range(len(positions)):
            # when we use [i][0] we first use i which tells that we are applying this to every value in length of position
            # and [0] tells us if we are applying it to the first row (x) or second row (y)
            positions[i][0] += velocities[i][0]
            positions[i][1] += velocities[i][1]
            if positions[i][0] < 0:
                positions[i][0] = 0
                velocities[i][0] = abs(velocities[i][0])  # Reverse direction
            elif positions[i][0] > SCREEN_WIDTH - IMAGE_SIZE[0]:
                positions[i][0] = SCREEN_WIDTH - IMAGE_SIZE[0]
                velocities[i][0] = -abs(velocities[i][0])  # Reverse direction

            if positions[i][1] < 0:
                positions[i][1] = 0
                velocities[i][1] = abs(velocities[i][1])  # Reverse direction
            elif positions[i][1] > SCREEN_HEIGHT - IMAGE_SIZE[1]:
                positions[i][1] = SCREEN_HEIGHT - IMAGE_SIZE[1]
                velocities[i][1] = -abs(velocities[i][1])  # Reverse direction
                

        # cube_x += random.uniform(-speed, speed)
        # cube_y += random.uniform(-speed, speed)
        # cube_x1 += random.uniform(-speed, speed)
        # cube_y1 += random.uniform(-50, 50)
        # cube_x2 += random.uniform(-50, 50)
        # cube_y2 += random.uniform(-50, 50)
        # cube_x3+= random.uniform(-50, 50)
        # cube_y3 += random.uniform(-50, 50)
    # screen boudnaries 
    # cube_x = max(0, min(cube_x, SCREEN_WIDTH - IMAGE_SIZE[0]))
    # cube_y = max(0, min(cube_y, SCREEN_HEIGHT - IMAGE_SIZE[1]))
    # cube_x1 = max(0, min(cube_x1, SCREEN_WIDTH - IMAGE_SIZE[0]))
    # cube_y1 = max(0, min(cube_y1, SCREEN_HEIGHT - IMAGE_SIZE[1]))
    # cube_x2 = max(0, min(cube_x2, SCREEN_WIDTH - IMAGE_SIZE[0]))
    # cube_y2 = max(0, min(cube_y2, SCREEN_HEIGHT - IMAGE_SIZE[1]))
    # cube_x3 = max(0, min(cube_x3, SCREEN_WIDTH - IMAGE_SIZE[0]))
    # cube_y3 = max(0, min(cube_y3, SCREEN_HEIGHT - IMAGE_SIZE[1]))
    if action_active:   
        current_time = time.time()
        elapsed_time = current_time - action_start_time
        print(elapsed_time)
        
        if elapsed_time > action_duration:
            action_active = False
            feed = False
            
            # Stop the action after 10 seconds
    # Draw all cloned images
    for image, position in cloned_images:
        screen.blit(image, position)
    clock.tick(FPS)
    # Update the display
    pygame.display.flip()