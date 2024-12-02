import re

# https://chatgpt.com/share/674cf05e-6b48-8011-93b1-441c0ed10036

def pairwise_combine(list1, list2):
    """
    Combine two lists into pairwise format where each element is a tuple
    containing the corresponding elements of the lists.

    Parameters:
    list1 (list): The first list.
    list2 (list): The second list.

    Returns:
    list: A list of tuples containing pairwise elements from the two lists.
    """
    return [(list1[i], list2[i]) for i in range(min(len(list1), len(list2)))]

# Using above as reference, I create the following method to calculate the total distance

def pairwise_distance(pairwise_list):

    return sum(abs(pairwise_list[i][0] - pairwise_list[i][1]) for i in range(len(pairwise_list)))

# After authing, I discovered we have to read in some input, so I asked chatGPT to generate a script to handle it.
# Using regular expressions for this is rather overkill, but the idea of this exercise is to show off using AI input.
# https://chatgpt.com/share/674cf502-3cc4-8011-8ac6-6bd7cfe4d424

def extract_numbers(file_path):
    """
    Reads a file and extracts pairs of five-digit numbers separated by three spaces.

    Args:
        file_path (str): The path to the text file.

    Returns:
        tuple: Two lists - first list contains all the first numbers, 
               second list contains all the second numbers.
    """
    pattern = r'(\d{5})   (\d{5})'  # Regex for two 5-digit numbers separated by 3 spaces
    first_numbers = []
    second_numbers = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                matches = re.findall(pattern, line)
                for match in matches:
                    # Slight manual modification to cast as ints
                    first_numbers.append(int(match[0]))
                    second_numbers.append(int(match[1]))
    except FileNotFoundError:
        print(f"Error: File at {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return first_numbers, second_numbers

# Define input

left_list, right_list = extract_numbers("./day-01-input.txt")

# Sort input

left_list.sort()
right_list.sort()

# Apply operations to input and calculate desired output

pairwise_list = pairwise_combine(left_list, right_list)
pairwise_distance = pairwise_distance(pairwise_list)

# Pretty print part one result to console

print(f'Total distance: {pairwise_distance}')

# Now we need to count the number of occurrences of a left_list elements in right_list.
# https://chatgpt.com/share/674cf785-e9f0-8011-8f1b-b74fbdb801ba

def count_occurrences(list1, list2):
    """
    Compare two lists and return a list of counts where each element is the
    number of instances of the number from list1 occurring in list2.

    :param list1: List of elements to count in list2
    :param list2: List in which to count occurrences
    :return: List of counts
    """
    counts = [list2.count(element) for element in list1]
    return counts

# I manually create a wrapping function to summate the counts array result from the count_occurrences method

def similarity_score(list1, list2):

    occurrences = count_occurrences(list1, list2)
    return sum(occurrences[i] * list1[i] for i in range(len(list1)))

similarity_score = similarity_score(left_list, right_list)

# Pretty print part two answer to console

print(f'Similarity score: {similarity_score}')
