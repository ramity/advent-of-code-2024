# https://chatgpt.com/share/675bce37-3b7c-8011-8119-bd8ea99d3afc

def read_and_cluster(filename):
    # Read the file and convert to 2D array of letters
    with open(filename, 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    
    # Initialize visited matrix to track which cells have been visited
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    def get_neighbors(x, y):
        # Return the coordinates of cardinal neighbors (up, down, left, right)
        neighbors = []
        if x > 0:
            neighbors.append((x-1, y))
        if x < len(grid) - 1:
            neighbors.append((x+1, y))
        if y > 0:
            neighbors.append((x, y-1))
        if y < len(grid[0]) - 1:
            neighbors.append((x, y+1))
        return neighbors

    def dfs(x, y, char):
        # Perform Depth First Search to find a cluster
        stack = [(x, y)]
        cluster = []
        while stack:
            cx, cy = stack.pop()
            if visited[cx][cy]:
                continue
            visited[cx][cy] = True
            cluster.append((cx, cy))
            for nx, ny in get_neighbors(cx, cy):
                if not visited[nx][ny] and grid[nx][ny] == char:
                    stack.append((nx, ny))
        return cluster

    # Perform clustering by visiting each cell
    clusters = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j]:
                cluster = dfs(i, j, grid[i][j])
                if cluster:
                    clusters.append(cluster)

    return clusters

def compute_perimeter(cluster):
    perimeter = 0
    for x, y in cluster:
        # Check each of the four cardinal directions
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for nx, ny in neighbors:
            if (nx, ny) not in cluster:
                perimeter += 1
    return perimeter

def compute_area(cluster):
    return len(cluster)

def compute_area_perimeter_product(area, perimeter):
    return area * perimeter

# Assuming you have a file 'input.txt' with a grid of letters
filename = './day-12-input.txt'

# Step 1: Read file and perform clustering
clusters = read_and_cluster(filename)
sum = 0

# Step 2: Compute area and perimeter for each cluster
for cluster in clusters:
    area = compute_area(cluster)
    perimeter = compute_perimeter(cluster)
    
    # Step 3: Compute the product of area and perimeter
    area_perimeter_product = compute_area_perimeter_product(area, perimeter)
    sum += area_perimeter_product
    print(f"Area: {area}, Perimeter: {perimeter}, Product: {area_perimeter_product}")

print(sum)

# !!!

def read_and_cluster(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    clusters = []
    
    # Directions for cardinal neighbors: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def dfs(x, y, char, cluster):
        stack = [(x, y)]
        visited[x][y] = True
        cluster.append((x, y))
        
        while stack:
            cx, cy = stack.pop()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if in_bounds(nx, ny) and not visited[nx][ny] and grid[nx][ny] == char:
                    visited[nx][ny] = True
                    cluster.append((nx, ny))
                    stack.append((nx, ny))
    
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                cluster = []
                dfs(i, j, grid[i][j], cluster)
                clusters.append(cluster)
    
    return clusters

def calculate_vertices(cluster):
    # Create a set of unique boundary points
    boundary = set()
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for x, y in cluster:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in cluster:
                boundary.add((x, y))
                break
    
    return len(boundary)

def calculate_area(cluster):
    return len(cluster)

def calculate_sum_of_clusters(clusters):
    total_sum = 0
    for cluster in clusters:
        vertices = calculate_vertices(cluster)
        area = calculate_area(cluster)
        total_sum += vertices * area
        print(vertices, area)
    return total_sum

filename = './day-12-input.txt'
clusters = read_and_cluster(filename)
result = calculate_sum_of_clusters(clusters)
print(result)
