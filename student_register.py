""" This program will ask the teacher for the name of the class/exam,
the date, the name of the teacher and also the number of students.
Once these details are input the program will then ask each student to
enter their unique student ID"""


class ExamRegister:
    def __init__(self, name, date, instructor_name):
        self.exam_name = name
        self.exam_date = date
        self.teacher_name = instructor_name
        self.student_ids = []

    # Stores student ID's and prints with a line for signing underneath
    def add_student_id(self, id_number):
        line = '-' * 80
        self.student_ids.append(f"{id_number}\n{line}")

    # Saves all input data to a .txt file and prints Class/Exam, Date & Teacher Name as a header
    def save_to_file(self):
        with open("reg_form.txt", "w") as reg_file:
            header = (f"Class/Exam: {self.exam_name}\t\t"
                      f"Date: {self.exam_date}\t\t"
                      f"Teacher: {self.teacher_name}\n\n")
            reg_file.write(header)
            for id_number in self.student_ids:
                reg_file.write(f"{id_number}\n")


# The program, asks class/exam name, date, teachers name and amount of students
if __name__ == "__main__":
    class_exam_name = input("Enter the class/exam name: \n").capitalize()
    class_exam_date = input("Enter the date of the class/exam (e.g. DD-MM-YYYY): \n")
    teacher_name = input("Enter your name: \n").capitalize()
    amount_students = int(input("Enter the amount of students: \n"))

    # Confirm details with the teacher
    print(f"\nYou have entered:\n"
          f"\nClass/Exam Name: {class_exam_name}\n"
          f"\nDate: {class_exam_date}\n"
          f"\nTeacher's Name: {teacher_name}\n"
          f"\nNumber of Students: {amount_students}\n")
    confirmation = input("Are these details correct? (Y/N): \n").strip().upper()
    if confirmation != "Y":
        print("\nPlease restart the program and enter the correct details.")
        exit()  # Program restarts if 'Y' isn't selected

    exam_register = ExamRegister(class_exam_name, class_exam_date, teacher_name)
# Asks the students for their unique ID number
    for _ in range(amount_students):
        student_id_input = input("Enter your student ID number: ")
        exam_register.add_student_id(student_id_input)
# Saves all data to the text file in a readable and usable way
    exam_register.save_to_file()
    print("\nThe register has been saved to 'reg_form.txt'.")
