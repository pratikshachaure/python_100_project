number=int (input("Enter the number :- "))
add=0
 
for i in range(1,number+1):
    newnum=int(input("enter newNum: -"))
    add=add+newnum

avg=add/number
print("The average is :- ",avg)

