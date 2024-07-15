# 051. Write a program to print digits, alphabets in capital and lower case in Python
# print("The special characters are:- ")

for i in range(1,255):
    if i>=33 and i<=47:
        print("special char :- ",chr(i))
    elif i>=48 and i<=57:
        print("digit is :- ",chr(i))
    elif i>=65 and i<=122:
        print("the alphabate :- ",chr(i))

    

