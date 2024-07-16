string="hellow to string and i want to find now volwels."
char_count=0
for i in range (len(string)):
    if string[i]=='a' or string[i]=='e'or string[i]=='i'or string[i]=='o'or string[i]=='u':
        char_count+=1 
print("The total volwels in the string are :- ",char_count)