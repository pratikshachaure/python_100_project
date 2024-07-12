
# 011. Write a program to accept roll no and marks of 3 subjects of a student, Calculate total of 3 subjects and average in Python

roll_number=int(input("Enter the roll number :- "))
subject1=int(input("Enter the marks of first_subject :- "))
subject2=int(input("Enter the marks of subject_two :-"))
subject3=int(input("Enter the marks of subject_three :- "))

total_marks=subject1+subject2+subject3
average=total_marks/3
print("The total average is :- ",average)