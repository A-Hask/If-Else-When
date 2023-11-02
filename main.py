# Student data is collected here
studentLast = input("Please enter the student's last name here (If you wish to quit this program, enter 'ZZZ'): ")
# If the user enters ZZZ as the student's last name, the program stops
if studentLast == "ZZZ":
    exit()

# If the user enters a last name, the program continues to get the remainder of the information
studentFirst = input("Please enter the student's first name: ")
gpa = float(input("Please enter the student's GPA: "))

if gpa >= 3.50:
    print(studentFirst + " " + studentLast + " is on the Dean's List!")

elif gpa >= 3.25:
    print(studentFirst + " " + studentLast + " is on the Honor Roll!")
    
else:
    exit()