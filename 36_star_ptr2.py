
# 034. Write a program to print following outputs in Python

# *
# **
# ***
# *****
# ******


for i in range (0,6,+1):
    row=""
    
    for j in range (0,6,+1):
        if i<=j:
            row+=" *"
        else:
            row+="  " 
    print(row)
