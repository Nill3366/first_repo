# first_repo
# Student Report Generator

A simple Python script that takes student details and subject marks as input, calculates the total, average, and percentage, and prints a formatted student report.

## Features

- Captures student information (Name, Roll Number, Department, and Age).
- Accepts five subject marks using robust input validation to ensure only numbers between 0 and 100 are accepted.
- Automatically calculates:
  - Total marks obtained.
  - Average marks.
  - Percentage score.
- Assigns a Grade based on the percentage.
- Displays a clean, formatted report of the results.

## Prerequisites

To run this script, you need to have Python installed on your computer. You can download it from [python.org](https://www.python.org/).

## How to Run

1. Clone this repository or copy the Python script.
2. Open your terminal or command prompt.
3. Navigate to the directory where the script is saved.
4. Run the script using the following command:

```bash
python script_name.py
```

5. Follow the on-screen prompts to enter the student's name, roll number, department, age, and subject marks.

## Example Usage

When you run the script, you will be prompted to enter the data:

```text
enter your name : John Doe
enter your roll number : 101
enter your Department name : Computer Science
enter your age : 20
enter your subject 1 mark : 85
enter your subject 2 mark : 90
enter your subject 3 mark : 78
enter your subject 4 mark : 92
enter your subject 5 mark : 88
```

The script will then output the report:

```text
_________________________

     STUDENT REPORT
_________________________
Subject_1 : 85.0
Subject_2 : 90.0
Subject_3 : 78.0
Subject_4 : 92.0
Subject_5 : 88.0

total : 433.0
average : 86.6
percentage : 86.6
Grade : B
```

## License

##This project is open-source and available for anyone to use and modify.

student_name=input("enter your name : ")
roll_number= int(input("enter your roll number : "))
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


Subject_1 = get_valid_mark(1)
Subject_2 = get_valid_mark(2)
Subject_3 = get_valid_mark(3)
Subject_4 = get_valid_mark(4)
Subject_5 = get_valid_mark(5)

total=Subject_1 + Subject_2 + Subject_3 + Subject_4 + Subject_5
average =total / 5
percentage= total / 500 * 100

if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
else:
    grade = 'F'

print("_"*25)
print("\n     STUDENT REPORT")
print("_"*25)
print(f"Subject_1 : {Subject_1}")
print(f"Subject_1 : {Subject_2}")
print(f"Subject_1 : {Subject_3}")
print(f"Subject_1 : {Subject_4}")
print(f"Subject_1 : {Subject_5}\n")


print(f"total : {total}")
print(f"average : {average}")
print(f"percentage : {percentage}\n")
print(f"Grade : {grade}")
