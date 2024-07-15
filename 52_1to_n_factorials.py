number=int (input("Enter the number :- "))
add=0
for i in range (1,number+1):
    fact=1
    for j in range (1,i+1):
        fact=fact*j
        
    print(i," = ","Factorial = ",fact)