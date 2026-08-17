import csv
import os
from abc import ABC, abstractmethod


# =========================================================
# 1. ABSTRACT CLASS
# =========================================================

class Person(ABC):

    @abstractmethod
    def display(self):
        pass


# =========================================================
# 2. STUDENT CLASS
# =========================================================

class Student(Person):

    def __init__(self, sid, name, age, course, marks):
        self.__sid = sid
        self.__name = name
        self.__age = age
        self.__course = course
        self.__marks = marks

    # ---------- Getters ----------

    def get_sid(self):
        return self.__sid

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_course(self):
        return self.__course

    def get_marks(self):
        return self.__marks

    # ---------- Setters ----------

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_course(self, course):
        self.__course = course

    def set_marks(self, marks):
        self.__marks = marks

    # ---------- Polymorphism ----------

    def display(self):
        print(
            f"ID: {self.__sid}, "
            f"Name: {self.__name}, "
            f"Age: {self.__age}, "
            f"Course: {self.__course}, "
            f"Marks: {self.__marks}"
        )


# =========================================================
# 3. STUDENT MANAGER CLASS
# =========================================================

class StudentManager:

    FILE_NAME = "students.csv"

    # ---------- Create CSV ----------

    def create_file(self):

        if not os.path.exists(self.FILE_NAME):

            with open(self.FILE_NAME, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "ID",
                    "Name",
                    "Age",
                    "Course",
                    "Marks"
                ])

    # ---------- Search Student ----------

    def search_student_return(self, sid):

        with open(self.FILE_NAME, "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                if row["ID"] == sid:
                    return row

        return None

    # ---------- Add Student ----------

    def add_student(self):

        try:

            sid = input("Enter Student ID: ").strip()

            # Check duplicate ID
            if self.search_student_return(sid):
                print("Student ID already exists.")
                return

            name = input("Enter Name: ").strip()

            if not name:
                print("Name cannot be empty.")
                return

            age = int(input("Enter Age: "))

            if age <= 0:
                print("Age must be greater than 0.")
                return

            course = input("Enter Course: ").strip()

            if not course:
                print("Course cannot be empty.")
                return

            marks = float(input("Enter Marks: "))

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
                return

            student = Student(
                sid,
                name,
                age,
                course,
                marks
            )

            with open(
                self.FILE_NAME,
                "a",
                newline=""
            ) as file:

                writer = csv.writer(file)

                writer.writerow([
                    student.get_sid(),
                    student.get_name(),
                    student.get_age(),
                    student.get_course(),
                    student.get_marks()
                ])

            print("Student Added Successfully.")

        except ValueError:
            print("Invalid numeric input.")

    # ---------- View Students ----------

    def view_students(self):

        with open(self.FILE_NAME, "r", newline="") as file:

            reader = csv.DictReader(file)

            students_found = False

            for row in reader:

                students_found = True

                student = Student(
                    row["ID"],
                    row["Name"],
                    row["Age"],
                    row["Course"],
                    row["Marks"]
                )

                student.display()

            if not students_found:
                print("No students found.")

    # ---------- Search Student ----------

    def search_student(self):

        sid = input("Enter Student ID to search: ").strip()

        student = self.search_student_return(sid)

        if student:

            print("\nStudent Found")

            print("--------------------")
            print("ID:", student["ID"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Course:", student["Course"])
            print("Marks:", student["Marks"])

        else:

            print("Student Not Found.")

    # ---------- Update Student ----------

    def update_student(self):

        sid = input("Enter Student ID to update: ").strip()

        rows = []
        found = False

        with open(self.FILE_NAME, "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                if row["ID"] == sid:

                    found = True

                    print("\nEnter New Details")

                    name = input("Enter Name: ").strip()

                    age = int(input("Enter Age: "))

                    course = input("Enter Course: ").strip()

                    marks = float(input("Enter Marks: "))

                    row["Name"] = name
                    row["Age"] = age
                    row["Course"] = course
                    row["Marks"] = marks

                rows.append(row)

        if not found:

            print("Student Not Found.")
            return

        with open(
            self.FILE_NAME,
            "w",
            newline=""
        ) as file:

            fieldnames = [
                "ID",
                "Name",
                "Age",
                "Course",
                "Marks"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(rows)

        print("Student Updated Successfully.")

    # ---------- Delete Student ----------

    def delete_student(self):

        sid = input("Enter Student ID to delete: ").strip()

        rows = []
        found = False

        with open(self.FILE_NAME, "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                if row["ID"] == sid:

                    found = True

                else:

                    rows.append(row)

        if not found:

            print("Student Not Found.")
            return

        with open(
            self.FILE_NAME,
            "w",
            newline=""
        ) as file:

            fieldnames = [
                "ID",
                "Name",
                "Age",
                "Course",
                "Marks"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(rows)

        print("Student Deleted Successfully.")


# =========================================================
# 4. MAIN PROGRAM
# =========================================================

def main():

    manager = StudentManager()

    # Create CSV if it doesn't exist
    manager.create_file()

    while True:

        print("\n================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("================================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            manager.add_student()

        elif choice == "2":

            manager.view_students()

        elif choice == "3":

            manager.search_student()

        elif choice == "4":

            try:
                manager.update_student()

            except ValueError:
                print("Invalid numeric input.")

        elif choice == "5":

            manager.delete_student()

        elif choice == "6":

            print("Thank you for using Student Management System.")
            break

        else:

            print("Invalid Choice.")


# =========================================================
# 5. PROGRAM START
# =========================================================

if __name__ == "__main__":
    main()

