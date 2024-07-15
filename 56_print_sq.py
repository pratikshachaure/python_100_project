for i in range(1, 6):
    row = ""
    for j in range(1, 6):
        if i == 1 or i == 5:  
            # Top or bottom border
            row += " --" 
        elif j == 1 or j == 5:  # Left or right border
            row += " |"
        else:  # Inside the border
            row += "    "
    print(row)
