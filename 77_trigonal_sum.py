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
        if i+j<=6:
            add1=add1+first_arr[j][i]

        

print("FirstArray :- ",first_arr)
print("Sum of diagonal element sum = ",add1)
