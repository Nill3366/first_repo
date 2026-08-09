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
print(f"Subject_2 : {Subject_2}")
print(f"Subject_3 : {Subject_3}")
print(f"Subject_4 : {Subject_4}")
print(f"Subject_5 : {Subject_5}\n")


print(f"total : {total}")
print(f"average : {average}")
print(f"percentage : {percentage}\n")
print(f"Grade : {grade}")
