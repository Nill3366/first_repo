# first_repo
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
