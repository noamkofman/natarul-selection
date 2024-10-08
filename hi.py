import pygame
import sys
import random
import time
import math
import atexit 
import matplotlib.pyplot as plt
import numpy as np






# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
IMAGE_PATH = 'png-transparent-binary-large-object-blob-s-leaf-grass-cartoon-thumbnail-removebg-preview.png'
food_path = 'large_Poly_Orange_7579up_1471502253-removebg-preview.png'
IMAGE_SIZE = (55, 73)
food_size = (20, 20)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Display Image Example')
font = pygame.font.Font('freesansbold.ttf', 32)


# Load and scale the image
cube = pygame.image.load(IMAGE_PATH)
scaled_cube = pygame.transform.scale(cube, IMAGE_SIZE)
scaled1_cube = pygame.transform.scale(cube, IMAGE_SIZE)
scaled2_cube = pygame.transform.scale(cube, IMAGE_SIZE)
scaled3_cube = pygame.transform.scale(cube, IMAGE_SIZE)
food = pygame.image.load(food_path)
scaled_food = pygame.transform.scale(food, food_size)

# Initialize lists
cloned_images = []
cloned_food = []
SPEED = 5


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
key_pressed = False
action_start_time = None
action_duration = 2
action_active = False
FPS = 60
MAX_FOOD_ITEMS =  5
ate = 0
generation_duration = 5
current_generation = 1
penis = 0
 # Create a figure and axis for the plot
def plot_food():
    
    generations = list(range(1, len(generation_food_data) + 1))
    food_counts = generation_food_data
    total_cubes = total_cube_data
    total_speed = total_speed_data
    plt.xlabel("Generations")
    plt.ylabel("Total Food Eaten")
    plt.plot(generations, food_counts, marker='o', linestyle='-', color='b', label='Total Food Eaten')
    plt.plot(generations, total_cubes, marker='o', linestyle='-', color='r', label='Total Cubes')
    plt.plot(generations, total_speed, marker='o', linestyle='-', color='g', label='Total Speed Mutation')
    plt.plot(generations, total_non_mutants, marker='o', linestyle='-', color='m', label='Total Non-Mutants')


    plt.figtext(0.15, 0.83, "food eaten in blue, total cubes in red")


    plt.show()

# set the center of the rectangular object.
food_counts = [0] * len(positions)

def add_food():
    if len(cloned_food) < MAX_FOOD_ITEMS:
        new_food_position = [random.randint(0, SCREEN_WIDTH - food_size[0]), random.randint(0, SCREEN_HEIGHT - food_size[1])]
        cloned_food.append((scaled_food.copy(), new_food_position))
        
def speed_mutation(velocity):
    speed_increase = 10
    velocity[0] *= speed_increase
    velocity[1] *= speed_increase
generation_food_data = []
total_cube_data = []
total_speed_data = []
total_non_mutants = []
non_mutants = 0

mutations = [0] * len(positions) 
initial_mutation_chance = 1/5
offspring_muation_chance = 1/2
mutation_chance = initial_mutation_chance

