
# import heapq

# GRID_SIZE = 10
# grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
# grid[0][0] = 2  # Start
# grid[GRID_SIZE-1][GRID_SIZE-1] = 3  # Destination

# def heuristic(a, b):
#     return abs(a[0] - b[0]) + abs(a[1] - b[1])

# def a_star_search(start, goal):
#     open_list = []
#     heapq.heappush(open_list, (0, start))
    
#     came_from = {}
#     cost_so_far = {start: 0}
#     came_from[start] = None

#     while open_list:
#         current = heapq.heappop(open_list)[1]

#         if current == goal:
#             break
        
#         for next in get_neighbors(current):
#             new_cost = cost_so_far[current] + 1
#             if next not in cost_so_far or new_cost < cost_so_far[next]:
#                 cost_so_far[next] = new_cost
#                 priority = new_cost + heuristic(goal, next)
#                 heapq.heappush(open_list, (priority, next))
#                 came_from[next] = current

#     # Reconstruct path
#     current = goal
#     path = []
#     while current is not None:
#         path.append(current)
#         current = came_from[current]
#     path.reverse()
#     return path

# def get_neighbors(current):
#     neighbors = []
#     x, y = current
#     for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#         new_x, new_y = x + dx, y + dy
#         if 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE:
#             if grid[new_x][new_y] != 1:  # Not an obstacle
#                 neighbors.append((new_x, new_y))
#     return neighbors

# def add_obstacle(x, y):
#     if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
#         grid[x][y] = 1  # Set obstacle

import heapq

GRID_SIZE = 10
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
grid[0][0] = 2  # Start
grid[GRID_SIZE-1][GRID_SIZE-1] = 3  # Destination

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    came_from = {}
    cost_so_far = {start: 0}
    came_from[start] = None

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            break
        
        for next in get_neighbors(current):
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

def get_neighbors(current):
    neighbors = []
    x, y = current
    # Add horizontal, vertical, and diagonal movements
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), 
                   (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE:
            if grid[new_x][new_y] != 1:  # Not an obstacle
                neighbors.append((new_x, new_y))
    return neighbors


def add_obstacle(x, y):
    if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
        grid[x][y] = 1  # Set obstacle
