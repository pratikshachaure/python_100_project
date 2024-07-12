# 024. Write a Program to accept user’s marital status, gender and age to check if he/she is eligible for marriage or not. 

status = input("Enter the marital status (yes or no): ").lower()

if status == "no":
    gender = input("Enter the gender (f or m): ").lower()
    
    if gender == "f":
        age = int(input("Enter the age: "))
        if age >= 18:
            print("You are eligible for marriage.")
        else:
            print("You are not eligible for marriage.")
    
    elif gender == "m":
        age = int(input("Enter the age: "))
        if age >= 21:
            print("You are eligible for marriage.")
        else:
            print("You are not eligible for marriage.")
    
    else:
        print("Invalid gender input. Please enter 'f' for female or 'm' for male.")

else:
    print("You are already married.")

