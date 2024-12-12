# https://chatgpt.com/share/675a6471-50a8-8011-93ab-54aa008ef0f7

def read_integers_from_file(filename):
    """
    Reads a single-line file of space-delimited integers and returns them as a list of integers.

    Args:
        filename (str): The path to the file to read.

    Returns:
        list: A list of integers.

    Raises:
        ValueError: If the file contains non-integer values.
        FileNotFoundError: If the file does not exist.
    """
    try:
        with open(filename, 'r') as file:
            # Read the single line from the file
            line = file.readline().strip()
            # Split the line into individual strings and convert to integers
            integers = [int(num) for num in line.split()]
            return integers
    except ValueError as e:
        raise ValueError(f"Error converting file contents to integers: {e}")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {e}")

# https://chatgpt.com/share/675a6493-6734-8011-a820-d6e891e294ab

def transform_stones(stones, n):
    def split_number(num):
        """Splits a number into two parts and returns them as integers."""
        num_str = str(num)
        mid = len(num_str) // 2
        return int(num_str[:mid]), int(num_str[mid:])
    
    for _ in range(n):
        print(_, end="\r")
        new_stones = []
        for stone in stones:
            if stone == 0:
                # Rule 1: Replace with a stone engraved with 1
                new_stones.append(1)
            elif len(str(abs(stone))) % 2 == 0:  # Rule 2: Check for even number of digits
                left, right = split_number(stone)
                new_stones.extend([left, right])
            else:
                # Rule 3: Replace with stone engraved with the old number * 2024
                new_stones.append(stone * 2024)
        stones = new_stones
    return stones

stones = read_integers_from_file("./day-11-input.txt")
transformed_stones = transform_stones(stones, 25)
print(len(transformed_stones))
