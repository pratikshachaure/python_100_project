number=int (input("Enter the length of an array :- "))
mylst=[]
for i in range(1,number+1):
    element=int (input("Element"))
    mylst.append(element) 
print("The array is = ",mylst)
mylst.sort()
print("Ascending array = ",mylst)
mylst.reverse()
print("Descending array :-",mylst)