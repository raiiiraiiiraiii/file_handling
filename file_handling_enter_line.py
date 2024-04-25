#Add Pseudocode

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
#End the program
print("Lines have been written to mylife.txt\n")
print('='*50)