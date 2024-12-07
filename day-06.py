# https://chatgpt.com/share/675399ce-4d24-8011-8650-d78367200ea5

def parse_file(filename):
    # Initialize variables
    matrix = []
    detected_char = None
    detected_coords = None
    target_chars = {"^", ">", "V", "<"}

    # Open the file and process it line by line
    with open(filename, 'r') as file:
        for y, line in enumerate(file):
            # Strip any leading/trailing whitespace from the line
            line = line.strip()
            row = []

            for x, char in enumerate(line):
                row.append(char)
                # Check if the character is one of the target ones
                if char in target_chars:
                    detected_char = char
                    detected_coords = (y, x)
            
            matrix.append(row)

    return matrix, detected_char, detected_coords

# https://chatgpt.com/share/6753a1cc-5088-8011-96db-b29941d6bbd4

def check_direction(matrix, target, coordinates):
    y, x = coordinates  # Extract y and x from the coordinates tuple

    # Check if the coordinates are out of bounds
    if y < 0 or y >= len(matrix) or x < 0 or x >= len(matrix[0]):
        return False

    if target == "^":
        # Check if the character above (y-1, x) is "#", and ensure y-1 is within bounds
        if y - 1 < 0:
            return False
        return matrix[y - 1][x] == "#"
    
    elif target == ">":
        # Check if the character to the right (y, x+1) is "#", and ensure x+1 is within bounds
        if x + 1 >= len(matrix[0]):
            return False
        return matrix[y][x + 1] == "#"
    
    elif target == "V":
        # Check if the character below (y+1, x) is "#", and ensure y+1 is within bounds
        if y + 1 >= len(matrix):
            return False
        return matrix[y + 1][x] == "#"
    
    elif target == "<":
        # Check if the character to the left (y, x-1) is "#", and ensure x-1 is within bounds
        if x - 1 < 0:
            return False
        return matrix[y][x - 1] == "#"

    return False  # Return False if the target is not one of the valid directions

# https://chatgpt.com/share/67539b73-0988-8011-9ce8-39688824eefd

def is_out_of_bounds(matrix, coordinates):
    y, x = coordinates

    # Check if the y coordinate is out of bounds
    if y < 0 or y >= len(matrix):
        return True
    
    # Check if the x coordinate is out of bounds
    if x < 0 or x >= len(matrix[0]):
        return True
    
    # If both coordinates are within bounds, return False
    return False

# https://chatgpt.com/share/67539d4e-3764-8011-bdbd-30362828b990

def update_matrix(matrix, target, coords):
    # Extract current y, x coordinates
    y, x = coords
    
    # Replace the target character with "X" at the original coordinates
    matrix[y][x] = "X"
    
    # Move the target character based on the direction
    if target == "^":
        y -= 1  # Move up
    elif target == ">":
        x += 1  # Move right
    elif target == "V":
        y += 1  # Move down
    elif target == "<":
        x -= 1  # Move left
    
    # Ensure the new coordinates are within matrix bounds (if necessary, even if invalid)
    # For the task, we do not need to check if the new position is within bounds.
    
    # Update the matrix with the new character position (even if out of bounds)
    if 0 <= y < len(matrix) and 0 <= x < len(matrix[0]):
        matrix[y][x] = target
    
    # Return the updated matrix and coordinates
    return matrix, (y, x)

# https://chatgpt.com/share/675386cd-9144-8011-bff1-372568dee216

def change_direction(matrix, target_substring, coordinates):
    # Define the cycle of direction changes
    directions = ["^", ">", "V", "<"]
    
    # Find the current direction index
    current_index = directions.index(target_substring)
    
    # Get the next direction in the cycle (circular)
    next_direction = directions[(current_index + 1) % 4]
    
    # Extract the coordinates (y, x)
    y, x = coordinates
    
    # Change the target substring in the matrix
    matrix[y][x] = next_direction
    
    # Return the updated matrix and the new character
    return matrix, next_direction

# https://chatgpt.com/share/675389a9-83d8-8011-a0e5-16defaddbcfd

def count_x(matrix):
    count = 0
    for row in matrix:
        for cell in row:
            if cell == "X":
                count += 1
    return count

# https://chatgpt.com/share/67538de1-bf7c-8011-9266-ceb0eb7e92c4

def print_matrix(matrix):
    # Get the maximum column width for each column in the matrix
    column_widths = [max(len(str(cell)) for cell in column) for column in zip(*matrix)]
    
    # Print the matrix with the appropriate formatting
    for row in matrix:
        row_str = " | ".join(f"{str(cell):<{column_widths[i]}}" for i, cell in enumerate(row))
        print(row_str)
    
    # Print the bottom border
    border = "-" * (sum(column_widths) + 3 * (len(column_widths) - 1))
    print(border)

# Because of the complexity of this task, I opted to ask chatGPT for the logic and stitch it together with a simple while loop.

matrix, guard, coords = parse_file("./day-06-input.txt")
print_matrix(matrix)

while not is_out_of_bounds(matrix, coords):
    if check_direction(matrix, guard, coords):
        matrix, guard = change_direction(matrix, guard, coords)
    matrix, coords = update_matrix(matrix, guard, coords)

# Calculate and pretty print the answer to part one
print_matrix(matrix)
distinct_position_count = count_x(matrix)
print(f'Distinct positions: {distinct_position_count}')
