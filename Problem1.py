#Pseudocode

#Create a text file named "numbers.txt"

#Open the input file
with open('numbers.txt', 'r') as my_file:
    numbers = my_file.read().split()

#Open the output files
with open('even.txt', 'w') as even_file, open('odd.txt', 'w') as odd_file:
    #Create a loop
    for num in numbers:
        # Check if the number is even or odd
        if int(num) % 2 == 0:
            # Write even numbers to even.txt
            even_file.write(num + '\n')
        else:
            # Write odd numbers to odd.txt
            odd_file.write(num + '\n')

print("Files 'even.txt' and 'odd.txt' have been created successfully.")