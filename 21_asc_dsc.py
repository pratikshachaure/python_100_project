# 020. Write a program to accept two numbers from user and compare them in C language

# 015. Write a program to accept a number and print if the number is Positive/Negative in C language
number = int(input("Enter the first number: ")) 
second = int(input("Enter the second number: ")) 

if number == second:
    print("Both numbers are equal:", number, second)
elif number > second:
    print("Ascending order:", second, number) 
    print("Descending order:", number, second)
else:
    print("Ascending order:", number, second) 
    print("Descending order:", second, number)
