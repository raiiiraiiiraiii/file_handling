#Pseudocode

import time
import sys

#Open source file (integers.txt) to read
with open('integers.txt', 'r') as source_file:
    # Read the integers from the source file
    integers = [int(line.strip()) for line in source_file.readlines()]

#Open output files (double.txt and triple.txt) for writing
with open('double.txt', 'w') as double_file, open('triple.txt', 'w') as triple_file:
    for num in integers:
        # Check if the number is even or odd
        if num % 2 == 0:
            # Write the square of even numbers to 'double.txt'
            double_file.write(str(num ** 2) + '\n')
        else:
            # Write the cube of odd numbers to 'triple.txt'
            triple_file.write(str(num ** 3) + '\n')
#Message to confirm the success of the program
def slow_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07)  # Adjust the sleep time for faster or slower printing

def print_end():
    slow_print("\033[1;33;40m")  # Set text color to yellow
    slow_print("The files double.txt and triple.txt has been created successfully🎉")
    slow_print("\033[0;0m")  # Reset text color

print_end()