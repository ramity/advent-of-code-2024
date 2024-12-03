# https://chatgpt.com/share/674e6636-c394-8011-9dfc-117b78fe9a12

def read_numbers_file(file_path):
    """
    Reads a file where each line contains space-separated numbers and 
    stores the values into a list of lists of integers.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        list of list of int: A list of lists containing the integers from the file.
    """
    try:
        with open(file_path, 'r') as file:
            # Read each line, split it into numbers, and convert them to integers
            data = [list(map(int, line.split())) for line in file]
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []
    except ValueError as e:
        print(f"Error: Non-numeric value encountered. {e}")
        return []

reports = read_numbers_file('day-02-input.txt')

# https://chatgpt.com/share/674e66f7-d9a4-8011-8f25-2713c01e8587

def is_valid_sequence(lst):
    """
    Check if a list of integers follows a strictly increasing or decreasing order
    where adjacent values differ by at least 1 and at most 3.

    Args:
        lst (list): A list of integers.

    Returns:
        bool: True if the list satisfies the conditions, False otherwise.
    """
    if len(lst) < 2:
        return True  # A single-element list or empty list is trivially valid.

    is_increasing = None  # To determine the direction of the sequence.

    for i in range(1, len(lst)):
        diff = lst[i] - lst[i - 1]
        
        # Check if adjacent values differ by at least 1 and at most 3
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        
        # Determine the direction of the sequence
        if is_increasing is None:
            is_increasing = diff > 0
        elif (is_increasing and diff < 0) or (not is_increasing and diff > 0):
            return False  # Direction changes, invalid sequence.

    return True

# Part one: Calculate and pretty print the number of safe reports

safe_reports = sum(int(is_valid_sequence(reports[z])) for z in range(len(reports)))
print(f'There are {safe_reports} safe reports.')

# There's a much more efficienct way to calculate this, but our AI friend's wasteful approach calculates the correct result
# https://chatgpt.com/share/674e6894-0bb4-8011-b1a8-aa353d4c594c - slight modification to method name

def is_loosely_valid_sequence(nums):
    def check_sequence(sequence):
        if len(sequence) < 2:
            return True
        increasing = sequence[1] > sequence[0]
        for i in range(1, len(sequence)):
            diff = abs(sequence[i] - sequence[i-1])
            if (increasing and sequence[i] <= sequence[i-1]) or \
               (not increasing and sequence[i] >= sequence[i-1]) or \
               diff < 1 or diff > 3:
                return False
        return True

    # Check if the original list passes the conditions
    if check_sequence(nums):
        return True

    # Check if removing one element allows the sequence to pass
    for i in range(len(nums)):
        if check_sequence(nums[:i] + nums[i+1:]):
            return True

    return False

# Part two: Calculate and pretty print the number of loosely safe reports

loosely_safe_reports = sum(int(is_loosely_valid_sequence(reports[z])) for z in range(len(reports)))
print(f'There are {loosely_safe_reports} loosely safe reports.')
