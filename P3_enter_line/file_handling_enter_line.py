#Add Pseudocode

import time
import sys

#Create an empty list
lines = []

print('='*50, '\n')
#Start an infinite loop
while True:
    line = input("Enter line: ")
    lines.append(line)
    choice = input("Are there more lines y/n? ").lower()

#Validate the user's input
    while choice not in ['y', 'n']:
        print("Invalid input. Please enter 'y' or 'n'.")
        choice = input("Are there more lines y/n? ").lower()
    if choice == 'n':
        break
#Open txt file
with open("mylife.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")

#Add effects
def slow_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07)  # Adjust the sleep time for faster or slower printing

def print_end():
    slow_print("\033[1;33;40m")  # Set text color to yellow
    slow_print("Lines have been written to mylife.txt")
    slow_print("\033[0;0m")  # Reset text color
    print()
    print()

#End the program
print_end()
print('='*50)