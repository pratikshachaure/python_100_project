import numpy as np
row=int(input("Enter the rowLength:- "))
column=int (input("Enter the column length:- "))

a=np.zeros((row,column))
b=np.zeros((row,column))
c=np.zeros((row,column))
for i in range(row):
    for j in range(column):
        a[i][j]=int(input("Element :-"))

print("Array1 ",a) 
for i in range(row):
    for j in range(column):
        b[i][j]=int(input("Element :-"))

print("Array2 ",b)

c=np.array([[a],[b]])
print("The result = ",c)


