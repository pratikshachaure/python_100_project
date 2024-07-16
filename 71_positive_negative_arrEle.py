number=int(input("Enter the lenght:- "))
arr=[]
for i in range(0,number+1):
    element=int(input("Element :- "))
    arr.append(element)

print("The array is :- ",arr)

for i in range (0,len(arr)):
    if arr[i]>0:
        print("Possitive :- ",arr[i])
    else:
        print("Negative :- ",arr[i])