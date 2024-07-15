
print("  1")
for i in range (1,6,+1):
    row=" "
    for j in range(1,6,+1):
        if j<=i:
            row+=" "+str(j)
       
        else:
            row+=""
    
    print(row+" 1")