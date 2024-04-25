#Pseudocode

import time
import sys

#Create a text file named "numbers.txt"

#Open the input file
with open('numbers.txt', 'r') as my_file:
    numbers = my_file.read().split()

#Open the output files
with (open('even.txt', 'w') as even_file,
      open('odd.txt', 'w') as odd_file):
    #Create a loop
    for num in numbers:
        # Check if the number is even or odd
        if int(num) % 2 == 0:
            # Write even numbers to even.txt
            even_file.write(num + '\n')
        else:
            # Write odd numbers to odd.txt
            odd_file.write(num + '\n')

#Add effect
def slow_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07)  # Adjust the sleep time for faster or slower printing

def print_end():
    message = "Files 'even.txt' and 'odd.txt' have been created successfully."
    slow_print("\033[1;33;40m")  # Set text color to yellow
    slow_print(message.center(75))
    slow_print("\033[0;0m")  # Reset text color
    print()
    print()

print_end()