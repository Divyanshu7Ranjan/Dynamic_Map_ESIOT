import heapq

GRID_SIZE = 10
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
grid[0][0] = 2  # Start
grid[9][9] = 3  # Destination

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])



def a_star_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            break
        
        neighbors = get_neighbors(grid, current)
        for next in neighbors:
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                heapq.heappush(open_list, (priority, next))
                came_from[next] = current

    # Reconstruct path
    current = goal
    path = []
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

def get_neighbors(grid, current):
    neighbors = []
    x, y = current
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
            if grid[new_x][new_y] != 1:  # Avoid obstacles
                neighbors.append((new_x, new_y))
    return neighbors

def check_for_obstacle():
    # Simulate obstacle detection (in real life, this would be done by ultrasonic sensors)
    # Return True if an obstacle is detected
    return True  # Simulated detection   

def reroute(start, destination):
    return a_star_search(grid, start, destination)
