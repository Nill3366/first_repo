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

