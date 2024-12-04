import re

# https://chatgpt.com/share/674fbe5d-9d78-8011-8f1a-9686cbcac55b

def calculate_mul_total(filename):
    """
    Reads a file, searches for instances of 'mul(X,Y)' where X and Y are 
    1 to 3 digit numbers, multiplies X and Y, and returns the running total.

    Parameters:
        filename (str): The name of the file to process.

    Returns:
        int: The total sum of the products of all matches.
    """
    # Regular expression to match 'mul(X,Y)' where X and Y are 1-3 digit numbers
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    total = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                matches = re.findall(pattern, line)
                for match in matches:
                    x, y = map(int, match)  # Convert matched strings to integers
                    total += x * y
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return total

# Calculate and pretty print the result for part one

result = calculate_mul_total("./day-03-input.txt")
print(f'Total result: {result}')

# https://chatgpt.com/share/674fc2b8-5948-8011-8f3a-a6deafb5ad61

def calculate_enabled_mul_total(filename):
    # Step 1: Read the contents of the file into a variable
    with open(filename, 'r') as file:
        content = file.read()
    
    # Step 2: Initialize a running total
    running_total = 0
    
    # Step 3: Extract all text between "do()" and "don't()"
    between_texts = re.findall(r"do\(\)(.*?)don't\(\)", content, re.DOTALL)
    
    # Step 4: Process each extracted text to find and calculate mul(X,Y)
    for text in between_texts:
        matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", text)
        for x, y in matches:
            running_total += int(x) * int(y)
    
    # Step 5: Extract text before the first occurrence of "do()" or "don't()"
    before_text_match = re.search(r"^(.*?)(do\(\)|don't\()", content, re.DOTALL)
    if before_text_match:
        before_text = before_text_match.group(1)
        # Step 6: Apply the second regular expression to this text
        matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", before_text)
        for x, y in matches:
            running_total += int(x) * int(y)
    
    # Step 7: Return the running total
    return running_total

# Calculate and pretty print the result for part two

enabled_result = calculate_enabled_mul_total("./day-03-input.txt")
print(f'Enabled result: {enabled_result}')
