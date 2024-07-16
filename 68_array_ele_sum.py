number=int (input("Enter the length of an array :- "))
mylst=[]
add=0
for i in range(1,number+1):
    element=int (input("Element"))
    mylst.append(element) 
    add=add+element

# mylst.reverse()
print("The addition of  array element is = ",add)
