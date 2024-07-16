import numpy as np
row=int(input("Enter the row length_"))
column=int(input("Enter the column length_"))
a=np.zeros((row,column))
print(a)
for i in range (row):
     
    for j in range (column):
        a[i][j]=int (input("Enter element "))




print("The array is :- ",a)