# Main loop
while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
                atexit.register(print_results)
                print("generation_food_data:", generation_food_data)
                print("total_cube_data:", total_cube_data)
                print("total_speed_data:", total_speed_data)
                print("total_non_mutants:", total_non_mutants)

                plot_food()
                s = False
                
        
                pygame.quit()
                sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if not action_active:
            action_start_time = time.time()
            action_active = True
            feed = True

    if keys[pygame.K_LEFT]:
        if not key_pressed:
            cloned_image = scaled_cube.copy()
            cloned_images.append((cloned_image, (50, 100 + len(cloned_images) * 60)))
            key_pressed = True
            add_food()
    elif keys[pygame.K_RIGHT]:
        if not key_pressed:
            
            key_pressed = True
    else:
        key_pressed = False

    screen.fill((0, 0, 0))

    # Draw the original images
    for i in range(len(positions)):
        screen.blit(scaled_cube, positions[i])
    
    def print_results():
            for i, count in enumerate(food_counts.copy()):
                #print(f"Cube {i} ate {count} food items.")
                total_cubes = i

    if feed:
        add_food()
        
        # Function to print the results
        
        # Draw all cloned food items
        for food_image, food_pos in cloned_food:
            screen.blit(food_image, food_pos)
        # below w do the calculations for eating food and adding the foodcount 
        for i in range(len(positions)):
            cube_x, cube_y = positions[i][0], positions[i][1]
            for food_image, food_pos in cloned_food:
                food_x, food_y = food_pos[0], food_pos[1]
                distance = math.sqrt((cube_x - food_x) ** 2 + (cube_y - food_y) ** 2)
                threshold = 20
                # below find if a cube has eaten
                if distance < threshold:
                    #print("Food eaten at", food_pos)
                    cloned_food.remove((food_image, food_pos))
                    #print(f"Cube {i} ate food at", food_counts)
                    food_counts[i] += 1
                    
                    add_food() # Optionally add more food
                    break

            # Update positions and handle boundary collisions
            positions[i][0] += velocities[i][0]
            positions[i][1] += velocities[i][1]
            if positions[i][0] < 0:
                positions[i][0] = 0
                velocities[i][0] = abs(velocities[i][0])
            elif positions[i][0] > SCREEN_WIDTH - IMAGE_SIZE[0]:
                positions[i][0] = SCREEN_WIDTH - IMAGE_SIZE[0]
                velocities[i][0] = -abs(velocities[i][0])

            if positions[i][1] < 0:
                positions[i][1] = 0
                velocities[i][1] = abs(velocities[i][1])
            elif positions[i][1] > SCREEN_HEIGHT - IMAGE_SIZE[1]:
                positions[i][1] = SCREEN_HEIGHT - IMAGE_SIZE[1]
                velocities[i][1] = -abs(velocities[i][1])
    if action_active:
        # Time tracking for generations
        current_time = time.time()
        elapsed_time = current_time - action_start_time
    
        s = str(elapsed_time)
        text = font.render("Generations: "+str(current_generation), True, green, blue)
        textRect = text.get_rect()

        textRect.center = (200, 50)
        screen.blit(text, textRect)

        #print(elapsed_time)
        # below we do all the stuff for the next generations
        if elapsed_time > action_duration:
            # After each generation update (where new cubes are created and old cubes die)
            non_mutants = sum(1 for mutation in mutations if mutation == 0)  # Correctly count non-mutants
            mutants = sum(1 for mutation in mutations if mutation == 1)  # Correctly count mutants (speed mutations)

            # Append the count to the appropriate lists
            total_non_mutants.append(non_mutants)
            total_speed_data.append(mutants)  # Track only the number of mutant cubes
            total_cube_data.append(len(positions))  # This remains the same (total number of cubes)
            generation_food_data.append(sum(food_counts))



            #action_active = False

            current_generation += 1
            print(f"Total cubes: {len(positions)}, Mutants: {mutants}, Non-mutants: {non_mutants}")


            dead_indices = []   
            living_indices = []
            for i, count in enumerate(food_counts):
                if food_counts[i] < 1:
                    #print(f"Cube {i} has died")
                    dead_indices.append(i)
                else:
                    #print(i, "lives on")
                    living_indices.append(positions[i])
                    
            for index in sorted(dead_indices, reverse=True):  # Remove in reverse order to avoid index shifting
                del positions[index]
                del velocities[index]
                del food_counts[index]
                del mutations[index]
            food_counts = [0] * len(positions)
            for parent_index, parent_position in enumerate(living_indices):
                for _ in range(2):  # Two offspring per surviving parent
                    # Slightly randomize the position of the offspring
                    offspring_position = [
                        parent_position[0] + random.randint(-50, 50),
                        parent_position[1] + random.randint(-50, 50)
                    ]
                    new_velocity = ([random.uniform(-SPEED, SPEED), random.uniform(-SPEED, SPEED)])
                    m = 0
                    #mutation_chnace = 0.1
                    if mutations[parent_index] == 1:
                        mutation_chance = offspring_muation_chance
                    if random.random() < mutation_chance:
                        mutations.append(1)
                        speed_mutation(new_velocity)
                        #print("speed gained")
                    else:
                        mutations.append(0)
                        #print("none")
                   #print(len(mutations))
                        
                    positions.append(offspring_position)
                    velocities.append(new_velocity)
                    food_counts.append(0)  # Initialize food count for the new offspring
            
            action_start_time = current_time
            
    for image, position in cloned_images:
        screen.blit(image, position)
        #print(food_counts[i])
       
   

    #print(penis)
       
    clock.tick(FPS)
    
    pygame.display.flip()