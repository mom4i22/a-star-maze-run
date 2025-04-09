import heapq

maze = [
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 5)
rows, cols = len(maze), len(maze[0])
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def valid(pos):
    r, c = pos
    in_bounds = 0 <= r < rows and 0 <= c < cols
    is_open = maze[r][c] == 0 if in_bounds else False
    return in_bounds and is_open

def a_star(start, goal):
    open_set = []

    manhattan_distance = heuristic(start, goal)
    print("Result from Manhattan distance heuristic:", manhattan_distance)

    heapq.heappush(open_set, (0 + manhattan_distance, 0, start, [start]))
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current == goal:
            return path

        if current in visited:
            continue
        visited.add(current)

        for move in moves:
            neighbor = (current[0] + move[0], current[1] + move[1])
            if valid(neighbor) and neighbor not in visited:
                heapq.heappush(open_set, (g + 1 + heuristic(neighbor, goal), g + 1, neighbor, path + [neighbor]))

    return None

path = a_star(start, goal)
print("Path found:", path)
