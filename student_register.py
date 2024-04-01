""" This program will ask the teacher for the name and date of the
class/exam, the name of the teacher and also the number of students.
Once these details are input the program will then ask each student to
enter their fullname and unique student ID. The program will then display
all student names and IDs to check if the details are ready to print"""
import os
from datetime import datetime


class ExamRegister:
    def __init__(self, exam_name, exam_date, instructor_name):
        self.exam_name = exam_name
        self.exam_date = exam_date
        self.teacher_name = instructor_name
        self.student_records = []

    # Modified to store student's first name, last name, and ID
    def add_student_record(self, student_first_name, student_last_name, student_id):
        line = '-' * 50
        record = f"{student_first_name} {student_last_name} ({student_id})\n{line}"
        self.student_records.append(record)

    # Method to confirm student details
    @staticmethod
    def confirm_student_details(student_first_name, student_last_name, student_id):
        print(f"\nPlease confirm the following details:\n"
              f"Full Name: {student_first_name} {student_last_name}\n"
              f"Student ID: {student_id}\n")
        student_confirmation = input("Are these details correct? (Y/N): ").strip().upper()
        return student_confirmation == "Y"

    # Saves all input data to a .txt file and prints Class/Exam, Date & Teacher Name as a header
    def save_to_file(self, filename="reg_form.txt"):
        with open(filename, "w") as reg_file:
            # Get today's date in the format DD-MM-YYYY
            today_date = datetime.now().strftime("%d-%m-%Y")
            # Capitalize each part of the teacher's name
            capitalized_teacher_name = self.teacher_name.title()
            # Write the header with the current date
            header = (f"Class/Exam Date: {self.exam_date}\t\t\t"
                      f"Class/Exam: {self.exam_name}\n"
                      f"Register Printed {today_date}\t\t\t"
                      f"Teacher: {capitalized_teacher_name}\n\n")

            # Calculate padding for centering "Student Register"
            total_width = 80  # Adjust this based on your desired total width
            student_register_text = "Student Register"
            padding = (total_width - len(student_register_text)) // 2

            # Write the centered "Student Register"
            reg_file.write(header + " " * padding + student_register_text + "\n\n")
            for record in self.student_records:
                # Write each record followed by a line separator
                reg_file.write(record + '-' * 50 + '\n')

    def display_student_records(self):
        print("\nStudent name and ID records:")
        for index, record in enumerate(self.student_records, start=1):
            # Extract the name and ID and format them as "Student #: Name - ID"
            name_id = record.split('(')[0].strip()
            student_id = record.split('(')[1].split(')')[0]
            print(f"Student {index}: {name_id} ID: {student_id}")

    # Accepts a filename as an argument
    @staticmethod
    def print_file(filename):
        os.startfile(filename, "print")


# The program, asks class/exam name, date, teachers name and amount of students
try:
    exam_name_input = input("Enter the class/exam name: \n").capitalize()
    exam_date_input = input("Enter the date of the class/exam (e.g. DD-MM-YYYY): \n")
    teacher_name_input = input("Enter your name: \n").capitalize()
    try:
        student_count = int(input("Enter the amount of students: \n"))
    except ValueError:
        print("You did not enter a valid number. Please enter an integer value for the number of students.")
        # You can then either exit the program or loop back to ask for the input again
        exit()

    # Confirm details with the teacher
    print(f"You have entered:\n"
          f"\nClass/Exam Name: {exam_name_input}\n"
          f"\nDate: {exam_date_input}\n"
          f"\nTeacher's Name: {teacher_name_input}\n"
          f"\nNumber of Students: {student_count}\n")
    details_confirmation = input("Are these details correct? (Y/N): \n").strip().upper()

    if details_confirmation != "Y":
        print("\nPlease restart the program and enter the correct details.")
        exit()  # Program exits if 'Y' isn't selected

except KeyboardInterrupt:
    print("\nInput was cancelled by the user. Exiting the program.")
    exit()  # Program restarts if 'Y' isn't selected

exam_register = ExamRegister(exam_name_input, exam_date_input, teacher_name_input)
# Asks the students for their full name and unique ID number
for i in range(student_count):
    while True:
        first_name = input("Enter your first name: ").capitalize()
        last_name = input("Enter your last name: ").capitalize()
        if any(char.isdigit() for char in first_name + last_name):
            print("Names cannot contain numbers. Please try again.")
            continue
        student_id_input = input("Enter your student ID number: ")
        if exam_register.confirm_student_details(first_name, last_name, student_id_input):
            exam_register.add_student_record(first_name, last_name, student_id_input)
            break
        else:
            print("Please re-enter the student's details.")

# After the last student has entered their details, display all records
exam_register.display_student_records()

# Save the records to a file
exam_register.save_to_file()

# Ask the teacher if they are ready to print
teacher_confirmation = input("\nAre you ready to print the register? (Y/N): \n").strip().upper()
if teacher_confirmation == "Y":
    # Print the register to the console
    with open("reg_form.txt", "r") as file:
        print(file.read())
    # Print the register to the default printer
    exam_register.print_file("reg_form.txt")
else:
    print("\nPrinting cancelled. The register is saved and can be printed later.")
