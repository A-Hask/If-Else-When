# Student GPA Checker
#   Arlene Haskins
#   This app takes a student's first and last name and their GPA
#   and prints out a statement if they are on the Dean's list or Honor roll.

studentLast = input("Please enter the student's last name: ")
studentFirst = input("Please enter the student's first name: ")
gpa = float(input("Please enter the student's GPA: "))

if studentLast == "ZZZ":
    quit

if gpa >= 3.50:
    print(studentFirst + " " + studentLast + " is on the Dean's List!")

if gpa >= 3.25:
    print(studentFirst + " " + studentLast + " is on the Honor Roll!")