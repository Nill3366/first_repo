# first_repo
🎓 Student Report Generator

A simple Python script that takes student info and marks, calculates results, displays a report, and saves the data in a CSV file.

##Features
Collects student name, roll number, department, and age.
Accepts 5 subject marks with validation (0–100).
Calculates total, average, percentage, and grade.
Displays a formatted report.
Saves all student data to a CSV file using csv.DictWriter.
How It Works
User enters basic student info (name, roll number, department, age).
For each subject (1 to 5), a while loop ensures marks are valid (between 0 and 100).
Total, average, percentage, and grade are calculated.
A student report is printed.
User specifies a CSV file name.
If the file doesn’t exist, a header is created.
The student data is saved as a row in the CSV file.

##Grade Calculation
Percentage	Grade
90–100	A
80–89	B
70–79	C
60–69	D
Below 60	F

##How to Run
Ensure Python is installed.
Save the script as student_report.py.

##Run the script:

python student_report.py
Follow the prompts to enter student info, marks, and the file name.
Example

##Input:

enter your name : John Doe
enter your roll number : 101
enter your Department name : Computer Science
enter your age : 20
enter your subject 1 mark: 85
enter your subject 2 mark: 90
...

##Output:

STUDENT REPORT

Subject 1 : 85.0
Subject 2 : 90.0
...
Total: 433
Average: 86.6
Percentage: 86.6
Grade: B

Student data saved successfully!
Project Structure
student-report-generator/
│
├── student_report.py
├── student_info.csv (created by the script)
└── README.md
License

Open source. Feel free to use and modify!

Author

Nilesh Waghmare
A learning project to practice Python basics and CSV file handling.


