for i in range(65, 70):
    row = ""
    for j in range(65-1, i):
        if i + j >= 128:  
            row += chr(i)
        else:
            row += " "
    print(row)
 