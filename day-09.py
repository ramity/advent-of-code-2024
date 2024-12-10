# https://chatgpt.com/share/67579b40-609c-8011-9ac7-2e2b3ab0c7c3

def process_file(filename):
    """
    Reads a file character by character into an array and processes the array based on even and odd indices.

    Parameters:
        filename (str): The name of the file to process.

    Returns:
        list: The processed output array.
    """
    # Read the file character by character into an array
    with open(filename, 'r') as file:
        char_array = list(file.read().strip())  # Strip to remove extra spaces or newlines

    # Initialize variables
    counter = 0
    output = []

    # Iterate over the character array
    for i, char in enumerate(char_array):
        try:
            # Convert the character to an integer
            N = int(char)
        except ValueError:
            # Skip non-numeric characters
            continue

        if i % 2 == 0:
            # For even indices, append the counter value N times and increment counter
            output.extend([counter] * N)
            counter += 1
        else:
            # For odd indices, append "." N times
            output.extend(['.'] * N)

    return output

# https://chatgpt.com/share/67579b4d-9398-8011-86c7-ade699004149

def swap_dots(arr):
    # Iterate from right to left
    for i in range(len(arr) - 1, -1, -1):
        print(f"{i}", end="\r")
        if arr[i] != '.':  # If current element is not a dot
            # Find the leftmost dot (.) from index 0 to i
            for j in range(i):
                if arr[j] == '.':
                    # Swap the non-dot element with the leftmost dot
                    arr[j], arr[i] = arr[i], arr[j]
                    break
    return arr

def sum_index_multiplication(arr):
    sum_var = 0
    for i, value in enumerate(arr):
        if value != ".":
            sum_var += i * value
    return sum_var

# Human written code to calculate and pretty print answer to part one

# filesystem = process_file("./day-09-input.txt")
# sorted_filesystem = swap_dots(filesystem)
# checksum = sum_index_multiplication(sorted_filesystem)
# print(checksum)

# Part two benefits from a refactor, so performing that below

# https://chatgpt.com/share/6757e0e8-3c04-8011-9903-07e5efa0108d

def process_file(file_path):
    files = []  # Array to hold file objects
    space = []  # Array to hold space objects
    running_index = 0  # Running index value
    running_id = 0  # Running ID value

    try:
        with open(file_path, 'r') as file:
            for idx, char in enumerate(file.read()):
                if char.isdigit():  # Process only digits
                    digit = int(char)
                    if idx % 2 == 0:  # Even file index
                        files.append({
                            "ID": running_id,
                            "size": digit,
                            "index": running_index
                        })
                        running_id += 1  # Increment the ID
                    else:  # Odd file index
                        space.append({
                            "size": digit,
                            "index": running_index
                        })
                    
                    running_index += digit  # Update the running index
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return files, space

# https://chatgpt.com/share/6757bb46-6248-8011-85ab-384e9558d4fe

def remove_objects_with_size_zero(input_array):
    # Create a new array to store objects with size other than 0
    modified_array = []

    # Iterate over each object in the input array
    for obj in input_array:
        # Check if the object has a 'size' property and if its value is not 0
        if obj.get('size', 0) != 0:
            modified_array.append(obj)

    # Return the modified array
    return modified_array

# https://chatgpt.com/share/6757e332-5c64-8011-a3d2-0da3d926fad3

def allocate_files_to_space(files, space):
    for file_elem in reversed(files):  # Iterate over files from right to left
        for space_elem in space:  # Iterate over space from left to right
            if space_elem['size'] >= file_elem['size']:
                
                # Update the file's index to match the space's index
                file_elem['index'] = space_elem['index']
                
                # Reduce the space size by the size of the file
                space_elem['size'] -= file_elem['size']
                
                # Update the space index to reflect the used portion
                space_elem['index'] += file_elem['size']
                
                # Stop looking for space for the current file
                break
                
    return files, space

# https://chatgpt.com/share/6757dd60-efbc-8011-b0f9-f55a04d33201

def sort_objects_by_index(objects):
    """
    Sorts an array of objects (dictionaries) by the 'index' key.

    Args:
        objects (list): A list of dictionaries, each containing an 'index' key.

    Returns:
        list: The sorted list of dictionaries by the 'index' key.
    """
    return sorted(objects, key=lambda obj: obj.get('index', 0))

# https://chatgpt.com/share/6757e4ec-a938-8011-89f7-7b74a0eefca7

def calculate_running_sum(array_of_objects):
    """
    Calculate the running sum based on the given array of objects.
    
    Parameters:
        array_of_objects (list): List of objects with keys 'index', 'size', and 'ID'.
    
    Returns:
        int: The calculated running sum.
    """
    running_sum = 0  # Initialize running sum variable
    
    for obj in array_of_objects:  # Iterate over each object in the array
        start = obj['index']
        end = start + obj['size']
        for i in range(start, end):  # Loop over the range from 'index' to 'index' + 'size'
            running_sum += obj['ID'] * i  # Add product of 'ID' and index to running sum
    
    return running_sum

files, space = process_file("./day-09-input.txt")
corrected_space = remove_objects_with_size_zero(space)

# print(files)
# print(corrected_space)
# print('-'*42)

allocated_files, remaining_space = allocate_files_to_space(files, corrected_space)
sorted_allocated_files = sort_objects_by_index(allocated_files)

# print(remaining_space)

corrected_remaining_space = remove_objects_with_size_zero(remaining_space)

# print(corrected_remaining_space)
# print(allocated_files)
# print(sorted_allocated_files)
# print('-'*42)
# print(remaining_space)
# print(calculate_running_sum(sorted_allocated_files))

# The code for part two is non-functional. It doesn't correctly
# consider creating a new space entry for when ID 2 is moved.
# It generates a correct checksum in the small scale example, but
# doesn't for the provided input. I just wasn't interested in the added
# complexity of inserting a new space entry and then having it sort that array every file.
# Mostly because I know the efficient thing to do would be to use a
# data structure or revert to the previous array of digits and . char approach
# and iterate over the array in a complex way when fragmenting.
