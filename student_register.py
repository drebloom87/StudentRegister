# This program will log the amount of students taking an exam and print each student ID to a text file with a line for
# each student to sign and show they have attended the exam
student_id = []  # Used to store the ID's to a list
line = '-' * 80  # Used to print a line for signing after the ID is printed

registered_students = int(input("Enter the amount of students entering: "))  # Stores amount of students as an int

for students in range(registered_students):  # Will loop through the number entered above and terminate when reached
    id_number = (input("Enter your student ID number: "))  # Used to store each student ID entered
    student_id.append(id_number + '\n' + line)  # Joins the student ID with line underneath for each signature
    with open("reg_form.txt", "w") as register:  # Opens the text file in order to create the register
        register.write('\n'.join(student_id))  # Prints ID number with a line underneath as a list in a txt file
