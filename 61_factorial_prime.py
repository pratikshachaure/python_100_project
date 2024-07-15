number=int(input("Enter the number :- "))
rem=0
count=0
fact=1
for i in range(1,number+1):
    fact=fact*i
print("The factorial of given number is :- ",fact)

for i in range(1,number+1):
    if number%i==0:
        count+=1
    
if count==2:
    print("The number is Prime ",number)
else:
    print("The number is not prime ",number)
