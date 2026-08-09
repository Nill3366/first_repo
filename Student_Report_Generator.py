import csv  # csv gives us tools for working with CSV files.
import os  # os lets us interact with the operating system, including checking whether a file exists.


student_name = input("enter your name : ")  # input is basically used to take input from the user, to get student info, marks and everything
roll_number = int(input("enter your roll number : "))
Department = input("enter your Department name : ")
age = int(input("enter your age : "))


def get_valid_mark(subject_number):
    while True:
        try:
            mark = float(
                input(f"enter your subject {subject_number} mark: ")
            )

            if 0 <= mark <= 100:
                return mark
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")


Subject_1 = get_valid_mark(1)  # invoke the function means calling the function by its name and storing the returned value in a variable
Subject_2 = get_valid_mark(2)
Subject_3 = get_valid_mark(3)
Subject_4 = get_valid_mark(4)
Subject_5 = get_valid_mark(5)


total = Subject_1 + Subject_2 + Subject_3 + Subject_4 + Subject_5  # I performed some arithmetic operations
average = total / 5
percentage = total / 500 * 100


if percentage >= 90:  # I used if, elif and else statements to find the student's grade
    grade = "A"  # and stored the value in a variable
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"


print("_" * 25)
print("\n     STUDENT REPORT")
print("_" * 25)

print(f"Subject_1 : {Subject_1}")  # print is a built-in function; we use it to display the value on the console
print(f"Subject_2 : {Subject_2}")
print(f"Subject_3 : {Subject_3}")
print(f"Subject_4 : {Subject_4}")
print(f"Subject_5 : {Subject_5}\n")

print(f"total : {total}")
print(f"average : {average}")
print(f"percentage : {percentage}\n")
print(f"Grade : {grade}")


# -----------------------------
# FILE HANDLING
# -----------------------------

File_Name = input(
    "enter your file name where you want to store data "
)  # write your file name with .csv extension, for instance name.csv

file_exists = os.path.exists(File_Name)  # this checks whether the file exists or not


# -----------------------------
# CSV FIELD NAMES
# -----------------------------

fieldnames = [
    "Name",
    "Roll Number",
    "Department",
    "Age",
    "Subject 1",
    "Subject 2",
    "Subject 3",
    "Subject 4",
    "Subject 5",
    "Total",
    "Average",
    "Percentage",
    "Grade"
]  # these are the column names that will be stored in the CSV file


# -----------------------------
# OPEN CSV FILE
# -----------------------------

with open(File_Name, "a", newline="") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )  # DictWriter is used because we are storing student data as a dictionary


    # Create header if file doesn't exist

    if not file_exists:  # if the file does not exist, it will create the header
        writer.writeheader()  # writeheader() writes the fieldnames as the first row of the CSV file


    # Write student data

    student_data = {
        "Name": student_name,
        "Roll Number": roll_number,
        "Department": Department,
        "Age": age,
        "Subject 1": Subject_1,
        "Subject 2": Subject_2,
        "Subject 3": Subject_3,
        "Subject 4": Subject_4,
        "Subject 5": Subject_5,
        "Total": total,
        "Average": average,
        "Percentage": percentage,
        "Grade": grade
    }  # I stored all student information inside a dictionary


    writer.writerow(student_data)  # this code puts the dictionary values into the correct columns in the CSV file


print("\nStudent data saved successfully!")  # after that this message will print on the console
