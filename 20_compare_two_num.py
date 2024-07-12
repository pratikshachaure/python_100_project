# 015. Write a program to accept a number and print if the number is Positive/Negative in C language
number=int (input("Enter the first number :- ")) 
second=int (input("Enter the first number :- ")) 
if number==second:
    print("The both numbers is equal:- ",number,second)
elif number>10:
    print("The first number is greater than second number",number,second)
else:
    print("The first number is less than second ",number,second)