# https://chatgpt.com/share/67524007-34f0-8011-a793-0d7d702ac865

def process_file(filename):
    """
    Processes a file with the specified format:
    - Lines in the format "X|Y" are saved until a blank line is encountered.
    - Subsequent lines are treated as comma-delimited numbers and saved.

    Args:
        filename (str): The name of the file to process.

    Returns:
        tuple: A tuple containing two arrays:
            - The first array contains "X|Y" formatted strings.
            - The second array contains comma-delimited strings.
    """
    xy_array = []
    comma_array = []
    blank_line_encountered = False

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()  # Remove leading and trailing whitespace
                
                if not line:  # Check for a blank line
                    blank_line_encountered = True
                    continue

                if not blank_line_encountered:
                    if '|' in line:  # Check for X|Y format
                        xy_array.append(line)
                else:
                    if ',' in line:  # Check for comma-delimited numbers
                        comma_array.append(line)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return xy_array, comma_array

# https://chatgpt.com/share/6752402c-ab38-8011-94f3-f7d688deb32d

def validate_order(numbers: str, rules: list) -> bool:
    """
    Validates if a comma-delimited list of numbers follows a set of ordering rules.

    :param numbers: A comma-delimited string of numbers.
    :param rules: A list of "X|Y" strings representing ordering rules (X must occur before Y).
    :return: True if the numbers follow the rules, False otherwise.
    """
    # Convert the comma-delimited string into a list of numbers
    number_list = numbers.split(",")
    
    # Check each rule
    for rule in rules:
        # Parse the X|Y rule
        try:
            x, y = rule.split("|")
        except ValueError:
            raise ValueError(f"Invalid rule format: {rule}. Expected 'X|Y'.")
        
        # Ensure X occurs before Y in the number list
        x_indices = [i for i, num in enumerate(number_list) if num == x]
        y_indices = [i for i, num in enumerate(number_list) if num == y]
        
        # If Y appears before X, the rule is violated
        if x_indices and y_indices and min(y_indices) < max(x_indices):
            return False

    # If all rules pass, return True
    return True

# https://chatgpt.com/share/675240fb-dcc4-8011-9843-8c2a4d5c4e58

def middle_number(numbers_str):
    # Split the input string into a list of strings
    numbers_list = numbers_str.split(',')
    
    # Convert the list of strings to a list of integers
    numbers = [int(num) for num in numbers_list]
    
    # Find the middle index
    middle_index = len(numbers) // 2
    
    # Return the number at the middle index
    return numbers[middle_index]

# Calculate and pretty print the answer to part one

xy_rules, orderings = process_file("./day-05-input.txt")
middle_sum = sum(middle_number(ordering) if validate_order(ordering, xy_rules) else 0 for ordering in orderings)
print(f'Sum of valid middle pages: {middle_sum}')

# https://chatgpt.com/share/67529f4f-5900-8011-878e-6d4099efc9eb

def reorder_numbers(number_list, ordering_rules):
    # Split the input string into a list of integers
    numbers = list(map(int, number_list.split(',')))

    # Create a graph to represent dependencies and track in-degrees
    adjacency_list = {num: [] for num in numbers}
    in_degree = {num: 0 for num in numbers}

    # Parse ordering rules to populate the graph
    for rule in ordering_rules:
        x, y = map(int, rule.split('|'))
        if x not in adjacency_list: continue
        if y not in in_degree: continue
        if y not in adjacency_list[x]:  # Avoid duplicate edges
            adjacency_list[x].append(y)
            in_degree[y] += 1

    # Topological Sort using Kahn's Algorithm
    queue = [num for num in numbers if in_degree[num] == 0]  # Start with nodes with no dependencies
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current)

        for neighbor in adjacency_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check for cycles (if result doesn't include all numbers, a cycle exists)
    if len(result) != len(numbers):
        raise ValueError("The ordering rules contain a cycle, so a valid ordering is not possible.")

    # Return the result as a comma-delimited string
    return ','.join(map(str, result))

# Calculate and pretty print the answer to part two

corrected_middle_sum = sum(0 if validate_order(ordering, xy_rules) else middle_number(reorder_numbers(ordering, xy_rules)) for ordering in orderings)
print(f'Sum of reordered and valid middle pages: {corrected_middle_sum}')
