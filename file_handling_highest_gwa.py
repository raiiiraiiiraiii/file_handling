#Pseudocode

#Decided to add effects
#Import
import time
import sys

#Open the input file and read its content
with open('students.txt', 'r') as my_file:
    lines = my_file.readlines()

#Inialize variables
highest_gwa = 0.0
highest_student = ''

#Add effect on Congratulating the highest student
def slow_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07)  # Adjust the sleep time for faster or slower printing

def print_congratulations(highest_student):
    message = f"🎉🎉🎉Congratulations, {highest_student}!🎉🎉🎉"
    slow_print("\033[1;33;40m")  # Set text color to yellow
    slow_print(message.center(75))
    slow_print("\033[0;0m")  # Reset text color
    print()
    print()
    print("=" * 80)

#Loop through each line of the file to determine the who has the highest GWA
for line in lines:
    # Split the line into name and GWA
    student_info = line.strip().split(',')
    name = student_info[0]
    gwa = float(student_info[1])

    # Check if the GWA is within the valid range
    if gwa < 1.00 or gwa > 5.00:
        print(f"Warning: {name}'s GWA ({gwa}) is beyond the valid range (1.00 - 5.00)")
        continue

    # Check if the current GWA is higher than the highest GWA seen so far
    if gwa > highest_gwa:
        highest_gwa = gwa
        highest_student = name

print("="*80)
print()
#Display the output
if highest_student:
    result = f"The student with the highest GWA is {highest_student} with a GWA of {highest_gwa:.2f}"
    print(result.center(80))

    print_congratulations(highest_student)
else:
    print("No valid GWAs in the input file.")