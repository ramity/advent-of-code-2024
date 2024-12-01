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

# Define input

left_list = [3, 4, 2, 1, 3, 3]
right_list = [4, 3, 5, 3, 9, 3]

# Sort input

left_list.sort()
right_list.sort()

# Apply operations to input and calculate desired output

pairwise_list = pairwise_combine(left_list, right_list)
pairwise_distance = pairwise_distance(pairwise_list)

# Pretty print result to console

print(f'Total distance: {pairwise_distance}')
