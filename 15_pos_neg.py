# 015. Write a program to accept a number and print if the number is Positive/Negative in C language
number=int (input("Enter the first number :- ")) 
if number>0:
    print("The number is positive :- ",number)
elif number==0:
    print("The number is zero ",number)
else:
    print("The number is negative ",number)