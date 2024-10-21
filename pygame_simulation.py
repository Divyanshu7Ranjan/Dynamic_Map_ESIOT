# # import pygame
# # import requests
# # import time
# # import grid

# # def draw_grid(screen):
# #     for row in range(grid.GRID_SIZE):
# #         for col in range(grid.GRID_SIZE):
# #             color = (255, 255, 255)  # Default: white
# #             if grid.grid[row][col] == 1:
# #                 color = (255, 0, 0)  # Obstacle
# #             elif grid.grid[row][col] == 2:
# #                 color = (0, 255, 0)  # Start
# #             elif grid.grid[row][col] == 3:
# #                 color = (0, 0, 255)  # Destination

# #             pygame.draw.rect(screen, color, (col * 50, row * 50, 50, 50))
# #             pygame.draw.rect(screen, (0, 0, 0), (col * 50, row * 50, 50, 50), 1)

# # def update_grid():
# #     response = requests.get("http://localhost:5000/grid")
# #     grid.grid = response.json()

# # def main():
# #     pygame.init()
# #     screen = pygame.display.set_mode((500, 500))
# #     pygame.display.set_caption('IoT Car Simulation')

# #     running = True
# #     while running:
# #         for event in pygame.event.get():
# #             if event.type == pygame.QUIT:
# #                 running = False
# #             if event.type == pygame.KEYDOWN:
# #                 # Simulate adding an obstacle on key press
# #                 if event.key == pygame.K_a:
# #                     # Add an obstacle at (3, 4) as an example
# #                     requests.get("http://localhost:5000/add_obstacle/3/4")
        
# #         update_grid()
# #         screen.fill((255, 255, 255))
# #         draw_grid(screen)
# #         pygame.display.flip()
# #         time.sleep(1)  # Refresh rate

# #     pygame.quit()

# # if __name__ == '__main__':
# #     main()

# import pygame
# import requests
# import time
# import grid

# def draw_grid(screen):
#     for row in range(grid.GRID_SIZE):
#         for col in range(grid.GRID_SIZE):
#             color = (255, 255, 255)  # Default: white
#             if grid.grid[row][col] == 1:
#                 color = (255, 0, 0)  # Obstacle
#             elif grid.grid[row][col] == 2:
#                 color = (0, 255, 0)  # Start
#             elif grid.grid[row][col] == 3:
#                 color = (0, 0, 255)  # Destination

#             pygame.draw.rect(screen, color, (col * 50, row * 50, 50, 50))
#             pygame.draw.rect(screen, (0, 0, 0), (col * 50, row * 50, 50, 50), 1)

# def draw_car(screen, pos):
#     """Draw the car on the grid at the given position"""
#     x, y = pos
#     pygame.draw.circle(screen, (255, 255, 0), (y * 50 + 25, x * 50 + 25), 20)

# def update_grid():
#     response = requests.get("http://localhost:5000/grid")
#     grid.grid = response.json()

# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((500, 500))
#     pygame.display.set_caption('IoT Car Simulation')

#     # Define the start and goal positions
#     start_pos = (0, 0)
#     goal_pos = (grid.GRID_SIZE-1, grid.GRID_SIZE-1)
    
#     # Get the initial path from Flask
#     path_response = requests.get(f"http://localhost:5000/reroute/{start_pos[0]}/{start_pos[1]}/{goal_pos[0]}/{goal_pos[1]}")
#     path = path_response.json()['path']
    
#     car_pos = start_pos
#     path_index = 0  # Index to track position along the path

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.KEYDOWN:
#                 # Simulate adding an obstacle on key press
#                 if event.key == pygame.K_a:
#                     requests.get("http://localhost:5000/add_obstacle/3/4")
#                     path_response = requests.get(f"http://localhost:5000/reroute_after_obstacle/{start_pos[0]}/{start_pos[1]}/{goal_pos[0]}/{goal_pos[1]}/3/4")
#                     path = path_response.json()['path']  # Update the path after adding the obstacle
#                     path_index = 0  # Reset path index

#         update_grid()
#         screen.fill((255, 255, 255))
#         draw_grid(screen)

#         if path_index < len(path):
#             car_pos = path[path_index]
#             path_index += 1

#         draw_car(screen, car_pos)
#         pygame.display.flip()
#         time.sleep(0.5)  # Refresh rate and car speed

#     pygame.quit()

# if __name__ == '__main__':
#     main()

import pygame
import requests
import time

# Pygame settings
GRID_SIZE = 10
CELL_SIZE = 50
WINDOW_SIZE = GRID_SIZE * CELL_SIZE

# Global variables for car path and position
path = []
path_index = 0
start_pos = (0, 0)
goal_pos = (GRID_SIZE - 1, GRID_SIZE - 1)

def draw_grid(screen, grid_data):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            color = (255, 255, 255)  # Default: white
            if grid_data[row][col] == 1:
                color = (255, 0, 0)  # Obstacle
            elif grid_data[row][col] == 2:
                color = (0, 255, 0)  # Start
            elif grid_data[row][col] == 3:
                color = (0, 0, 255)  # Destination

            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, (0, 0, 0), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            
def draw_path(screen, path):
    for pos in path:
        pygame.draw.rect(screen, (255, 255, 0), (pos[1] * CELL_SIZE, pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def update_grid():
    response = requests.get("http://localhost:5000/grid")
    return response.json()

def add_obstacle(x, y):
    requests.get(f"http://localhost:5000/add_obstacle/{x}/{y}")

def reroute():
    global path, path_index
    response = requests.get(f"http://localhost:5000/reroute/{start_pos[0]}/{start_pos[1]}/{goal_pos[0]}/{goal_pos[1]}")
    path = response.json()['path']
    path_index = 0  # Reset path index for car animation

def move_car():
    global path_index
    if path and path_index < len(path):
        car_pos = path[path_index]
        path_index += 1
        return car_pos
    return None

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption('IoT Car Simulation')

    grid_data = update_grid()
    car_pos = start_pos

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                grid_x = mouse_y // CELL_SIZE
                grid_y = mouse_x // CELL_SIZE
                add_obstacle(grid_x, grid_y)  # Add obstacle where user clicked
                reroute()  # Reroute after adding obstacle
        
        # Update the grid data
        grid_data = update_grid()

        # Move the car along the path
        new_car_pos = move_car()
        if new_car_pos:
            car_pos = new_car_pos

        # Clear screen
        screen.fill((255, 255, 255))

        # Draw the grid
        draw_grid(screen, grid_data)

        # Draw the car (green square)
        pygame.draw.rect(screen, (0, 255, 0), (car_pos[1] * CELL_SIZE, car_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Update the display
        pygame.display.flip()

        time.sleep(0.5)  # Adjust refresh rate for animation

    pygame.quit()

if __name__ == '__main__':
    reroute()  # Initial pathfinding
    main()
