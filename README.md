# Prompts:

### Day 01

- Using python, create a script that combines two lists into pairwise format where each element of the result is the pairing of each n element.

- Generate a python script that reads in a specified text file and for each line, pulls a 5 digit number and a following 5 digit number separated by 3 space characters. Return an array of tuples containing the 5 digit numbers.

- Generate a python script that compares two lists and returns a list of counts where each element is the number of instances of the number from list 1 occurring in list 2.

### Day 02

- Generate a python script that reads in a file where each line contains a dynamic list of numbers separated by a space character. Place the values into a list of lists of ints.

- Generate a python method that intakes a list of ints and returns true or false. If the ordering of values in the list only increase or decrease and adjacent values differ by at least one and at most three.

- Generate a python method that intakes a list of ints and returns true or false. If the ordering of values in the list only increase or decrease, adjacent values differ by at least one and at most three, and consider a solutions valid where removing a single element allows for passing the aforementioned conditions.

### Day 03

- Generate a python script that defines a method that intakes a filename and searches the contents of the file using regular expressions. The regular expression should look for instances of "mul(X,Y)" where X and Y are 1 to 3 digit numbers. For each match, the X and Y values should be multiplied and added to a running total. Lastly, return the running total.

- Generate a python script that defines a method that intakes a filename and searches the contents of the file using regular expressions. The first regular expression should extract all text that begins between the substring "do()" and ends with the substring "don't()". For each extracted text, a second regular expression should be used to look for instances of "mul(X,Y)" where X and Y are 1 to 3 digit numbers. For each match, the X and Y values should be multiplied and added to a running total. Lastly, extract the text before the first instance of the substring "do()" and similarly apply the second regular expression, and add its mul expressions to the running total. Finally return the running total.

### Day 04

- Generate a python method that intakes a filename, reads that file into a variable, and then treats that variable as the lines of a word search. The word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. This word search is a little different though. There is one valid word, but it is provided numerous times. Given a target search word, calculate the total number of occurrences of that word. 

- Without using any external packages, generate a python method that intakes a filename and target pattern. The target pattern can be a multiline string and can contain wildcard character "*". Read in the contents of the filename and treat it as 2d data composed of rows and columns. Consider all rotations of the target pattern. Using the target pattern, calculate the total number of instances of the target pattern within the 2d and return its value.

### Day 05

- Generate a python method that intakes a filename. Within the method, open the file and process lines in the format of X|Y where X and Y are numbers. Save the X|Y strings into an array. Process the lines until there is a blank line. Then process each line as a comma delimited string of numbers. Save the comma delimited strings into an array. Return both arrays.

- Without using any external libraries, generate a python method that takes in a comma delimited list of numbers and an array of X|Y strings where X and Y are numbers. The array of X|Y strings are the ordering rules. X|Y means number X must occur before Y. Considering all the rules provided, return the result of if the incoming string follows the incoming rules.

- Generate a python method that intakes a comma delimited string of numbers and returns the number in the middle of the list. Assume the incoming string contains an odd number of numbers.

- Without using any external libraries, generate a python method that takes in a comma delimited list of numbers and an array of X|Y strings where X and Y are numbers. The array of X|Y strings are the ordering rules where X|Y means number X must occur before Y. Correctly reorder the incoming string to follow the required rules and return the result in comma delimited string format.

### Day 06

- Without using any external packages, generate a python method that takes in a filename. Traverse the file line by line, char by char creating a 2d matrix of the file while also looking for one of the following characters ("^",">","V","<"). Return the 2d matrix of strings, the character detected, and its Y and X coordinate tuple.

- Without using any external packages, generate a python method that takes in a 2d matrix of strings, a target substring, and the coordinates to that character in y, x format. The target substring will be one of the following characters ("^",">","V","<"). Return the boolean result of the following conditionals: If "^", check if the character at y - 1 is "#". If ">", check if the character at x + 1 is "#". If "V", check if the character at y + 1 is "#". If "<", check if the character at x - 1 is "#". Foreach of the aforementioned conditionals, return false if the proposed x or y coord is out of bounds of the matrix.

- Without using any external packages, generate a python method that takes in a 2d matrix of strings and coordinates in y, x format. Return if the provided coordinates are out of bounds or not.

