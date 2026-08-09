# first_repo
🎓 Student Report Generator

A simple Python script that takes student info and marks, calculates results, displays a report, and saves the data in a CSV file. 📊

🌟 Features
🧑‍🎓 Collects student name, roll number, department, and age.
📚 Accepts 5 subject marks (validated between 0 and 100).
🧮 Calculates total, average, percentage, and grade.
📄 Displays a student report.
💾 Saves data to a CSV file using csv.DictWriter.
📋 How It Works
Enter student info: name, roll, department, age.
For each subject, a while loop ensures valid marks (0–100).
Calculates total, average, percentage, and assigns a grade.
Shows a formatted student report.
Saves data to a CSV file.
🏅 Grading
Percentage	Grade
90–100	A
80–89	B
70–79	C
60–69	D
Below 60	F
▶️ How to Run
Ensure Python is installed.

Run the script:

python student_report.py  
Enter details and marks when prompted.
📁 Project Structure
student-report-generator/
│
├── student_report.py
├── student_info.csv (created)
└── README.md
🧑‍💻 Author

Nilesh Waghmare
A learning project to practice Python basics
