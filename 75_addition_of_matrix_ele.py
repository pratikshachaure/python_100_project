import numpy as np
row=int (input("Enter row length:- "))
column=int (input("Enter column length:- "))
first_arr=np.zeros((row,column))
second_arr=np.zeros((row,column))
add1=0
add2=0
for i in range (row):
    for j in range (column):
        first_arr[i][j]=int (input("Element : "))
        add1=add1+first_arr[i][j]

print("FirstArray :- ",first_arr)
print("first sum = ",add1)


for i in range (row):
    for j in range (column):
        second_arr[i][j]=int (input("Element : "))
        add2=add2+second_arr[i][j]


print("second array = ",second_arr)

print("Second_arrya sum = ",add2)


allelementSum=add1+add2

print("The sum is :- ",allelementSum)