# Open the input file
with open('students.txt', 'r') as my_file:
    # Read the contents of the file
    lines = my_file.readlines()

# Initialize variables
highest_gwa = 0.0
highest_student = ''

# Loop through each line in the file
for line in lines:
    # Split the line into name and GWA
    student_data = line.strip().split(',')
    name = student_data[0]
    gwa = float(student_data[1])

    # Check if the GWA is within the valid range
    if gwa < 1.00 or gwa > 5.00:
        print(f"Warning: {name}'s GWA ({gwa}) is outside the valid range (1.00 - 5.00)")
        continue

    # Check if the current GWA is higher than the highest GWA seen so far
    if gwa > highest_gwa:
        highest_gwa = gwa
        highest_student = name

# Output the name of the student with the highest GWA
if highest_student:
    print(f"The student with the highest GWA is {highest_student} with a GWA of {highest_gwa:.2f}")
else:
    print("No valid GWAs found in the input file.")