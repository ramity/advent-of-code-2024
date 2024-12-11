# https://chatgpt.com/share/67591283-597c-8011-8ee8-41d364fd734b

from collections import deque

def find_paths(filename):
    # Read the file into a 2D array (map)
    with open(filename, 'r') as file:
        map = [list(line.strip()) for line in file.readlines()]
    
    # Get the dimensions of the map
    rows = len(map)
    cols = len(map[0])
    
    # Directions for cardinal moves: (down, up, right, left)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Function to check if a position is valid and traversable
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols and map[r][c] != '.'

    # Function to perform a BFS search from a given start
    def bfs(start_r, start_c):
        # Initialize a queue for BFS with starting position
        queue = deque([(start_r, start_c, [start_r, start_c])])  # (row, col, path)
        visited = set()  # to track visited nodes
        visited.add((start_r, start_c))
        paths = []
        
        while queue:
            r, c, path = queue.popleft()
            
            # If we reach '9', add the path to result
            if map[r][c] == '9':
                paths.append(path)
                continue
            
            # Explore cardinal directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if is_valid(nr, nc) and (nr, nc) not in visited and ord(map[nr][nc]) == ord(map[r][c]) + 1:
                    visited.add((nr, nc))
                    queue.append((nr, nc, path + [nr, nc]))
        
        return paths

    # Find all paths starting from '0'
    paths_from_zero = []
    for r in range(rows):
        for c in range(cols):
            if map[r][c] == '0':
                paths_from_zero.extend(bfs(r, c))
    
    return paths_from_zero

paths = find_paths("day-10-input.txt")
print(len(paths))

def find_paths(filename):
    # Read the file and create the 2D map
    with open(filename, 'r') as file:
        map = [list(line.strip()) for line in file]

    rows = len(map)
    cols = len(map[0])
    counter = 0

    # Direction vectors for cardinal neighbors (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Helper function to check if a position is within bounds
    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    # Helper function to perform a depth-first search from a starting position
    def dfs(x, y, current_value):
        nonlocal counter
        # If we've reached the value '9', increment the counter
        if current_value == 9:
            counter += 1
            return

        # Check all cardinal neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and map[nx][ny] != ".":
                # Convert the character to an integer
                neighbor_value = int(map[nx][ny])
                if neighbor_value == current_value + 1:
                    map[nx][ny] = "."  # Mark as visited by replacing it with "."
                    dfs(nx, ny, neighbor_value)
                    map[nx][ny] = str(neighbor_value)  # Unmark after dfs

    # Start DFS from every '0' in the map
    for i in range(rows):
        for j in range(cols):
            if map[i][j] == '0':  # Start a DFS if the current element is '0'
                dfs(i, j, 0)

    return counter

print(find_paths("./day-10-input.txt"))
