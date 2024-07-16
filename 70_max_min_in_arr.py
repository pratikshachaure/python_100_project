number=int (input("Enter the length of an array :- "))
mylst=[]
for i in range(1,number+1):
    element=int (input("Element"))
    mylst.append(element) 
print("The array is = ",mylst)

for i in range(0,len(mylst)):
    if mylst[i]>mylst[0]:
        mylst[0]=mylst[i]


print("The maximum elemet :- ",mylst[0])



for i in range(0,len(mylst)):
    if mylst[i]<mylst[0]:
        mylst[0]=mylst[i]


print("The min elemet :- ",mylst[0])