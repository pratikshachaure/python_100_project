number=int(input("Enter the length:- "))
a=0
b=1
c=0
print("The fibonacci elements are :- ")
for i in range (1,number+1):
    print(a)
    c=a+b
    a=b
    b=c