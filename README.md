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

