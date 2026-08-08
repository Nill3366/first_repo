# first_repo
# Student Report Generator

A simple Python script that takes student details and subject marks as input, calculates the total, average, and percentage, and prints a formatted student report.

## Features

- Captures student information (Name, Roll Number, Department, and Age).
- Accepts marks for five different subjects.
- Automatically calculates:
  - Total marks obtained.
  - Average marks.
  - Percentage score.
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
Subject_1 : 90.0
Subject_1 : 78.0
Subject_1 : 92.0
Subject_1 : 88.0

total : 433.0
average : 86.6
percentage : 86.6
```

## License

##This project is open-source and available for anyone to use and modify.

student_name=input("enter your name : ")
roll_number= int(input("enter your roll number : "))
Department = input("enter your Department name : ")
age = int(input("enter your age : "))
Subject_1  = float(input("enter your subject 1 mark : "))
Subject_2 =  float(input("enter your subject 2 mark : "))
Subject_3 = float(input("enter your subject 3 mark : "))
Subject_4 = float(input("enter your subject 4 mark : "))
Subject_5 = float(input("enter your subject 5 mark : "))

total=Subject_1 + Subject_2 + Subject_3 + Subject_4 + Subject_5
average =total / 5
percentage= total / 500 * 100

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