- Without using any external packages, generate a python method that takes in a 2d matrix of strings, a target substring, and the coordinates to that character in y, x format. The target substring will be one of the following characters ("^",">","V","<"). Replace the target character with "X". If the incoming target substring was "^", place that character at y - 1. If the incoming target substring was ">", place that character at x + 1. If the incoming target substring was "V", place that character at y + 1. If the incoming target substring was "<", place that character at x - 1. Update the coords even if the new coords are invalid and return the updated matrix and coordinates.

- Without using any external packages, generate a python method that takes in a 2d matrix of strings, a target substring, and the coordinates to that character. The target substring will be one of the following characters ("^",">","V","<"). Don't validate if the provided or new coordinates are out of bounds and assume the provided coordinates are given in x, y and accessed in matrix[y][x] format. Return both the result of changing the target character in the matrix to the next possible character and the new character utilized. For example, ^ changes to >, > changes to V, and so on.

- Without using any external packages, generate a python method that takes in a 2d matrix of strings. Count the number of occurrences of the character "X" and return its value.

- Generate a python script that takes in a 2d matrix of strings and pretty prints its contents to the console. Also include a border at the bottom to separate invocations from one another.

### Day 07

- Generate a python method that intakes a filename. Process that file line by line. Each line will be in the format of X: Y1 Y2 ... Yn. The goal is to determine if there exists an arrangement of the + and * operators between Y elements to generate the resulting sum X. Computations are evaluated left to right and do not consider operator precedence. Sometimes the value X cannot be achieved. Return the sum of all X values that were possible to be computed.

- (Extend your solution to also handle the concatenation in addition to addition and multiplication.)

### Day 08

- Generate a python method that intakes a filename. In this method, a file is read into a 2d matrix. This 2d matrix is a map of objects where "." denotes an empty space and any alphanumeric character denotes an object. Objects are grouped by their corresponding character. Iterate over all characters and then foreach pairs of the same character, generate the points that would occur immediately before and after the provided points that fall on the same slope. For both generated points, increase a counter and place a # character if it falls within the boundaries of the map on a "." character. If the value falls within the boundaries but there exists a different type of character, increment the count anyways, but don't replace the character present. Lastly, return the count.

### Day 09

- Generate a python method that intakes a filename. Read the file character by character and read each character into an array. Initialize a counter variable to 0 and an "output" array. Then iterate over the character array. For even indices, append the counter value N number of times, where N is the incoming character array value, and increment the counter variable. For odd indices, append "." N number of times, where N is the coming character array value. Finally return the output array.

- Write a Python method that takes an array as input. Iterate over the array from right to left. Within that loop, create a loop to figure out the first find the first "." left most element between 0 and N where N is the element index of the outer loop. Then, if the incoming right to left element is a non "." element, switch that element with the found left most "." element. Return the modified array.

- Write a Python method that takes in a file path as input. Initialize a files array and a space array. Create a var for containing the running index value and a running ID value. Read in the file digit by digit. For each even file index, append an object to file array with property ID with value index, property size with the incoming digit value, and property index with value running_index. Lastly increment the ID by one. For each odd file index, append an object to the space array with the same properties but without an ID. Outside the conditional add the digit to the running_index. Return the files and space arrays.

- Generate a python array that intakes an array. Iterate over each object in the array. If the object has property size with value 0, remove it from the array. Return the modified array.

- Generate a python method that intakes two arrays, files and space. Iterate over the file array right to left. Within that loop, iterate over the space array left to right. Check if the given space element object's property size is equal to or greater than the file element's property size. If so, change the file element's index to the space element's index, change the space element's size equal to its size minus the file element's size, and change the space element's index property to its index + file element's size. Return the modified files and space arrays.

- Generate a python method that intakes an array of objects. Sort the objects by key "index". Return the sorted array of objects.

- Generate a python method that intakes an array of objects. Create a running sum variable. Iterate over each element of the object. For loop over a range with size of object['index'] to object['index'] + object['size']. Add the product of object['ID'] * the loop index to the running sum. Return the running sum.

### Day 10

- Generate a python method that intakes a file name, reads that file into a 2d array called map, each element is either a digit or ".". Finds all paths from 0 to 9 using only cardinal directions where each step increases value by 1. "." paths are not traversable. 

- Generate a python method that intakes a file name, reads that file into a 2d array called map, where each element is either a digit or ".". From each 0 in the map, check its cardinal neighbors, if its neighbor is the originating value + 1, move to that neighbor and repeat the process until digit 9 is reached, incrementing a counter. After considering all elements, return the counter. Be sure to consider every possible path.
