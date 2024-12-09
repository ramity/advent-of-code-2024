# https://chatgpt.com/share/67560548-7900-8011-ad46-e26fcf6da80b

def process_map(filename):
    def parse_map(file):
        """Reads the file into a 2D matrix and returns it."""
        with open(file, 'r') as f:
            return [list(line.strip()) for line in f]

    def is_within_bounds(x, y, rows, cols):
        """Checks if a point is within the map boundaries."""
        return 0 <= x < rows and 0 <= y < cols

    def generate_points(p1, p2):
        """Generates points immediately before and after two points sharing the same slope."""
        x1, y1 = p1
        x2, y2 = p2
        dx, dy = x2 - x1, y2 - y1

        # Generate points
        before = (x1 - dx, y1 - dy)
        after = (x2 + dx, y2 + dy)
        return before, after

    # Read the map
    matrix = parse_map(filename)
    rows, cols = len(matrix), len(matrix[0])
    character_positions = {}

    # Collect positions of each alphanumeric character
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c].isalnum():
                char = matrix[r][c]
                if char not in character_positions:
                    character_positions[char] = []
                character_positions[char].append((r, c))

    count = 0  # Counter for generated points
    
    # Iterate over characters and pairs of points
    for char, positions in character_positions.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                p1, p2 = positions[i], positions[j]
                before, after = generate_points(p1, p2)

                for x, y in [before, after]:
                    if is_within_bounds(x, y, rows, cols):
                        if matrix[x][y] == '.':
                            matrix[x][y] = '#'
                            count += 1
                        elif not matrix[x][y].isalnum():
                            count += 1  # Increment even if it doesn't replace

    return count

print(process_map("./day-08-input.txt"))

def read_file_to_map(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]

def in_bounds(x, y, map_width, map_height):
    return 0 <= x < map_width and 0 <= y < map_height

def generate_line_points(x1, y1, x2, y2, map_width, map_height):
    points = []
    dx = x2 - x1
    dy = y2 - y1

    # Special case: vertical line
    if dx == 0:
        step = 1 if y2 > y1 else -1
        # Extrapolate in both directions along y (before x1 and after x2)
        for y in range(y1 - step, -1, -step):  # Extrapolate before x1
            if in_bounds(x1, y, map_width, map_height):
                points.append((x1, y))
        for y in range(y2 + step, map_height, step):  # Extrapolate after x2
            if in_bounds(x1, y, map_width, map_height):
                points.append((x1, y))
        return points

    # Special case: horizontal line
    if dy == 0:
        step = 1 if x2 > x1 else -1
        # Extrapolate in both directions along x (before x1 and after x2)
        for x in range(x1 - step, -1, -step):  # Extrapolate before x1
            if in_bounds(x, y1, map_width, map_height):
                points.append((x, y1))
        for x in range(x2 + step, map_width, step):  # Extrapolate after x2
            if in_bounds(x, y2, map_width, map_height):
                points.append((x, y2))
        return points

    # Calculate slope for non-vertical, non-horizontal lines
    slope = dy / dx
    intercept = y1 - slope * x1

    # Extrapolate before the first point (moving backwards)
    x = x1
    while x >= 0:
        y = round(slope * x + intercept)
        if in_bounds(x, y, map_width, map_height):
            points.append((x, y))
        # Move to previous x in the line
        x -= 1

    # Extrapolate after the second point (moving forward)
    x = x2
    while x < map_width:
        y = round(slope * x + intercept)
        if in_bounds(x, y, map_width, map_height):
            points.append((x, y))
        # Move to next x in the line
        x += 1

    return points

def process_map(filename):
    map_data = read_file_to_map(filename)
    map_height = len(map_data)
    map_width = len(map_data[0])
    alphanumeric_points = {}

    # Step 1: Gather all alphanumeric character points
    for y in range(map_height):
        for x in range(map_width):
            char = map_data[y][x]
            if char.isalnum():
                if char not in alphanumeric_points:
                    alphanumeric_points[char] = []
                alphanumeric_points[char].append((x, y))

    # Step 2: Iterate over each character group and generate points
    total_hash_count = 0
    for points in alphanumeric_points.values():
        # For each pair of points (p1, p2) where both are the same character
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                # Generate line points and add `#` within bounds
                line_points = generate_line_points(x1, y1, x2, y2, map_width, map_height)
                for (x, y) in line_points:
                    if in_bounds(x, y, map_width, map_height) and map_data[y][x] == '.':
                        map_data[y][x] = '#'
                        total_hash_count += 1

    for line in map_data: print(line)

    return total_hash_count

print(process_map("./day-08-input.txt"))