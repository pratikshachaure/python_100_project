for i in range(1,6):
    row=" "
    for j in range(1,6):
        
        if i==1 or j==1 or j==5 or i==5:
            row+=" * "
        else:
            row+="   "
    print(row)