import numpy as np
row=int (input("Enter row length:- "))
column=int (input("Enter column length:- "))
first_arr=np.zeros((row,column))
second_arr=np.zeros((row,column))
multiplication=1
add2=0
for i in range (row):
    for j in range (column):
        first_arr[i][j]=int (input("Element : "))
         
        multiplication=multiplication*first_arr[i][j]

        

print("FirstArray :- ",first_arr)
print("Multiplication of arra element sum = ",multiplication)
