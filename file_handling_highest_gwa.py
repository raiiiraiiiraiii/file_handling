#Pseudocode

#Decided to add effects
#Import

#Add effect on Congratulating the highest student

#Open the input file and read its content
with open('students.txt', 'r') as my_file:
    lines = my_file.readlines()

#Inialize variables
highest_gwa = 0.0
highest_student = ''

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

#Display the output
if highest_student:
    print(f"The student with the highest GWA is {highest_student} with a GWA of {highest_gwa:.2f}")
else:
    print("No valid GWAs in the input file.")