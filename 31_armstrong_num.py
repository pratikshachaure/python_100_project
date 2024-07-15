
# 031. Write a program to accept a number from user and check if it is Armstrong number or not i.e. 153 = 1^3 + 5^3 + 3^3 = 153 in C language

number1 = int(input("Enter the number: "))
add = 0  
rem=0
org=number1 

while number1 != 0:
    rem = number1 % 10   
    add = add + rem *rem *rem 
    number1 = number1 // 10   
if org==add:
    print("The number is armstrong ")
else:
        print("The  Number is not armstrong ")
