import pygame
import grid

# Pygame setup and visualization
def draw_grid(screen):
    for row in range(grid.GRID_SIZE):
        for col in range(grid.GRID_SIZE):
            color = (255, 255, 255)  # Default: white
            if grid.grid[row][col] == 1:
                color = (255, 0, 0)  # Obstacle
            elif grid.grid[row][col] == 2:
                color = (0, 255, 0)  # Start
            elif grid.grid[row][col] == 3:
                color = (0, 0, 255)  # Destination

            pygame.draw.rect(screen, color, (col * 50, row * 50, 50, 50))

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('IoT Car Simulation')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((255, 255, 255))
        draw_grid(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
