# ABCDEEDCBA
# ABCD  DCBA
# ABC    CBA
# AB      BA
# A        A



for i in range (0,5,+1):
    row=" "
    ch=65
    ch1=69
    for j in range (0,5,+1):
        if i<=j:
            row+=" "+chr (ch)
            ch+=1
        else:
            row+=""  

    for j in range (0,5,+1):
        if i<=j:
            row+=" "+chr(ch1)
            ch1-=1
             
        else:
            row+="    "   
    print(row)
