ch=64
for i in range (0,6,+1):
    row=" "
    
    for j in range (0,6,+1):
        if i+j>=6:
            row+=" "+chr (ch)
            
        else:
            row+=" " 
    ch+=1
    print(row)
