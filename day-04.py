# https://chatgpt.com/share/67511e3c-3264-8011-976b-9dfbdff7654c

def count_word_in_wordsearch(filename, target_word):
    """
    Counts the total number of occurrences of the target_word in a word search.
    The word search supports horizontal, vertical, diagonal, and reversed directions.

    :param filename: str - The filename containing the word search grid.
    :param target_word: str - The word to search for in the word search grid.
    :return: int - Total occurrences of the target word.
    """
    def read_wordsearch(file):
        with open(file, 'r') as f:
            return [line.strip() for line in f.readlines()]

    def find_occurrences(grid, word):
        directions = [
            (0, 1),   # Right
            (0, -1),  # Left
            (1, 0),   # Down
            (-1, 0),  # Up
            (1, 1),   # Diagonal down-right
            (-1, -1), # Diagonal up-left
            (1, -1),  # Diagonal down-left
            (-1, 1)   # Diagonal up-right
        ]

        word_len = len(word)
        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    if all(
                        0 <= r + i * dr < rows and 
                        0 <= c + i * dc < cols and 
                        grid[r + i * dr][c + i * dc] == word[i]
                        for i in range(word_len)
                    ):
                        count += 1
        return count

    # Load the word search grid
    grid = read_wordsearch(filename)

    # Find occurrences of the word in the grid
    total_occurrences = find_occurrences(grid, target_word)

    return total_occurrences

# Calculate and pretty print the answer to part one

xmas_count = count_word_in_wordsearch("./day-04-input.txt", "XMAS")
print(f'XMAS occurances: {xmas_count}')

# https://chatgpt.com/share/6751219c-6978-8011-ad64-6c7bf5747471

def rotate_pattern(pattern):
    """
    Rotate the 2D pattern 90 degrees clockwise.
    """
    lines = pattern.split("\n")
    rotated = ["".join(row[i] for row in lines[::-1]) for i in range(len(lines[0]))]
    return "\n".join(rotated)


def generate_rotations(pattern):
    """
    Generate all 4 rotations of a pattern.
    """
    rotations = [pattern]
    for _ in range(3):
        pattern = rotate_pattern(pattern)
        rotations.append(pattern)
    return rotations


def match_pattern(grid, pattern, row, col):
    """
    Check if the pattern matches the grid starting from (row, col).
    Supports the '*' wildcard character.
    """
    grid_rows = len(grid)
    grid_cols = len(grid[0])
    pattern_lines = pattern.split("\n")
    pattern_rows = len(pattern_lines)
    pattern_cols = len(pattern_lines[0])

    for r in range(pattern_rows):
        for c in range(pattern_cols):
            grid_r, grid_c = row + r, col + c
            if grid_r >= grid_rows or grid_c >= grid_cols:
                return False
            if pattern_lines[r][c] != "*" and pattern_lines[r][c] != grid[grid_r][grid_c]:
                return False
    return True


def count_pattern_instances(filename, target_pattern):
    """
    Count the total instances of the target pattern in the 2D grid
    read from the given filename, considering all rotations of the pattern.
    """
    with open(filename, "r") as file:
        grid = [line.strip() for line in file.readlines()]
    
    rotations = generate_rotations(target_pattern)
    total_count = 0

    for pattern in rotations:
        pattern_lines = pattern.split("\n")
        pattern_rows = len(pattern_lines)
        pattern_cols = len(pattern_lines[0])

        for row in range(len(grid) - pattern_rows + 1):
            for col in range(len(grid[0]) - pattern_cols + 1):
                if match_pattern(grid, pattern, row, col):
                    total_count += 1

    return total_count

# Calculate and pretty print the answer to part two

x_mas_count = count_pattern_instances("./day-04-input.txt", "M*S\n*A*\nM*S")
print(f'X-mas count: {x_mas_count}')
