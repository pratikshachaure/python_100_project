# 008. Write a program to print simple interest SI = (PNR)/100 in C language
pinciple_amout=int (input("Enter the amount :-"))
number_period=int (input ("Enter the period:- "))
rate=int (input("Enter the rate :- "))
simple_interest=pinciple_amout*number_period*rate
print("Simple interest = ",simple_interest)