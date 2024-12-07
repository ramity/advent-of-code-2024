from itertools import product

# https://chatgpt.com/share/6754a906-5a90-8011-9aa8-aeab679261f9

# This first method was one character away from being correct.
# It halicinated using addition and subtraction instead despite the
# comment on the line before stating it would be using addition
# and multiplication.

def process_file(filename):
    def evaluate_expression(numbers, operators):
        # Evaluate the expression left-to-right without precedence
        result = numbers[0]
        for i, operator in enumerate(operators):
            if operator == '+':
                result += numbers[i + 1]
            elif operator == '*':
                result *= numbers[i + 1]
        return result

    total_sum = 0  # To store the sum of all valid X values

    with open(filename, 'r') as file:
        for line in file:
            # Parse the line
            line = line.strip()
            if not line:
                continue
            parts = line.split(':')
            X = int(parts[0].strip())
            Y_values = list(map(int, parts[1].strip().split()))

            # Generate all combinations of operators ('+' and '*')
            operator_combinations = product('+*', repeat=len(Y_values) - 1)

            # Check if any combination of operators yields X
            for operators in operator_combinations:
                if evaluate_expression(Y_values, operators) == X:
                    print(X, operators, Y_values)
                    total_sum += X
                    break

    return total_sum

def process_file_with_concatenation(filename):
    def evaluate_expression(numbers, operators):
        # Evaluate the expression left-to-right without precedence
        current_value = numbers[0]
        for i, operator in enumerate(operators):
            if operator == '+':
                current_value += numbers[i + 1]
            elif operator == '*':
                current_value *= numbers[i + 1]
            elif operator == 'concat':
                # Concatenate the current value with the next number
                current_value = int(str(current_value) + str(numbers[i + 1]))
        return current_value

    total_sum = 0  # To store the sum of all valid X values

    with open(filename, 'r') as file:
        for line in file:
            # Parse the line
            line = line.strip()
            if not line:
                continue
            parts = line.split(':')
            X = int(parts[0].strip())
            Y_values = list(map(int, parts[1].strip().split()))

            # Generate all combinations of operators ('+', '*', 'concat')
            operator_combinations = product(['+', '*', 'concat'], repeat=len(Y_values) - 1)

            # Check if any combination of operators yields X
            for operators in operator_combinations:
                if evaluate_expression(Y_values, operators) == X:
                    total_sum += X
                    break

    return total_sum

# The human wrote 3 lines of code today. I was blown away by its ability
# to solve today's puzzle. All of the puzzles so far have been easy to
# implement but difficult to describe to LLMs without doing some amount of
# abstraction/division of the problem into smaller parts. Today's was simple
# enough, but I was very impressed it was able to handle the large prompt
# I provided it.

print(process_file("day-07-input.txt"))
print(process_file_with_concatenation("day-07-input.txt"))
