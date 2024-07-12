
# 023. Write a program to accept roll number ,and marks for three subjects, print total marks and average, also print grade by considering following conditions

 

roll_number = int(input("Enter the roll number: "))
subject1 = int(input("Enter the marks of first subject: "))
subject2 = int(input("Enter the marks of second subject: "))
subject3 = int(input("Enter the marks of third subject: "))

total_marks = subject1 + subject2 + subject3
print("The total marks: ", total_marks)

average = total_marks / 3
print("The total average is: ", average)
if average>=90:
    print("You passed with Grade A ")
elif average<90 and average>=70:
    print("You passed with Grade B ")
elif average<70 and average>=50:
    print("You passed with Grade C")
else:
    print("You failed keep try again best of luck")
