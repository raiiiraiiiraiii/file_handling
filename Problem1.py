#Pseudocode

#Create a text file named "numbers.txt"

#Open the input file
with open('numbers.txt', 'r') as my_file:
    numbers = my_file.read().split()

#Open the output files
with open('even.txt', 'w') as even_file, open('odd.txt', 'w') as odd_file:

